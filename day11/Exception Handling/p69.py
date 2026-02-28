try:
    print(10 / 0)        # code that might fail
except ZeroDivisionError:
    print("Can't divide by zero!")  # handle the error
    
#Catching Multiple Errors

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("That's not a number!")