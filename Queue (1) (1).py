#the Queue class takes in a node(objects) and regulates in a Queue
#the attribute of the class is the headnote and the number of nodes in the queue
#the class mainly has two methods
  #the enqueue method adds a node to the back of the queue
  #the dequeue method deletes a node from the beggining of the queue
#the Queue class takes in a node(objects) and regulates in a Queue
#the attribute of the class is the headnote and the number of nodes in the queue
#the class mainly has two methods
  #the enqueue method adds a node to the back of the queue
  #the dequeue method deletes a node from the beggining of the queue
class QNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
    def __repr__(self):
        return self.data.__repr__()
        
class Queue:
    def __init__(self):
        self.head_node = None
        self.rear_node = None
        self.num_of_nodes = 0
    
    def size(self):
        return self.num_of_nodes

    def is_empty(self):
        return self.num_of_nodes == 0

    def enqueue(self, data):
        new_node = QNode(data)
        self.num_of_nodes +=1
        if self.head_node is None:
            self.head_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next_node = new_node
            self.rear_node = new_node

    def dequeue(self):
        if self.head_node is None:
            return None
        else:
            deleted_node = self.head_node
            self.head_node = self.head_node.next_node
            deleted_node.next_node = None
            self.num_of_nodes -= 1
            return deleted_node

    def print_queue(self):
        if self.head_node is None:
            print("The queue is empty!")
        else:
            temp_node = self.head_node
            while temp_node is not None:
                print(temp_node.data)
                temp_node = temp_node.next_node

    def __repr__(self):
        if self.head_node is None:
            return "The queue is empty!"
        else:
            output = f"The queue has {self.size()} cards.\n"
            temp_node = self.head_node
            while temp_node is not None:
                output += temp_node.__repr__() + "\n"
                temp_node = temp_node.next_node