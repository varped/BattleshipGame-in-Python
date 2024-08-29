class FiringBoard:

  def __init__(self,gameConfig) -> dict:
    """
    This function creates the Firing Board.
    :param gameConfig: class
    return: dict
    """
    self.dict_firing_board = {}
    for i in range(gameConfig.max_rows):
        for j in range(gameConfig.max_cols):
            self.dict_firing_board[i,j] = "*"

  def showBoard(self,gameConfig) -> dict:
    """
    This function displays the Firing Board for each player.
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
            row_str += self.dict_firing_board[row,col]
        row_str = str(row)+row_str
        print(row_str)

  def fireOnShip(self, row: int, col: int, player_name: str, oppo_name: str, opponentPlacementBoard: dict, gameConfig) -> bool:
    """
    This function will check if the input for firing is valid and output to the player that they either hit a ship or missed.
    :param row: int
    :param col: int
    :param player_name: str
    :param oppo_name: str
    :param opponentPlacementBoard: dict
    :param gameConfig: class
    :return: bool
    """
    if(self.dict_firing_board[row,col] != "*"):
        return False

    if(opponentPlacementBoard.dict_placement_board[row,col] not in "*OX"):
        print(f'{player_name} hit {oppo_name}\'s {opponentPlacementBoard.dict_placement_board[row,col]}!')
        ship_type_hit = opponentPlacementBoard.dict_placement_board[row,col]

        opponentPlacementBoard.dict_placement_board[row,col] = "X"
        self.dict_firing_board[row,col] = "X"

        last_hit_on_ship = True
        for i in range(gameConfig.max_rows):
            for j in range(gameConfig.max_cols):
                if opponentPlacementBoard.dict_placement_board[i,j] == ship_type_hit:
                    last_hit_on_ship = False
                    break

        if last_hit_on_ship == True:
            print(f'{player_name} destroyed {oppo_name}\'s {ship_type_hit}!')

        return True
    else:
        print(f'{player_name} missed.')
        opponentPlacementBoard.dict_placement_board[row,col] = "O"
        self.dict_firing_board[row,col] = "O"
        return True

    return True