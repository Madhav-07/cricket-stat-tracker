from constants import year_path, player_records_path
from file_store import file_store
from models.player_model import player_input, player_model
from backend.models.player_stats_record_model import player_stats_record_model

class service:
  current_year: str
  player_stats_record: player_stats_record_model

  def __init__(self):
    self.get_player_stat_record()
    self.get_current_year()

  def get_player_stat_record(self):
    file_content = file_store.read_json(player_records_path)
    self.player_stats_record = player_stats_record_model(**file_content) if file_content else player_stats_record_model()

  def get_current_year(self) -> None:
    file_content = None
    with open(year_path, 'r') as file:
      file_content = file.read().strip()
    
    if not file_content:
      self.current_year = '1'
      with open(year_path, 'w') as file:
        file.write(self.current_year)
    else:
      self.current_year = file_content

  def increment_year(self) -> None:
    self.current_year = str(int(self.current_year) + 1)
    with open(year_path, 'w') as file:
      file.write(self.current_year)

  def get_default_player_stats(self) -> list[player_model]:
    pass

  def add_or_update_player(self, player_name: str, player_stats: player_input) -> None:
    self.player_stats_record.update(self.current_year, player_name, player_stats)

if __name__ == "__main__":
  service_instance = service()
  print(service_instance.current_year)