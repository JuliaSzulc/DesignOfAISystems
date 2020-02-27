import Node
from random import choice
import numpy as np
from numpy import chararray

class Tree:
    def __init__(self, symbol):
        self.root = Node()
        self.expandable_nodes = [] #To avoid going down the same path twice
        self.symbol = symbol

    def select(self):
        exp_node = choice(self.expandable_nodes)
        return exp_node

    def expand(self, expandable_node):
        child = self.expand_child(expandable_node)
        child.parent = expandable_node
        expandable_node.children.append(child)
        return child


    def simulate(self, node):
        while not node.is_terminal():
            node = self.expand_child(node)
        return node


    def evaluate(self, node):
        node.visits += 1
        winner = self.check_winner(node)
        if winner == self.symbol:
            return 1
        if not winner:
            return 0
        return -1


    def backpropagate(self, node):
        result = self.evaluate(node)
        node.visits += 1
        node.reward += result
        while node.parent:
            node = node.parent
            node.visits += 1
            node.reward += result



    def check_winner(self, node):
        state = node.state
        for i in range(state.shape[1]):
            char = state[0][i]
            if all(state[j][i]==char for j in range(1,state.shape[0])):
                return char

        for j in range(state.shape[0]):
            char = state[j][0]
            if all(state[j][i] == char for i in range(1, state.shape[1])):
                return char

            char = state[0][0]
            if all(state[i][i] == char for i in range(1, state.shape[0])):
                return char

            char = state[0][-1]
            if all(state[i][-i] == char for i in range(1, state.shape[0])):
                return char
        return None


    def expand_child(self, node):
        child_state = node.state
        empty_fields = np.where(child_state == b'')
        chosen_index = choice(range(len(empty_fields[0])))
        square = (empty_fields[0][chosen_index], empty_fields[1][chosen_index])
        child_turn = 'o' if node.turn == 'x' else 'x'
        child_state[square[0], square[1]] = child_turn
        child = Node(child_state, node.empty_squares - 1, child_turn)
        return child
