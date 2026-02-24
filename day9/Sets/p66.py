a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # union - all items from both
               # {1, 2, 3, 4, 5, 6}

print(a & b)   # intersection - only common items
               # {3, 4}

print(a - b)   # difference - items in a but not b
               # {1, 2}