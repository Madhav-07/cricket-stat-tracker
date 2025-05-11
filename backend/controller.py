from flask import Flask, Blueprint, jsonify
from service import service

service_instance = service()

api = Blueprint('api', __name__, url_prefix='/api')

# Provide current year
@api.route('/year', methods=['GET'])
def get_current_year():
  return jsonify({"current_year": service_instance.current_year})

# Increment current year
@api.route('/year', methods=['POST'])
def increment_year():
  service_instance.increment_year()
  return jsonify({"current_year": service_instance.current_year})

# Get default player stats list
@api.route('/player', methods=['GET']) 
def get_default_player_stats():
  return service_instance

# Get player stats by name
@api.route('/player/<name>', methods=['GET'])
def get_player_stats(name):
  pass

# Add or update player stats
@api.route('/player/<name>', methods=['POST'])
def add_or_update_player(name):
  pass

app = Flask(__name__)
app.register_blueprint(api)