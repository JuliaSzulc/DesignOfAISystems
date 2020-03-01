class Node:

    def __init__(self, state, turn, coordinates=None):
        self.visits = 0
        self.reward = 0
        self.children = []
        self.state = state
        self.coordinates = coordinates
        self.empty_squares = (state == '').sum()
        self.turn = turn
        self.parent = None
        self.win = False

    def is_terminal(self):
        return self.is_leaf() or self.win

    def is_leaf(self):
        return self.empty_squares < 1

    def is_expandable(self):
        return len(self.children) < self.empty_squares and not self.is_terminal()
