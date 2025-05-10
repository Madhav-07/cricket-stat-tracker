import json

class file_store:
  def read_json(self, file_name: str) -> object:
    if not file_name:
      return None
    
    try:
      with open(file_name, 'r') as file:
        data = json.load(file)
      print(f"Data read from {file_name} successfully.")
      return data
    except FileNotFoundError:
      print(f"File {file_name} not found.")
    except json.JSONDecodeError:
      print(f"Error decoding JSON from file {file_name}.")

  def write_json(self, file_name: str, data: object) -> None:
    if not file_name or data is None:
        return
    
    try:
      with open(file_name, 'w') as file:
        json.dump(data.to_dict(), file, indent=2)
      print(f"Data written to {file_name} successfully.")
    except IOError:
      print(f"Error writing to file {file_name}.")