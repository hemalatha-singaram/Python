class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # if there was an error
            print(f"Error type: {exc_type}")
            print(f"Error message: {exc_val}")
        return True  # suppresses the error!

with MyContext():
    print(10 / 0)  # causes ZeroDivisionError

print("Program continues!")