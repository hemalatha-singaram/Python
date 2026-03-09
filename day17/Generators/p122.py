def get_numbers():
    yield 1
    yield 2
    yield 3

for num in get_numbers():
    print(num)
