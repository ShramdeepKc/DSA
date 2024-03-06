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