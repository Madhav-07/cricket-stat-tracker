class batting_input:
  runs: int
  balls_faced: int
  fours: int
  sixes: int

  def __init__(self, runs: int = 0, balls_faced: int = 0, fours: int = 0, sixes: int = 0):
    self.runs = runs
    self.balls_faced = balls_faced
    self.fours = fours
    self.sixes = sixes

  def to_dict(self) -> dict:
    return {
      "runs": self.runs,
      "balls_faced": self.balls_faced,
      "fours": self.fours,
      "sixes": self.sixes
    }

class batting_model:
  innings: int
  runs: int
  balls_faced: int
  strike_rate: float
  fours: int
  sixes: int
  average_runs: float
  highest_score: int
  fifty: int
  century: int
  orange_caps: int

  # To initialize the batting model
  def __init__(self, **kwargs):
    # Set default values
    self.innings = 0
    self.runs = 0
    self.balls_faced = 0
    self.fours = 0
    self.sixes = 0
    self.strike_rate = None
    self.average_runs = None
    self.highest_score = 0
    self.fifty = 0
    self.century = 0
    self.orange_caps = 0

    # Override defaults with values from kwargs, if provided
    for key, value in kwargs.items():
      setattr(self, key, value)

  # To update the batting model with new data
  def update(self, batting_input: batting_input) -> None:
    self.innings += 1
    self.runs += batting_input.runs
    self.balls_faced += batting_input.balls_faced
    self.fours += batting_input.fours
    self.sixes += batting_input.sixes

    if batting_input.balls_faced > 0:
      self.strike_rate = round((self.runs / batting_input.balls_faced) * 100, 2)
      self.average_runs = round(self.runs / self.innings, 2)

    if batting_input.runs > self.highest_score:
      self.highest_score = batting_input.runs

    if batting_input.runs >= 50 and batting_input.runs < 100:
      self.fifty += 1
    elif batting_input.runs >= 100:
      self.century += 1

  # To award an orange cap to the player
  def award_orange_cap(self) -> None:
    self.orange_caps += 1
  
  # To serialize the batting model to a dictionary for JSON storage
  def to_dict(self) -> dict:
    return {
      "innings": self.innings,
      "runs": self.runs,
      "balls_faced": self.balls_faced,
      "fours": self.fours,
      "sixes": self.sixes,
      "strike_rate": self.strike_rate,
      "average_runs": self.average_runs,
      "highest_score": self.highest_score,
      "fifty": self.fifty,
      "century": self.century,
      "orange_caps": self.orange_caps
    }
  
  def getValues(self) -> list[str]:
    return [
      self.innings,
      self.runs,
      self.balls_faced,
      self.average_runs,
      self.strike_rate,
      self.highest_score,
      self.fours,
      self.sixes,
      self.fifty,
      self.century,
      self.orange_caps
    ]
  
batting_header_list = [
  "Innings",
  "Runs",
  "Balls Faced",
  "Average Runs",
  "Strike Rate",
  "Highest Score",
  "Fours",
  "Sixes",
  "Fifty",
  "Century",
  "Orange Caps"
]
  
if __name__ == "__main__":
  batting_data = batting_input()
  batting_data.runs = 50
  batting_data.balls_faced = 30
  batting_data.fours = 5
  batting_data.sixes = 2
  batting = batting_model()
  batting.update(batting_data)

  # New batting model values: {'innings': 1, 'runs': 50, 'balls_faced': 30, 'strike_rate': 166.67, 'fours': 5, 'sixes': 2, 'average_runs': 50.0, 'highest_score': 50, 'fifty': 1, 'century': 0, 'orange_caps': 0}
  from testing.test_utils import expect
  expect(batting.to_dict()).to_equal({'innings': 1, 'runs': 50, 'balls_faced': 30, 'strike_rate': 166.67, 'fours': 5, 'sixes': 2, 'average_runs': 50.0, 'highest_score': 50, 'fifty': 1, 'century': 0, 'orange_caps': 0})
  # Output: Test passed

  batting.award_orange_cap()
  expect(batting.orange_caps).to_equal(1)
  # Output: Test passed

  import json
  from backend.constants import batting_model_sample_path
  json.dump(batting.to_dict(), open(batting_model_sample_path, "w"), indent=2)
