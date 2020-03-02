class User:
    def __init__(self, symbol, name='You'):
        self.symbol = symbol
        self.name = name

    def make_move(self, grid):
        user_input = input(
            "Write coordinates (0-{}) separated with space\n".format(
                grid.shape[0] - 1))
        user_input = [int(i) for i in user_input.split()]
        user_coordinates = (user_input[0], user_input[1])

        return user_coordinates

    def reset(self):
        pass
