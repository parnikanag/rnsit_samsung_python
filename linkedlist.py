class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, pos):
        node = Node(data)
        if pos == 0:
            node.next, self.head = self.head, node
            return
        current = self.head
        for _ in range(pos - 1):
            if not current: return
            current = current.next
        if not current: return
        node.next, current.next = current.next, node

    def delete_at_position(self, pos):
        if not self.head: return
        if pos == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(pos - 1):
            if not current.next: return
            current = current.next
        if not current.next: return
        current.next = current.next.next

    def reverse(self):
        prev, current = None, self.head
        while current:
            temp = current.next
            current.next = prev
            prev, current = current, temp
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print("List is empty" if not self.head else "")

def main():
    ll = LinkedList()
    while True:
        print("\n1) Insert at Position  2) Delete at Position  3) Reverse  4) Display  5) Exit")
        choice = int(input("Enter choice: "))
        if choice == 1: 
            ll.insert_at_position(int(input("Enter data: ")), int(input("Enter position: ")))
        elif choice == 2: 
            ll.delete_at_position(int(input("Enter position: ")))
        elif choice == 3: 
            ll.reverse()
        elif choice == 4: 
            ll.display()
        elif choice == 5: 
            break
        else: print("Invalid choice")

main()
