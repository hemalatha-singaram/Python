from contextlib import contextmanager

@contextmanager
def safe_open(filename):
    try:
        file = open(filename, "r")
        yield file
    except FileNotFoundError:
        print("File not found!")
    finally:
        print("Done!")

with safe_open("bts.txt") as f:
    print(f.read())