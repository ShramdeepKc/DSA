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
print ("num", num4)
print ("num", num3)
print ("num", id(num4))
print ("num", id(num3))