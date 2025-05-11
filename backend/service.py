from constants import year_path

class service:
  current_year: str

  def __init__(self):
    self.get_current_year()

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

if __name__ == "__main__":
  service_instance = service()
  print(service_instance.current_year)