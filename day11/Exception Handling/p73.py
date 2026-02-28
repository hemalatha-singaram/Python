try:
    num=int(input("enter a number: "))
    print(100/num)
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
    print("That's not a number!")
