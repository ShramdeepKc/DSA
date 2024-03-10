# BASICS OF PYTHON
def find_max(lst):
    max_num = float('-inf')  # Initialize max_num to negative infinity
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num


# Example usage
numbers = [3, 7, 1, 9, 4, 6, 8, 2]
result = find_max(numbers)
print("Maximum element:", result)

stock_prices = [234, 233, 236, 238]
print(stock_prices[3])


class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self):
        return self.color


cookie_1 = Cookie('#000000')
cookie_2 = Cookie('#00FF00')

print('cookie is', cookie_1.get_color())
print('cookie is', cookie_2.get_color())

num4 = 10
num3 = num4
print("num", num4)
print("num", num3)
print("num", id(num4))
print("num", id(num3))


# DATASTRUCTURES AND ALGORITHMS LINKED LIST
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()

print(my_linked_list.pop())

my_linked_list.print_list()
