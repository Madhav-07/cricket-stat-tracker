class expect:
  def __init__(self, actual_value):
    self.actual_value = actual_value

  def to_equal(self, expected_value):
    assert self.actual_value == expected_value, f"Expected {expected_value}\n\n, but got {self.actual_value}."
    print(f"Test passed.")