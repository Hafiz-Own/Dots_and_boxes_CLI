from game.game_engine import GameEngine

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    game = GameEngine(rows, columns)
    game.start()
