# even_numbers=(n for n in range(20))
# for n in even_numbers:
#     if n%2==0:
#         print(n)
def even_numbers():
    for n in range(1, 21):
        if n % 2 == 0:
            yield n

for num in even_numbers():
    print(num)