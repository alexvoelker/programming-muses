class Binary_Tree:
    """ Not Sure if I coded this properly, but it's a start"""
    def __init__(self, input_value: int):
        self.value = input_value
        self.node_count = 1
        self.left = None
        self.right = None

    def add_node(self, input_value: int):
        if input_value > self.value:
            if self.right == None:
                self.right = Binary_Tree(input_value)
            else:
                self.right.add_node(input_value)
        elif input_value <= self.value:
            if self.left == None:
                self.left = Binary_Tree(input_value)
            else:
                self.left.add_node(self.value)
            self.value = input_value  

        self.node_count += 1


    def remove_node(self):
        if self.left == None and self.right == None:
            self.value = None
        elif self.left != None:
            self.left.remove_node()
        elif self.right != None:
            self.right.remove_node()

    def get_node_count(self):
        return self.node_count
            
    def __reverse_children(self):
        self.left, self.right = self.right, self.left

    def reverse(self):
        self.__reverse_children()

        if self.left != None:
            self.left.reverse()
        if self.right != None:
            self.right.reverse()

    def print_tree(self):
        print(str(self.value) + ": {L: ", end="")
        if self.left != None:
            self.left.print_tree()
        print("} {R: ", end="")
        if self.right != None:
            self.right.print_tree()
        print("}", end="")
