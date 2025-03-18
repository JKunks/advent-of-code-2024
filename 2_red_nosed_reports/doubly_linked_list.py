# Python Program for a doubly linked list at the beginning of a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.prev: Node = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.length: int = 0

    # Function to insert a node at the beginning of a doubly linked list
    def insert(self, data, current_node: Node = None):
        new_node = Node(data)
        if current_node:
            next_node = current_node.next
            new_node.next = next_node
            new_node.prev = current_node
            current_node.next = new_node
            if next_node:
                next_node.prev = new_node
        else:
            if self.head:
                self.head.prev = new_node
                new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node

    def remove(self, node: Node):
        if node.prev:
            prev: Node = node.prev
            prev.next = node.next
        if node.next:
            next: Node = node.next
            next.prev = node.prev
            if self.head == node:
                self.head = next
        self.length -= 1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
