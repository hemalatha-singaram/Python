print(10 / 0)          # ZeroDivisionError
print(int("hello"))    # ValueError
print(x)               # NameError - x not defined
print([1,2,3][10])     # IndexError
open("nofile.txt","r") # FileNotFoundError