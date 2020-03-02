import numpy as np


class Node:
    def __init__(self, grid, symbol, coordinates=None):
        self.visits = 0
        self.reward = 0
        self.children = []
        self.grid = grid
        self.coordinates = coordinates
        self.empty_squares = (grid == '').sum()
        self.symbol = symbol
        self.parent = None
        self.win = False

    def is_terminal(self):
        return self.is_leaf() or self.win

    def is_leaf(self):
        return self.empty_squares < 1

    def is_expandable(self):
        return len(self.children) < self.empty_squares and not self.is_terminal()

    def get_empty_fields(self):
        empty_indexes = np.where(self.grid == '')
        empty_fields = list(zip(empty_indexes[0], empty_indexes[1]))

        return empty_fields

    def __eq__(self, other):
        return np.array_equal(self.grid, other.grid)\
               and self.symbol == other.symbol
