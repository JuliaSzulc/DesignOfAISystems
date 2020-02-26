class Node:
    N=0
    Q=0
    children = []
    state = []
    empty_squares = 0

    def is_terminal(self):
        return (self.empty_squares < 1)#||win

    def create_child(self):
        #Add child to child list
        child = Node()
        return child

