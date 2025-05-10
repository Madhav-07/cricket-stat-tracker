from models.batting_model import batting_model, batting_input
from models.bowling_model import bowling_model, bowling_input

class player_input:
  batting_stats: batting_input
  bowling_stats: bowling_input

  def __init__(self, batting_stats: batting_input = None, bowling_stats: bowling_input = None):
    self.batting_stats = batting_stats
    self.bowling_stats = bowling_stats

class player_model:
  name: str
  matches: int
  batting_stats: batting_model
  bowling_stats: bowling_model

  def __init__(self, **kwargs):
    if "name" not in kwargs:
      raise ValueError("Player name is required")
    
    self.name = kwargs.get("name", '')
    self.matches = kwargs.get("matches", 0)
    self.batting_stats = batting_model(**kwargs.get("batting_stats", {})) 
    self.bowling_stats = bowling_model(**kwargs.get("bowling_stats", {}))

  def update(self, player_input: player_input) -> None:
    self.matches += 1
    if player_input.batting_stats:
      self.batting_stats.update(player_input.batting_stats)
    if player_input.bowling_stats:
      self.bowling_stats.update(player_input.bowling_stats)

  def to_dict(self) -> dict:
    return {
      "name": self.name,
      "matches": self.matches,
      "batting_stats": self.batting_stats.to_dict(),
      "bowling_stats": self.bowling_stats.to_dict()
    }

  def getValues(self) -> list[str]:
    return [
      self.name,
      str(self.matches)
    ]

player_header_list = [
  "Name",
  "Matches"
]

if __name__ == "__main__":
  from testing.test_utils import expect

  try:
    player1 = player_model()
  except ValueError as e:
    expect(str(e)).to_equal("Player name is required")
  
  player2 = player_model(name="Player 2")
  expect(player2.to_dict()).to_equal({
    "name": "Player 2",
    "matches": 0,
    "batting_stats": {
      "innings": 0,
      "runs": 0,
      "balls_faced": 0,
      "fours": 0,
      "sixes": 0,
      "strike_rate": None,
      "average_runs": None,
      "highest_score": 0,
      "fifty": 0,
      "century": 0,
      "orange_caps": 0
    },
    "bowling_stats": {
      "overs": {
        "complete_overs": 0,
        "partial_overs": 0
      },
      "runs_conceded": 0,
      "wickets": 0,
      "bowler_average": None,
      "economy_rate": None,
      "best_bowling": {
        "enabled": False,
        "wickets": 0,
        "runs_conceded": 0
      },
      "purple_caps": 0
    }
  })

  import json
  from backend.constants import player_model_sample_path
  json.dump(player2.to_dict(), open(player_model_sample_path, "w"), indent=2)
