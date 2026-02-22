fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]  # can mix types!
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # mango
print(fruits[-1])  # mango  (negative = from the end)
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3]
print(numbers[2:])    # [3, 4, 5]
print(numbers[:])     # [1, 2, 3, 4, 5] (copy of the whole list)
fruits = ["apple", "banana", "mango"]

fruits.append("grape")     # adds to the end
fruits.insert(1, "kiwi")   # adds at index 1
fruits.remove("banana")    # removes by value
fruits.pop()               # removes last item
fruits.sort()              # sorts alphabetically
fruits.reverse()           # reverses the list
print(len(fruits))         # counts items
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
    
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)    # True
print("grape" in fruits)    # False