import os

file_store_path = os.path.join(".", "file-store")
player_records_path = os.path.join(file_store_path, "player-records")
team_records_path = os.path.join(file_store_path, "team-records")

models_path = os.path.join(".", "models")
bowling_model_sample_path = os.path.join(models_path, "bowling_model_sample.json")
batting_model_sample_path = os.path.join(models_path, "batting_model_sample.json")
player_model_sample_path = os.path.join(models_path, "player_model_sample.json")