# one parameter
square = lambda n: n * n
print(square(5))   # 25

# two parameters
add = lambda a, b: a + b
print(add(3, 4))   # 7

# with condition
even = lambda n: True if n % 2 == 0 else False
print(even(4))     # True
print(even(5))     # False