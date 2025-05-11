from flask import Flask
from models.player_stats_record import player_stats_record

app = Flask(__name__)

# Provide 
@app.route('/year', methods=['GET'])
def handle_default_endpoint():
  return {
    "Year": 2023,
  }
