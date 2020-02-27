class Node:

    def __init__(self, state, empty_squares, turn):
        self.visits=0
        self.reward=0
        self.children = []
        self.state = state
        self.empty_squares = empty_squares
        self.turn = turn
        self.parent = None

    def is_terminal(self):
        return (self.empty_squares < 1)#||win

    def create_child(self):
        #Add child to child list
        child = Node()
        return child

