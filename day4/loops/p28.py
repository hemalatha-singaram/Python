n = int(input("enter a number: "))

# compute the sum of numbers from 1 through n
total = 0
for i in range(1, n+1):
    total += i

print(f"the sum is = {total}")
