from Node import *
from random import choice
import numpy as np


class Tree:
    def __init__(self, symbol, grid, simulation_steps=2):
        self.root = Node(grid, symbol, None)  # empty_squares, turn
        self.expandable_nodes = [self.root]  # To avoid going down the same path twice
        self.symbol = symbol
        self.simulation_steps = simulation_steps
        self.current_node = self.root

    def select(self):
        if not self.expandable_nodes:
            return None

        exp_node = choice(self.expandable_nodes)
        return exp_node

    def expand(self, expandable_node):
        child = self.expand_child(expandable_node)
        child.parent = expandable_node
        expandable_node.children.append(child)
        if self.check_winner(child.state):
            child.win = True

        return child

    def simulate(self, node):
        simulated_node = node
        while not simulated_node.is_terminal():
            simulated_node = self.expand_child(simulated_node)
        return simulated_node

    def evaluate(self, node):
        winner = self.check_winner(node.state)
        if winner == self.symbol:
            return 1
        if not winner:
            return 0
        return -1

    def backpropagate(self, simulated_node, node):
        result = self.evaluate(simulated_node)
        node.visits += 1
        node.reward += result
        while node.parent:
            node = node.parent
            node.visits += 1
            node.reward += result

    def update_tree(self, exp_node, child):
        if not exp_node.is_expandable():
            self.expandable_nodes.remove(exp_node)
        if not child.is_terminal():
            self.expandable_nodes.append(child)

    def check_winner(self, state):
        for i in range(state.shape[1]):
            char = state[0][i]
            if all(state[j][i] == char for j in range(1, state.shape[0])):
                return char

        for j in range(state.shape[0]):
            char = state[j][0]
            if all(state[j][i] == char for i in range(1, state.shape[1])):
                return char

        char = state[0][0]
        if all(state[i][i] == char for i in range(1, state.shape[0])):
            return char

        char = state[0][-1]
        if all(state[i][-1 - i] == char for i in range(1, state.shape[0])):
            return char
        return None

    def expand_child(self, node):
        child_state = np.copy(node.state)
        empty_fields = np.where(child_state == '')
        chosen_index = choice(range(len(empty_fields[0])))
        coordinates = (empty_fields[0][chosen_index], empty_fields[1][chosen_index])
        symbol = 'o' if node.turn == 'x' else 'x'
        child_state[coordinates[0], coordinates[1]] = symbol
        child = Node(child_state, symbol, coordinates)
        return child

    def make_move(self):
        node = max(self.current_node.children, key=lambda n: n.reward)
        return node

    # def run(self):
    #     parent = self.select()
    #     if not parent:
    #         return False
    #     child = self.expand(parent)
    #     simulated_node = self.simulate(child)
    #     self.backpropagate(simulated_node, child)
    #     self.update_tree(parent, child)
    #
    #     return True

    def run(self, state, symbol):
        self.current_node = Node(state, symbol, None)
        self.expandable_nodes = [self.current_node]
        for _ in range(self.simulation_steps):
            new_exp_nodes = []
            while self.expandable_nodes:
                parent = self.select()
                for child_index in range(parent.empty_squares):
                    child = self.expand(parent)
                    simulated_node = self.simulate(child)
                    self.backpropagate(simulated_node, child)
                    if not child.is_terminal():
                        new_exp_nodes.append(child)

                self.expandable_nodes.remove(parent)
            self.expandable_nodes = new_exp_nodes

        chosen = self.make_move()
        return chosen.coordinates
