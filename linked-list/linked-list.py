# Linked List Code Example by NeuralNine on YouTube
# https://www.youtube.com/watch?v=1iz9SRWdpX8

# Class Node, a node with value and ref to the next node
class Node:
    def __init__(self, value):
        self.value = value      # init with a value
        self.next = None        # pointer to the next node, empty by default

# Class Linked list, add node will append to the list


class LinkedList:
    # init with empty list
    def __init__(self):
        self.head = None

    # traversing the list and print out values
    def __repr__(self):
        pass

    # O(n) - linear: avr -> check half the list / worst -> check whole list
    # check if a value exist in a list
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) - linear: count through all element in the list
    # O(n) - constant if size is included in the class
    # return size of the list
    def __lens__(self):
        counter = 0
        last = self.head
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(n) - linear: the more element there is then the longer it takes
    # add a value to the end of the list
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # O(n) - constant: no matter what it will perform the same
    # add a value to the start of the list
    def prepend(self, value):
        first = Node(value)
        first.next = self.head
        self.head = first

    # O(n) - linear: the higher the index is then the longer it takes
    # add a value to a certain position
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            # if list is empty and index != 0
            if self.head is None:
                raise ValueError("Index out of bound")
            else:
                last = self.head
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index out of bound")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    # delete a value in the list
    def delete(self, value):
        last = self.head

        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
        else:
            raise ValueError("Index out of bound")

    # delete a value in the list with index
    def pop(self, value):
        pass

    # return the value in the list at the specific index
    def get(self, value):
        pass

    # just a print function
    def print(self, value):
        pass


if __name__ == "__main__":
    pass
