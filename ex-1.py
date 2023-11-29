# Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
# чого покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"[{self.data}] -> {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f"{self.head}"

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node
    
    def remove(self, data_to_rm):
        current = self.head
        prev = None

        while current and current.data != data_to_rm:
            prev = current
            current = current.next

        if current:
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next
            
            del current
        else:
            print('key not found')

    def show_list(self):
        print(my_lst)

    def contains(self, value):
        current = self.head

        while current and current.data != value:
            current = current.next
        
        if current:
            return True



    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f"Значення {old_data} замінено на {new_data}")
                return
            current = current.next
        print(f"Значення {old_data} не знайдено у списку")

my_lst = LinkedList()
nums = input("Введіть усі числа через пробіл ").split()
for num in nums:
    my_lst.append(int(num))
print(my_lst)

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
            elem = int(input("Enter element: "))
            my_lst.append(elem)
        case 2:
            elem = int(input("Enter elem to replace: "))
            elem_repl = int(input("Enter new elem: "))
            my_lst.replace(elem, elem_repl)
        case 3:
            elem = int(input("Enter elem to check: "))
            print(my_lst.contains(elem))
        case 4:
            elem = int(input("Enter elem to remove: "))
            my_lst.remove(elem)
        case 5:
            my_lst.show_list()
