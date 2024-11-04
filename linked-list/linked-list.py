# Linked List Code Example by NeuralNine on YouTube
# https://www.youtube.com/watch?v=1iz9SRWdpX8

# Class Node, a node with value and ref to the next node
class node:
    def __init__(self, value):
        self.value = value      # init with a value
        self.next = None        # pointer to the next node, empty by default

# Class Linked list, add node will append to the list
class LinkedList:
    def __init__(self):
        self.head = None        # init with empty list

    def __repr__(self):
        pass                    # traversing the list and print out values

    def __contains__(self):
        pass                    # check if a value exist in a list

    def __lens__(self):
        pass                    # return size of the list

    def append(self, value):
        pass                    # add a value to the end of thelist

    def prepend(self, value):
        pass                    # add a value to the start of thelist

    def insert(self, value, index):
        pass                    # add a value to a certain position

    def delete(self, value):
        pass                    # delete a value in the list

    def pop(self, value):
        pass                    # delete a value in the list with index

    def get(self, value):
        pass                    # return the value in the list at the specific index

    def print(self, value):
        pass                    # just a print function

if __name__ == "__main__":
    pass
