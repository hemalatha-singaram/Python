words = ["hello", "world", "python", "is", "fun"]
result = [w.upper() for w in words if len(w) > 3]
print(result)