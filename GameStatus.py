class GameStatus:

    def __init__(self):
        player1won = ''
        player2won = ''

    def isGameOver(self, player1PlacementBoard: dict, player2PlacementBoard: dict, player1FiringBoard: dict, player2FiringBoard: dict, gameConfig) -> bool:
        """
        This function checks whether there are any remaining ships on the board in order to check if the game is over.
        If a player won, the function will announce which player won.
        :param player1PlacementBoard: dict
        :param player2PlacementBoard: dict
        :param player1FiringBoard: dict
        :param player2FiringBoard: dict
        :param gameConfig: class
        :return: bool
        """
        player1won = True
        player2won = True

        for i in range(gameConfig.max_rows):
            for j in range(gameConfig.max_cols):
                if player2PlacementBoard.dict_placement_board[i, j] not in "*XO":  # Ship exists
                    player1won = False
                    break
            if not player1won:
                break

        for i in range(gameConfig.max_rows):
            for j in range(gameConfig.max_cols):
                if player1PlacementBoard.dict_placement_board[i, j] not in "*XO":  # Ship exists
                    player2won = False
                    break
            if not player2won:
                break

        if player1won:
            print(f'{gameConfig.player1_name}\'s Firing Board')
            player1FiringBoard.showBoard(gameConfig)
            print(f'{gameConfig.player1_name}\'s Placement Board')
            player1PlacementBoard.showBoard(gameConfig)
            print(gameConfig.player1_name + " won!")
            return True

        if player2won:
            print(f'{gameConfig.player2_name}\'s Firing Board')
            player2FiringBoard.showBoard(gameConfig)
            print(f'{gameConfig.player2_name}\'s Placement Board')
            player2PlacementBoard.showBoard(gameConfig)
            print(gameConfig.player2_name + " won!")
            return True

        return False
