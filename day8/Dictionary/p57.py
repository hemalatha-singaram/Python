def flip_dict(dictionary):
    flipped = {}
    for key, value in dictionary.items():
        flipped[value] = key   # value becomes key, key becomes value
    return flipped
print(flip_dict({"a": 1, "b": 2}))  
