class PlacementBoard:

  def __init__(self,gameConfig) -> dict:
    """
    This function creates the Placement Board.
    :param gameConfig: class
    return: dict
    """
    self.dict_placement_board = {}
    self.ship_type = ""
    for i in range(gameConfig.max_rows):
        for j in range(gameConfig.max_cols):
            self.dict_placement_board[i,j] = "*" #Init squares with Blank

  def showBoard(self,gameConfig) -> dict:
    """
    This function displays the placement boards to the players.
    :param gameConfig: class
    :return: dict
    """
    col_heading = " "
    for i in range(gameConfig.max_cols):
        col_heading += str(i)
    print(col_heading)
    for row in range(gameConfig.max_rows):
        row_str = ""
        for col in range(gameConfig.max_cols):
            row_str += self.dict_placement_board[row,col]
        row_str = str(row)+ row_str
        print(row_str)

  def getInputForPlacingShips(self, player_name: str, gameConfig) -> dict:
      """
      This function asks each player where they want to place their ships and will place their ships on the placement boards.
      :param player_name: str
      :param gameConfig: class
      :return: dict
      """
      self.player_name = player_name
      print(f'{player_name}\'s Placement Board')
      self.showBoard(gameConfig)

      sorted_keys = sorted(gameConfig.dict_ship_type_to_length.keys())

      for key in sorted_keys:
          ship_type = key
          ship_len = gameConfig.dict_ship_type_to_length[key]
          placed = False

          while not placed:
              AskforOrientation = input(f'{player_name}, enter the orientation of your {ship_type}, which is {ship_len} long: ').lower().strip()

              if AskforOrientation in ['h', 'ho', 'hor', 'hori', 'horiz', 'horizo', 'horizon', 'horizont', 'horizonta', 'horizontal', 'horizontall', 'horizontally']:
                  direction = 0
              elif AskforOrientation in ['v', 've', 'ver', 'vert', 'verti', 'vertic', 'vertica', 'vertical', 'verticall', 'vertically']:
                  direction = 1
              else:
                  continue

              AskforLocation = input(f'Enter the starting location for your {ship_type}, which is {ship_len} long, in the form row col: ').strip()

              locationsplit = AskforLocation.split()
              if len(locationsplit) >= 2:
                  loc_row = int(locationsplit[0])
                  loc_col = int(locationsplit[1])
                  if (0 <= loc_row < gameConfig.max_rows) and (0 <= loc_col < gameConfig.max_cols):
                      if (direction == 0 and (loc_col + ship_len <= gameConfig.max_cols)) or \
                              (direction == 1 and (loc_row + ship_len <= gameConfig.max_rows)):
                          placed = self.placeShip(ship_type, loc_row, loc_col, direction, gameConfig)

          if placed:
              print(f'{player_name}\'s Placement Board')
              self.showBoard(gameConfig)

  def placeShip(self, ship_type_char: str, row: int, col: int, direction: str, gameConfig) -> bool:
    """
    This function will use the user's input and checks whether the ships can be placed on the desired locations.
    :param ship_type_char: str
    :param row: int
    :param col: int
    :param direction: str
    :param gameConfig:
    :return: bool
    """
    ship_len = gameConfig.dict_ship_type_to_length[ship_type_char]

    #Horizontal
    if(direction == 0):
        temp_col = col
        if((temp_col+ship_len) <= gameConfig.max_cols): #ship length fits here
            for i in range(ship_len):
                if(self.dict_placement_board[row,temp_col] != "*"): #Gameboard square is empty
                    return False
                temp_col += 1
        else:
            return False

        temp_col = col
        for i in range(ship_len):
            self.dict_placement_board[row,temp_col] = str(ship_type_char) #Update Ship Squares
            temp_col += 1
        return True

    #Vertical
    else:
        temp_row = row
        if((temp_row+ship_len) <= gameConfig.max_rows):
            for i in range(ship_len):
                if(self.dict_placement_board[temp_row,col] != "*"):
                    return False
                temp_row += 1
        else:
            return False

        temp_row = row
        for i in range(ship_len):
            self.dict_placement_board[temp_row,col] = str(ship_type_char) #Update Ship Squares
            temp_row += 1
        return True