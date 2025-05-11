from flask import Flask
from backend.service import service

service_instance = service()

app = Flask(__name__)

# Provide current year
@app.route('/year', methods=['GET'])
def get_current_year():
  return service_instance.current_year

# Increment current year
@app.route('/year', methods=['POST'])
def increment_year():
  service_instance.increment_year()
  return service_instance.cu

# Get default player stats list
@app.route('/player', methods=['GET']) 
def get_default_player_stats():
  return service_instance

# Get player stats by name
@app.route('/player/<name>', methods=['GET'])
def get_player_stats(name):
  pass

# Add or update player stats
@app.route('/player/<name>', methods=['POST'])
def add_or_update_player(name):
  pass

# 