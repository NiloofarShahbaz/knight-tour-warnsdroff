KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


class KnightTour:
    def __init__(self, board_size):
        self.board_size = board_size  # tuple
        self.board = []
        for i in range(board_size[0]):
            temp = []
            for j in range(board_size[1]):
                temp.append(0)
            self.board.append(temp) # empty cell
        self.move = 1

    def print_board(self):
        print('board:')
        for i in range(self.board_size[0]):
            print(self.board[i])

    def warnsdroff(self, start_pos, GUI=False):
        x_pos,  y_pos = start_pos
        self.board[x_pos][y_pos] = self.move

        if not GUI:
            while self.move <= self.board_size[0] * self.board_size[1]:
                self.move += 1
                next_pos = self.find_next_pos((x_pos, y_pos))
                if next_pos:
                    x_pos, y_pos = next_pos
                    self.board[x_pos][y_pos] = self.move
                else:
                    self.print_board()
                    return self.board
        else:
            if self.move <= self.board_size[0] * self.board_size[1]:
                self.move += 1
                next_pos = self.find_next_pos((x_pos, y_pos))
                return next_pos

    def find_next_pos(self, current_pos):
        empty_neighbours = self.find_neighbours(current_pos)
        if len(empty_neighbours) is 0:
            return
        least_neighbour = 8
        least_neighbour_pos = ()
        for neighbour in empty_neighbours:
            neighbours_of_neighbour = self.find_neighbours(pos=neighbour)
            if len(neighbours_of_neighbour) <= least_neighbour:
                least_neighbour = len(neighbours_of_neighbour)
                least_neighbour_pos = neighbour
        return least_neighbour_pos

    def find_neighbours(self, pos):
        neighbours = []
        for dx, dy in KNIGHT_MOVES:
            x = pos[0] + dx
            y = pos[1] + dy
            if 0 <= x < self.board_size[0] and 0 <= y < self.board_size[1] and self.board[x][y] is 0:
                neighbours.append((x, y))
        return neighbours




a = KnightTour((8, 8))
a.warnsdroff((3, 3))
