#The stack method takes in nodes(individual object) in the stack
#the atrributes of the class is the top node and the numbers of nodes in the class
#it use the pop/peek/push methods to regulate the stack
#the pop method deletes the first node in the stack
#the peek method returns the first node in the stack
#the push method adds one node to the top of the nodes

class SNode:
    def __init__(self, data):
        self.data= data
        self.next_node = None
        
    def __repr__(self):
        return self.data.__repr__()


class Stack:

    def __init__(self):
        # The first Node object in the list
        self.top_node = None
        self.num_of_nodes = 0

    def size(self):
        return self.num_of_nodes

    def get_middle(self):
        temp_node = self.top_node
        i = 0
        while i < self.num_of_nodes // 2:
            temp_node = temp_node.next_node
            i += 1
        return temp_node

    def pop(self):
        if self.top_node is None:
            return None
        else:
            deleted_node = self.top_node
            self.top_node = self.top_node.next_node
            deleted_node.next_node=None
            #del deleted_node
            self.num_of_nodes -= 1
            return deleted_node


    def peek(self, spot):
        item = self.top_node
        for i in range(spot):
            item = item.next_node
        return item

    def push(self, data):
        self.num_of_nodes += 1
        new_node = SNode(data)
        if self.top_node is None:  # if the list is empty
            self.top_node = new_node
        else:
            # update the references to keep the order
            new_node.next_node = self.top_node
            self.top_node = new_node


    def traverse(self, node):
        print(node)
        if node.next_node is not None:
            self.traverse(node.next_node)

    def __repr__(self):
        if self.top_node is None:
            return "The stack is empty!"
        else:
            output = f"The stack has {self.size()} cards.\n"
            current_node = self.top_node
            while current_node is not None:
                output += current_node.__repr__() + "\n"
                current_node = current_node.next_node
            return output