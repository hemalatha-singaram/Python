def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished!")
        return result
    return wrapper
@logger
def add(a, b):
    return a + b
add(3, 4)
print(add(3, 4))