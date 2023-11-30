# Користувач вводить з клавіатури набір рядків. Збережіть отримані рядки до двозв’язного списку. Після чого
# покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.

# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.prev} <- [{self.data}] -> {self.next} "

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
    
    def remove(self, data_to_rm):
        current = self.head
        prev = None

        while current:
            if current.data == data_to_rm:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                
                return True
            current = current.next

        return False
    
    def show_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def contains(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        return False

my_lst = DoublyLinkedList()

strs = input("Enter strings separated by space: ").split()
for string in strs:
    my_lst.append(string)


while True:
    choice = int(input("""
1. Add element
2. Replace element
3. Check element
4. Remove element
5. Display elements
0. Exit                                                                                                                   
"""))
    
    match choice:
        case 0:
            break
        case 1:
            elem = input("Enter element: ")
            my_lst.append(elem)
        case 2:
            elem = input("Enter elem to replace: ")
            elem_repl = input("Enter new elem: ")
            my_lst.replace(elem, elem_repl)
        case 3:
            elem = input("Enter elem to check: ")
            print(my_lst.contains(elem))
        case 4:
            elem = input("Enter elem to remove: ")
            my_lst.remove(elem)
        case 5:
            my_lst.show_list()
        case _:
            print("Incorrect action")