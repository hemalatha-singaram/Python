import re

text = "Hello my name is Hema and I am 20 years old"

# search - finds first match
result = re.search("Hema", text)
print(result.group())  # Hema

# findall - finds all matches
result = re.findall("a", text)
print(result)  # ['a', 'a', 'a', 'a']

# match - checks if pattern matches at beginning
result = re.match("Hello", text)
print(result.group())  # Hello

# sub - replaces matches
result = re.sub("Hema", "Alice", text)
print(result)  # Hello my name is Alice...