class overs_model:
  complete_overs: int
  partial_overs: int

  def __init__(self, complete_overs: int = 0, partial_overs: int = 0, **kwargs):
    self.complete_overs = complete_overs
    self.partial_overs = partial_overs

    for key, value in kwargs.items():
      setattr(self, key, value)
  
  def __add__(self, other: 'overs_model') -> 'overs_model':
    if not isinstance(other, overs_model):
      return NotImplemented
    
    return overs_model(
      self.complete_overs + other.complete_overs + (self.partial_overs + other.partial_overs)//6, 
      (self.partial_overs + other.partial_overs) % 6)
  
  def __str__(self) -> str:
    return f"{self.complete_overs}.{self.partial_overs}"
  
  def to_dict(self) -> dict:
    return {
      "complete_overs": self.complete_overs,
      "partial_overs": self.partial_overs
    }

class best_bowling_model:
  wickets: int
  runs_conceded: int
  enabled: bool

  def __init__(self, wickets: int = 0, runs_conceded: int = 0, **kwargs):
    self.wickets = wickets
    self.runs_conceded = runs_conceded
    self.enabled = False

    for key, value in kwargs.items():
      self.enabled = True
      setattr(self, key, value)

  def update(self, wickets: int, runs_conceded: int) -> None:
    if not self.enabled:
      self.enabled = True
      self.wickets = wickets
      self.runs_conceded = runs_conceded
      return
    
    if wickets < self.wickets:
      return
    
    if wickets == self.wickets and runs_conceded >= self.runs_conceded:
      return
    
    self.wickets = wickets
    self.runs_conceded = runs_conceded
  
  def __str__(self) -> str:
    return f"{self.wickets}-{self.runs_conceded}"
  
  def to_dict(self) -> dict:
    return {
      "enabled": self.enabled,
      "wickets": self.wickets,
      "runs_conceded": self.runs_conceded
    }
  
class bowling_input:
  overs: overs_model
  runs_conceded: int
  wickets: int

  def __init__(self, overs: overs_model = overs_model(), runs_conceded: int = 0, wickets: int = 0):
    self.overs = overs
    self.runs_conceded = runs_conceded
    self.wickets = wickets

  def to_dict(self) -> dict:
    return {
      "overs": self.overs.to_dict(),
      "runs_conceded": self.runs_conceded,
      "wickets": self.wickets
    }

class bowling_model:
  overs: overs_model
  runs_conceded: int
  wickets: int
  bowling_average: float # Average runs per wicket
  economy_rate: float
  best_bowling: best_bowling_model
  purple_caps: int

  def __init__(self, **kwargs):
    self.overs = overs_model()
    self.runs_conceded = 0
    self.wickets = 0
    self.bowling_average = None
    self.economy_rate = None
    self.best_bowling = best_bowling_model()
    self.purple_caps = 0

    for key, value in kwargs.items():
      if key == "overs":
        print("Overs model: ", value)
        self.overs = overs_model(**value)
      elif key == "best_bowling":
        print("Best Bowling model: ", value)
        self.best_bowling = best_bowling_model(**value)
      else:
        setattr(self, key, value)

  def update(self, bowling_input: bowling_input) -> None:
    self.overs += bowling_input.overs
    self.runs_conceded += bowling_input.runs_conceded
    self.wickets += bowling_input.wickets

    if self.wickets > 0:
      self.bowling_average = round(self.runs_conceded / self.wickets, 2)
    
    if self.overs.complete_overs != 0 or self.overs.partial_overs != 0:
      self.economy_rate = round(6 * self.runs_conceded / (self.overs.complete_overs*6 + self.overs.partial_overs), 2)
    self.best_bowling.update(self.wickets, self.runs_conceded)
    
  def award_purple_cap(self) -> None:
    self.purple_caps += 1
  
  def to_dict(self) -> dict:
    return {
      "overs": self.overs.to_dict(),
      "runs_conceded": self.runs_conceded,
      "wickets": self.wickets,
      "bowling_average": self.bowling_average,
      "economy_rate": self.economy_rate,
      "best_bowling": self.best_bowling.to_dict(),
      "purple_caps": self.purple_caps
    }

  def getValues(self) -> list[str]:
    return [
      str(self.overs),
      str(self.runs_conceded),
      str(self.wickets),
      str(self.bowling_average),
      str(self.economy_rate),
      str(self.best_bowling),
      str(self.purple_caps)
    ]

bowling_header_list = [
  "Overs",
  "Runs Conceded",
  "Wickets",
  "Bowler Average",
  "Economy Rate",
  "Best Bowling",
  "Purple Caps"
]

if __name__ == "__main__":
  bowling_update = bowling_input(overs_model(2,3), 45, 2)
  bowling_stats = bowling_model()
  bowling_stats.update(bowling_update)

  from testing.test_utils import expect
  expect(bowling_stats.to_dict()).to_equal({
    "overs": {
      "complete_overs": 2,
      "partial_overs": 3
    },
    "runs_conceded": 45,
    "wickets": 2,
    "bowling_average": 22.5,
    "economy_rate": 18.0,
    "best_bowling": {
      "enabled": True,
      "wickets": 2,
      "runs_conceded": 45
    },
    "purple_caps": 0
  })

  bowling_stats.update(bowling_input(overs_model(1,4), 5, 0))
  expect(bowling_stats.to_dict()).to_equal({
    "overs": {
      "complete_overs": 4,
      "partial_overs": 1
    },
    "runs_conceded": 50,
    "wickets": 2,
    "bowling_average": 25.0,
    "economy_rate": 12.0,
    "best_bowling": {
      "enabled": True,
      "wickets": 2,
      "runs_conceded": 45
    },
    "purple_caps": 0
  })

  bowling_stats.award_purple_cap()
  expect(bowling_stats.purple_caps).to_equal(1)

  import json
  from backend.constants import bowling_model_sample_path
  json.dump(bowling_stats.to_dict(), open(bowling_model_sample_path, "w"), indent=2)
