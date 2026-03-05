# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper
# def greet():
#     print("Hello!")

# greet = my_decorator(greet)  # wrapping greet with decorator
# greet()

#------------------------decorator syntax------------------------
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
@my_decorator   # same as greet = my_decorator(greet)
def greet():
    print("Hello!")
greet()
