from game.player import Player
from game.board import Board


class GameEngine:
    def __init__(self, rows, cols):
        self.board = Board(rows, cols)
        self.players = []
        self.n = None

    def setup_players(self):
        n = int(input("Enter the number of players: "))
        self.n = n
        for i in range(n):
            name = input(f"Enter name for Player {i + 1}: ")
            self.players.append(Player(name))

    def start(self):
        self.setup_players()
        self.board.render()
        idx = 0
        while not self.board.is_full():
            current_player = self.players[idx]
            print(f"\n{current_player.name}'s turn ({current_player.symbol})")
            if self.board.make_move(current_player):
                idx = (idx + 1) % self.n
            else:
                print("Can't draw there, Try again")
                self.board.render()
        self.end_game()

    def end_game(self):
        print("\nGame Over!")
        for player in self.players:
            print(f"{player.name} ({player.symbol}) scored: {player.score}")
