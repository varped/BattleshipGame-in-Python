import GameConfig
import PlacementBoard
import FiringBoard
import GameStatus
def main():
    # Initialize the game configuration
    gameConfig = GameConfig.GameConfig()
    gameConfig.readUserInput()

    # Initialize the game boards
    player1PlacementBoard = PlacementBoard(gameConfig)
    player2PlacementBoard = PlacementBoard(gameConfig)

    player1FiringBoard = FiringBoard(gameConfig)
    player2FiringBoard = FiringBoard(gameConfig)

    # Players place their ships
    player1PlacementBoard.getInputForPlacingShips(gameConfig.player1_name, gameConfig)
    player2PlacementBoard.getInputForPlacingShips(gameConfig.player2_name, gameConfig)

    # Initialize the game status
    gameStatus = GameStatus.GameStatus()

    # Game loop
    game_over = False
    while not game_over:
        # Player 1 fires
        print(f"{gameConfig.player1_name}'s turn to fire!")
        row = int(input("Enter row to fire: "))
        col = int(input("Enter column to fire: "))
        if player1FiringBoard.fireOnShip(row, col, gameConfig.player1_name, gameConfig.player2_name, player2PlacementBoard, gameConfig):
            game_over = gameStatus.isGameOver(player1PlacementBoard, player2PlacementBoard, player1FiringBoard, player2FiringBoard, gameConfig)

        if game_over:
            break

        # Player 2 fires
        print(f"{gameConfig.player2_name}'s turn to fire!")
        row = int(input("Enter row to fire: "))
        col = int(input("Enter column to fire: "))
        if player2FiringBoard.fireOnShip(row, col, gameConfig.player2_name, gameConfig.player1_name, player1PlacementBoard, gameConfig):
            game_over = gameStatus.isGameOver(player1PlacementBoard, player2PlacementBoard, player1FiringBoard, player2FiringBoard, gameConfig)

if __name__ == "__main__":
    main()