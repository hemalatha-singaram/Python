def safe_convert(string):
    try:
        return int(string)
    except ValueError:
        return 0
print(safe_convert("123"))
print(safe_convert("abc"))  