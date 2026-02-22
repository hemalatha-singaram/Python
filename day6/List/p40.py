#Challenge 3: Write a function list_sum that takes a list and returns the sum without using the built-in sum() function.
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
print(list_sum(numbers))