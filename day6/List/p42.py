'''Challenge 1: Create a list [3, 1, 4, 1, 5, 9, 2, 6, 1] and answer these without running the code first:
How many times does 1 appear?
What is the index of 9?
What does the list look like after sorting?'''
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 1]
print(numbers.count(1))
print(numbers.index(9))
numbers.sort()
print(numbers)