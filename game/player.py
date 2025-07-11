class Player:
    def __init__(self, name, symbol=None):
        self.score = 0
        self.name = name
        self.symbol = symbol if symbol else name[0].upper()

    def increment_score(self):
        self.score += 1
        return self.score
