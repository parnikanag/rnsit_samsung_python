class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.rear = None

    def insert_front(self, data):
        node = Node(data)
        node.next, self.head = self.head, node
        if not self.rear: self.rear = node

    def insert_rear(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.rear = node
        else:
            self.rear.next, self.rear = node, node

    def insert_at_position(self, data, pos):
        if pos == 0: return self.insert_front(data)
        node, current, i = Node(data), self.head, 0
        while current and i < pos - 1:
            current, i = current.next, i + 1
        if not current: return print("Position not in range")
        node.next, current.next = current.next, node
        if not node.next: self.rear = node

    def delete_front(self):
        if not self.head: return print("List is empty")
        print(self.head.data)
        self.head = self.head.next
        if not self.head: self.rear = None

    def delete_rear(self):
        if not self.head: return print("List is empty")
        if self.head == self.rear:
            print(self.head.data)
            self.head = self.rear = None
            return
        current = self.head
        while current.next != self.rear:
            current = current.next
        print(self.rear.data)
        current.next, self.rear = None, current

    def delete_at_position(self, pos):
        if not self.head: return print("List is empty")
        if pos == 0: return self.delete_front()
        current, i = self.head, 0
        while current.next and i < pos - 1:
            current, i = current.next, i + 1
        if not current.next: return print("Position not in range")
        print(current.next.data)
        current.next = current.next.next
        if not current.next: self.rear = current

    def reverse(self):
        prev, current = None, self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

    def display(self):
        current = self.head
        if not current: return print("List is empty")
        while current:
            print(current.data, end=" -> " if current.next else " ")
            current = current.next
        print()

def main():
    ll = LinkedList()
    while True:
        print("\n1) Insert Front  2) Insert Rear  3) Insert at Position  4) Delete Front")
        print("5) Delete Rear  6) Delete at Position  7) Reverse  8) Display  9) Exit")
        choice = int(input("Enter choice: "))
        if choice == 1: 
            ll.insert_front(int(input("Enter data: ")))
        elif choice == 2: 
            ll.insert_rear(int(input("Enter data: ")))
        elif choice == 3: 
            ll.insert_at_position(int(input("Enter data: ")), int(input("Enter position: ")))
        elif choice == 4: 
            ll.delete_front()
        elif choice == 5:
            ll.delete_rear()
        elif choice == 6: 
            ll.delete_at_position(int(input("Enter position: ")))
        elif choice == 7: 
            ll.reverse()
        elif choice == 8: 
            ll.display()
        elif choice == 9: 
            break
        else: print("Invalid choice")

main()
