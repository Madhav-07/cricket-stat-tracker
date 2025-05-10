from models.batting_model import batting_input
from models.bowling_model import bowling_input, overs_model
from models.player_model import player_model, player_input

class player_stats_record:
  player_records: dict[str, dict[int, player_model]]

  def __init__(self, **kwargs):
    self.player_records = {}
    for name, player_iter_stats in kwargs.items():
      self.player_records[name] = {
        iter: player_model(**player) for iter, player in player_iter_stats.items()
      }

  def update(self, iter:int, player_name: str, player_stats: player_input) -> None:
    if player_name not in self.player_records:
      self.player_records[player_name] = {
        0: player_model(name=player_name),
        iter: player_model(name=player_name)
      }
    
    self.player_records[player_name][0].update(player_stats)
    self.player_records[player_name][iter].update(player_stats)

  def to_dict(self) -> dict:
    return {
      name: {
        iter: player.to_dict() for iter, player in player_record.items()
      } for name, player_record in self.player_records.items()
    }
  
if __name__ == "__main__":
  from testing.test_utils import expect
  player_stats = player_stats_record()
  expect(player_stats.to_dict()).to_equal({})

  player_inp = player_input(
    batting_stats=batting_input(runs=10, balls_faced=20, fours=2, sixes=1),
    bowling_stats=bowling_input(overs=overs_model(2,5), runs_conceded=30, wickets=1)
  )

  player_stats.update(1, "Player 1", player_inp)
  print(player_stats.to_dict())

  inp = {
    'Player 1': {
      0: {
        'name': 'Player 1', 
        'matches': 1, 
        'batting_stats': {
          'innings': 1, 
          'runs': 10, 
          'balls_faced': 20, 
          'fours': 2, 
          'sixes': 1, 
          'strike_rate': 50.0, 
          'average_runs': 10.0, 
          'highest_score': 10, 
          'fifty': 0, 
          'century': 0, 
          'orange_caps': 0
        }, 
        'bowling_stats': {
          'overs': {
            'complete_overs': 2, 
            'partial_overs': 5
          }, 
          'runs_conceded': 30, 
          'wickets': 1, 
          'bowler_average': 30.0, 
          'economy_rate': 10.59, 
          'best_bowling': {
            'enabled': True, 
            'wickets': 1, 
            'runs_conceded': 30
          }, 
          'purple_caps': 0
        }
      }, 
      1: {
        'name': 'Player 1', 
        'matches': 1, 
        'batting_stats': {
          'innings': 1, 
          'runs': 10, 
          'balls_faced': 20, 
          'fours': 2, 
          'sixes': 1, 
          'strike_rate': 50.0, 
          'average_runs': 10.0, 
          'highest_score': 10, 
          'fifty': 0, 
          'century': 0, 
          'orange_caps': 0
        }, 
        'bowling_stats': {
          'overs': {
            'complete_overs': 2, 
            'partial_overs': 5
          }, 
          'runs_conceded': 30, 
          'wickets': 1, 
          'bowler_average': 30.0, 
          'economy_rate': 10.59, 
          'best_bowling': {
            'enabled': True, 
            'wickets': 1, 
            'runs_conceded': 30
          }, 
          'purple_caps': 0
        }
      }
    }
  }
  new_player_stats = player_stats_record(**inp)
  expect(new_player_stats.to_dict()).to_equal(inp)

  from constants import player_stats_record_sample_path
  import json
  json.dump(new_player_stats.to_dict(), open(player_stats_record_sample_path, "w"), indent=2)