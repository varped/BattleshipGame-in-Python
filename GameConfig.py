class GameConfig:

  def __init__(self):
    self.max_rows = 0
    self.max_cols = 0
    self.ship_count = 0
    self.dict_ship_type_to_length = {}

    self.player1_name = ""
    self.player2_name = ""
    self.filename = ""

  def readUserInput(self) -> None:
    """
    This function will ask for the file from the user and separate the parts of the file into the desired variables
    of rows, columns, ship type and ship length.
    :return: None
    """
    self.filename = input("Please enter the path to the configuration file for this game: ")
    with open(self.filename, 'r') as file:
      self.lines = file.readlines()
      self.max_rows = int(self.lines[0])
      self.max_cols = int(self.lines[1])
      self.ship_count = int(self.lines[2])
      for line in self.lines[3:]:
        parts = line.split()
        if len(parts) >= 2:
          ship_type = parts[0]
          ship_len = int(parts[1])
          self.dict_ship_type_to_length[ship_type] = ship_len

    file.close()

    self.player1_name = input("Player 1, please enter your name: ")
    self.player2_name = input("Player 2, please enter your name: ")