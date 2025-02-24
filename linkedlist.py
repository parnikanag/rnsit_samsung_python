class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.rear is None:
            self.rear = new_node

    def insert_rear(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.rear = new_node
        else:
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_front(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position not in range")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_front(self):
        if not self.head:
            print("List is empty")
            return
        print(self.head.data)
        self.head = self.head.next
        if self.head is None:
            self.rear = None

    def delete_rear(self):
        if not self.head:
            print("List is empty")
            return
        if self.head == self.rear:
            print(self.head.data)
            self.head = self.rear = None
            return
        current = self.head
        while current.next and current.next != self.rear:
            current = current.next
        print(self.rear.data)
        current.next = None
        self.rear = current

    def delete_at_position(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.delete_front()
            return
        current = self.head
        count = 0
        while current.next and count < pos - 1:
            current = current.next
            count += 1
        if current.next is None:
            print("Position not in range")
            return
        print(current.next.data)
        current.next = current.next.next
        if current.next is None:
            self.rear = current

    def reverse(self):
        print("Before reversing:", end=" ")
        self.display()
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("After reversing:", end=" ")
        self.display()

    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

def show_menu():
    print("\nChoose an operation:")
    print("1) Insert at front\n2) Insert at rear\n3) Insert at a position")
    print("4) Delete from front\n5) Delete from rear\n6) Delete from a position")
    print("7) Reverse the list\n8) Display the list\n9) Exit")

main()
