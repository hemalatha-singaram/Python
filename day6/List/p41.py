numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))  # Output: 1
fruits = ["apple", "banana"]
fruits.extend(["mango", "grape"])
print(fruits)  # ['apple', 'banana', 'mango', 'grape']
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # []
fruits = ["apple", "banana"]
fruits2 = fruits.copy()
fruits2.append("mango")
print(fruits)   # ['apple', 'banana']      -- unchanged!
print(fruits2)  # ['apple', 'banana', 'mango']