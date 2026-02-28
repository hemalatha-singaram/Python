try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("That's not a number!")
else:
    print("No errors occurred!")    # runs if NO error
finally:
    print("Program finished!")      # ALWAYS runs, error or not