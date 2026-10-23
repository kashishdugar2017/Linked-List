class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if self.head is None:
            print("List is empty!!!")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not  None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"{data} not found!")

    def search(self,data):
        current = self.head
        position = 0
        while current is not None:
            if current.data == data:
                print(f"Found {data} at position {position}!!!")
                return
            current = current.next 
            position += 1
        print(f"{data} not found!")
