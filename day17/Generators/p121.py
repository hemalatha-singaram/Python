def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
gen = get_numbers()
print(next(gen))  
print(next(gen))  
print(next(gen))  