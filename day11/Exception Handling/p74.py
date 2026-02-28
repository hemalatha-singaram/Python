
def safe_open(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

print(safe_open("bts.txt"))        # prints content
print(safe_open("missing.txt"))    # File not found!