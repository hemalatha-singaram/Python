def word_count(string):
    words = string.split()  # split into list of words
    counts = {}             # empty dictionary
    for word in words:
        if word in counts:
            counts[word] += 1  # word seen before, add 1
        else:
            counts[word] = 1   # word seen first time, set to 1
    return counts
print(word_count("hello world hello"))  
