from models.player_stats_record import player_stats_record
from file_store import file_store

class MainClass:
  file_content: player_stats_record

  def __init__(self):
    pass

  def run(self):
    print("Hello World")

if __name__ == "__main__":
  app = MainClass()
  app.run()
