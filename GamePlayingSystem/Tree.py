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
        return self.create_child(expandable_node)

    def simulate(self, policy, node):
        while not node.is_terminal():


    def evaluate(self, whole_path):
        result = 1 #-1 loss,0 draw,1 win
        return result

    def get_random_path(self):
        nodes_copy = self.root.copy()
        #Get children all the way
        #When there is no child, create a new node unless it's terminal - then we need to select different path

    def create_child(self, node):
        child_state = node.state
        empty_fields = np.where(child_state== b'')
        chosen_index = choice(range(len(empty_fields[0])))
        square = (empty_fields[0][chosen_index], empty_fields[1][chosen_index])
        child_turn = 'o' if node.turn == 'x' else 'x'
        child_state[square[0], square[1]] = child_turn
        child = Node(child_state, node.empty_squares-1, child_turn)
        node.children.append(child)
        return child

