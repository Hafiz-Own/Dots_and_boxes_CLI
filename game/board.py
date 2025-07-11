from game.player import Player


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.h_lines = [[False for _ in range(cols - 1)] for _ in range(rows)]
        self.v_lines = [[False for _ in range(cols)] for _ in range(rows - 1)]
        self.boxes = [[None for _ in range(cols - 1)] for _ in range(rows - 1)]

    def draw_horizontal(self, row: int, col: int, player: Player):
        """User gave coordinates like they are on the same row, so we got to draw a horizontal line for them"""
        if self.h_lines[row][col]:
            return False
        self.h_lines[row][col] = True
        return True

    def draw_vertical(self, row: int, col: int, player: Player):
        if self.v_lines[row][col]:
            return False
        self.v_lines[row][col] = True
        return True

    def make_move(self, player):
        direction = input("Enter Direction (H / V) : ").upper().strip()
        if direction in ['H', 'V']:
            r = int(input("Row : "))
            c = int(input("Col : "))
            if r > len(self.h_lines) - 1 or c > len(self.v_lines) - 1 or r < 0 or c < 0:
                return False
            if direction == 'H':
                if self.draw_horizontal(r, c, player):
                    if self.check_boxes(player) and not self.is_full():
                        print("You got the box, Go again!")
                        self.render()
                        self.make_move(player)
                    else:
                        self.render()
                else:
                    return False
            else:
                if self.draw_vertical(r, c, player):
                    if self.check_boxes(player) and not self.is_full():
                        print("You got the box, Go again!")
                        self.render()
                        self.make_move(player)
                    else:
                        self.render()
                else:
                    return False
        else:
            print("Please Enter the Right direction")
            self.make_move(player)
        return True

    def is_full(self):
        for row in self.boxes:
            for col in row:
                if col is None:
                    return False
        return True

    def check_boxes(self, player: Player):
        box_made = False
        for r in range(self.rows - 1):
            for c in range(self.cols - 1):
                if not self.boxes[r][c] and self.h_lines[r][c] and self.v_lines[r][c] and self.h_lines[r + 1][c] and \
                        self.v_lines[r][c + 1]:
                    """Box just got occupied"""
                    self.boxes[r][c] = player.symbol
                    player.score += 1
                    box_made = True
        return box_made

    def render(self):
        line = ''
        # Top line
        for row in range(1):
            for col in range(self.cols - 1):
                line += '*'
                line += '-----' if self.h_lines[row][col] else '     '
            line += '*'
            print(line)
        for row in range(1, self.rows):
            # Vertical Lines
            line = ''
            for col in range(self.cols - 1):
                line += '|' if self.v_lines[row - 1][col] else ' '
                line += '     ' if not self.boxes[row - 1][col] else '  ' + str(self.boxes[row - 1][col]) + '  '
            line += '|' if self.v_lines[row - 1][self.cols - 1] else ' '
            print(line)
            # Bottom
            line = ''
            for col in range(self.cols - 1):
                line += '*'
                line += '-----' if self.h_lines[row][col] else '     '
            line += '*'
            print(line)
