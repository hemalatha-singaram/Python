from contextlib import contextmanager
@contextmanager
def suppress_errors():
    try:
        yield
    except Exception as e:
        print(f"An error occurred: {e}")
    
with suppress_errors():
    print(10 / 0)  # normally crashes!
    
print("Program continues!")  # should still run!