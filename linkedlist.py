class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ins_front(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node

    def ins_rear(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.link:
            last = last.link
        last.link = new_node

    def ins_pos(self, data, pos):
        if pos == 0:
            self.ins_front(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.link
            count += 1
        if current is None:
            print("Position out of range.")
            return
        new_node.link = current.link
        current.link = new_node

    def del_front(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.link

    def del_rear(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.link is None:
            self.head = None
            return
        current = self.head
        while current.link and current.link.link:
            current = current.link
        current.link = None

    def del_pos(self, pos):
        if not self.head:
            print("List is empty.")
            return
        if pos == 0:
            self.del_front()
            return
        current = self.head
        count = 0
        while current.link and count < pos - 1:
            current = current.link
            count += 1
        if current.link is None:
            print("Position out of range.")
            return
        current.link = current.link.link

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.link
            current.link = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            if current.link:
                print(current.data, end=" -> ")
            else:
                print(current.data, end="")
            current = current.link
        print()

def menu():
    print("\nChoose an operation:")
    print("1. Insert an element at the front (ins_front)")
    print("2. Insert an element at the rear (ins_rear)")
    print("3. Insert an element at a specific position (ins_pos)")
    print("4. Delete an element from the front (del_front)")
    print("5. Delete an element from the rear (del_rear)")
    print("6. Delete an element from a specific position (del_pos)")
    print("7. Reverse the list")
    print("8. Print the list")
    print("9. Exit")

def main():
    llist = LinkedList()
    
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            data = int(input("Enter the data to insert at front: "))
            llist.ins_front(data)
        elif choice == "2":
            data = int(input("Enter the data to insert at rear: "))
            llist.ins_rear(data)
        elif choice == "3":
            data = int(input("Enter the data to insert: "))
            pos = int(input("Enter the position to insert at: "))
            llist.ins_pos(data, pos)
        elif choice == "4":
            llist.del_front()
        elif choice == "5":
            llist.del_rear()
        elif choice == "6":
            pos = int(input("Enter the position to delete from: "))
            llist.del_pos(pos)
        elif choice == "7":
            llist.reverse()
        elif choice == "8":
            llist.print_list()
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
