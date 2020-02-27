import Node
from random import choice
import numpy as np
from numpy import chararray

class Tree:
    def __init__(self):
        self.root = Node()
        self.expandable_nodes = [] #To avoid going down the same path twice

    def select(self):
        exp_node = choice(self.expandable_nodes)
        return exp_node

    def expand(self, expandable_node):
        child = self.expand_child(expandable_node)
        expandable_node.children.append(child)
        return child


    def simulate(self, node):
        while not node.is_terminal():
            node = self.expand_child(node)
        return node


    def evaluate(self, node):
        self.check_winner(node)
        result = 1 #-1 loss,0 draw,1 win
        return result

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



    def get_random_path(self):
        nodes_copy = self.root.copy()
        #Get children all the way
        #When there is no child, create a new node unless it's terminal - then we need to select different path


    def expand_child(self, node):
        child_state = node.state
        empty_fields = np.where(child_state == b'')
        chosen_index = choice(range(len(empty_fields[0])))
        square = (empty_fields[0][chosen_index], empty_fields[1][chosen_index])
        child_turn = 'o' if node.turn == 'x' else 'x'
        child_state[square[0], square[1]] = child_turn
        child = Node(child_state, node.empty_squares - 1, child_turn)
        return child
