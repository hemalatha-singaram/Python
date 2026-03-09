def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up(5):
    print(num)
