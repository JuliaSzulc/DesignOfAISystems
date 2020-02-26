class Tree:
    root = Node()
    expandable_nodes = [] #To avoid going down the same path twice

    def select(self):
        new_node = Node()
        return new_node

    def expand(self, new_node):
        pass

    def simulate(self, policy):
        pass

    def evaluate(self, whole_path):
        result = 1 #-1 loss,0 draw,1 win
        return result

    def get_random_path(self):
        nodes_copy = self.root.copy()
        #Get children all the way
        #When there is no child, create a new node unless it's terminal - then we need to select different path

