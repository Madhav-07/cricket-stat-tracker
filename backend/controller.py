from flask import Flask
from backend.models.player_stats_record_model import player_stats_record

app = Flask(__name__)

# Provide 
@app.route('/year', methods=['GET'])
def handle_default_endpoint():
  return {
    "Year": 2023,
  }
