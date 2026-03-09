import re

# find all digits
text = "I am 20 years old and my phone is 9876543210"
digits = re.findall(r"\d+", text)
print(digits)  # ['20', '9876543210']

# find all words
words = re.findall(r"\w+", "Hello, World!")
print(words)  # ['Hello', 'World']

# check if email is valid
email = "hema@gmail.com"
pattern = r"\w+@\w+\.\w+"
if re.match(pattern, email):
    print("Valid email!")