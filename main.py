class TicTacToe(object):
    data = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    crosses = 'x'
    zeros = '0'

    def restart(self):
        self.data = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def is_empty(self):
        for row in self.data:
            for cell in row:
                if cell != '':
                    return False
        return True

    def is_play(self):
        return not self.is_empty()

    def row_check(self, sim):
        for row in self.data:
            count = 0
            for cell in row:
                if cell == sim:
                    count += 1
            if count == 3:
                return True
        return False

    def colum_check(self, sim):
        for i in range(3):
            count = 0
            for row in self.data:
                if row[i] == sim:
                    count += 1
            if count == 3:
                return True
        return False

    def cross_check(self, sim):
        data = self.data
        if data[0][0] == sim and data[1][1] == sim and data[2][2] == sim:
            return True
        elif data[0][2] == sim and data[1][1] == sim and data[2][0] == sim:
            return True
        else:
            return False

    def get_image(self):
        return """
        {},\t{},\t{}
        {},\t{},\t{}
        {},\t{},\t{}
        """.format(*self.data[0], *self.data[1], *self.data[2])

    def check_win(self, sim):
        return self.colum_check(sim) or self.row_check(sim) or self.cross_check(sim)

    def game_is_finish(self):
        return self.check_win(self.crosses) or self.check_win(self.zeros) or self.is_cell_full()

    def is_cell_full(self):
        for row in self.data:
            for cell in row:
                if cell == '':
                    return False
        return True

    def set_cell(self, a, b, sem):
        if self.data[b][a] != '':
            print("cell is not empty")
        self.data[b][a] = sem
        print(self.get_image())
        if self.game_is_finish():
            self.who_is_win()

    def set_zero(self, a, b):
        self.set_cell(a, b, self.zeros)

    def set_cross(self, a, b):
        self.set_cell(a, b, self.crosses)

    def who_is_win(self):
        if self.is_play():
            if self.check_win(self.crosses):
                print("Crosses win and game")
            elif self.check_win(self.zeros):
                print("Zeros win and game")
            else:
                print("Game both of them not win")
        print('Game not started')


tic_tac_toe = TicTacToe()
print(tic_tac_toe.is_play())
print(tic_tac_toe.is_empty())

tic_tac_toe.set_cross(1, 1)

print(tic_tac_toe.is_play())
print(tic_tac_toe.is_empty())

tic_tac_toe.set_zero(2, 0)
tic_tac_toe.set_zero(2, 1)
tic_tac_toe.set_zero(2, 2)
