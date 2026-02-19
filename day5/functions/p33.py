def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_of_three(10, 2, 12))  # Output: 12
print(max_of_three(3, 7, 5))    # Output: 7

def min_and_max(a, b, c):
    return min(a, b, c), max(a, b, c)

low, high = min_and_max(3, 7, 5)
print(low)   # Output: 3
print(high)  # Output: 7