# # BASICS OF PYTHON
# def find_max(lst):
#     max_num = float('-inf')  # Initialize max_num to negative infinity
#     for num in lst:
#         if num > max_num:
#             max_num = num
#     return max_num
#
#
# # Example usage
# numbers = [3, 7, 1, 9, 4, 6, 8, 2]
# result = find_max(numbers)
# print("Maximum element:", result)
#
# stock_prices = [234, 233, 236, 238]
# print(stock_prices[3])
#
#
# class Cookie:
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_color(self):
#         return self.color
#
#
# cookie_1 = Cookie('#000000')
# cookie_2 = Cookie('#00FF00')
#
# print('cookie is', cookie_1.get_color())
# print('cookie is', cookie_2.get_color())
#
# num4 = 10
# num3 = num4
# print("num", num4)
# print("num", num3)
# print("num", id(num4))
# print("num", id(num3))


# DATASTRUCTURES AND ALGORITHMS LINKED LIST
class Node:
    def __init__(self, value):  # initialize new value
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):  # initialize head and tail as new value
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
        new_node = Node(value)  # get value
        if self.head is None:  # check if head is None then create new node as head and as tail
            self.head = new_node
            self.tail = new_node
        else:  # else append next new node
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1  # increase by length 1

    def pop(self):
        if self.length == 0:  # check length if 0 then return none
            return None
        temp = self.head  # define temp as self.head and pre as self.head
        pre = self.head

        while temp.next:  # use while loop for pre value and temp
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1  # pop the value

    def prepend(self, value):  # add new value in list
        new_node = Node(value)  # assign new_node as  value
        if self.length == 0:  # check length
            self.head = new_node  # if length is 0 then assign new node as head and as tail
            self.tail = new_node
        else:
            new_node.next = self.head  # else create and add new head as new_node
            self.head = new_node
        self.length += 1


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(0)
my_linked_list.pop()
my_linked_list.print_list()
