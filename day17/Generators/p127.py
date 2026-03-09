def fibonacci():
    a, b = 0, 1        # start with 0 and 1
    count = 0
    while count < 10:
        yield a        # yield current number
        a, b = b, a+b  # next number = sum of previous two
        count += 1

for num in fibonacci():
    print(num)
