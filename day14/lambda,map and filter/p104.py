numbers = [1, 2, 3, 4, 5, 6]

# first filter evens, then square them
evens = list(filter(lambda n: n % 2 == 0, numbers))
squared_evens = list(map(lambda n: n * n, evens))
print(squared_evens)  # [4, 16, 36]