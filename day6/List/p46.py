numbers=[]
while True:
    num=int(input("enter a number:"))
    if num==0:
        break
    numbers.append(num)
print(sum(numbers))