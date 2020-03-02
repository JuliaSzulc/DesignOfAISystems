from Node import *
from Utils import check_winner

from random import choice
import numpy as np
from math import log, sqrt


class MCTreeSearch:
    def __init__(self, symbol, grid,
                 simulation_steps=2,
                 name='AI',
                 strategy='reward'):
        self.symbol = symbol

        opponent_symbol = 'x' if self.symbol == 'o' else 'o'
        self.root = Node(np.copy(grid), opponent_symbol, None)
        self.current_node = self.root
        self.tree = [self.root]
        self.expandable_nodes = []

        self.simulation_steps = simulation_steps
        self.name = name

        strategies = {
            'reward': lambda n: n.reward,
            'uct': lambda n: n.reward / n.visits + sqrt(log(self.root.visits) / n.visits)
        }
        self.strategy = strategies[strategy]

    def select(self):
        exp_node = choice(self.expandable_nodes)
        return exp_node

    def expand(self, expandable_node, possible_coordinates):
        child = self.expand_child(expandable_node, possible_coordinates)
        child.parent = expandable_node
        expandable_node.children.append(child)
        if check_winner(child.grid):
            child.win = True

        return child

    def simulate(self, node):
        simulated_node = node
        while not simulated_node.is_terminal():
            random_coordinates = choice(simulated_node.get_empty_fields())
            simulated_node = self.expand_child(simulated_node, random_coordinates)
        return simulated_node

    def evaluate(self, node):
        winner = check_winner(node.grid)
        if winner == self.symbol:
            return 1
        if not winner:
            return 0
        return -1

    def backpropagate(self, simulated_node, node):
        result = self.evaluate(simulated_node)
        self.update(node, result)

    def update(self, node, result):
        node.visits += 1
        node.reward += result

        if node.parent:
            self.update(node.parent, result)

    def expand_child(self, node, coordinates):
        child_grid = np.copy(node.grid)
        symbol = 'o' if node.symbol == 'x' else 'x'
        child_grid[coordinates[0], coordinates[1]] = symbol
        child = Node(child_grid, symbol, coordinates)
        return child

    def make_move(self, grid):
        if not self.current_node:
            self.current_node = Node(grid, self.root.symbol, None)

        self.expandable_nodes = [self.current_node]
        for _ in range(self.simulation_steps):
            new_exp_nodes = []
            while self.expandable_nodes:
                parent = self.select()
                for possible_coordinates in parent.get_empty_fields():
                    child = self.expand(parent, possible_coordinates)
                    simulated_node = self.simulate(child)
                    self.backpropagate(simulated_node, child)
                    if not child.is_terminal():
                        new_exp_nodes.append(child)
                    if all(not node == child for node in self.tree):
                        self.tree.append(child)

                self.expandable_nodes.remove(parent)
            self.expandable_nodes = new_exp_nodes

        chosen = max(self.current_node.children, key=self.strategy)
        self.current_node = None
        return chosen.coordinates

    def reset(self):
        self.current_node = self.root
