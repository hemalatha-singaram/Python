import re
extract_numbers=("I am 20 years old and I have 3 cats and 1 dog")
digits=re.findall(r"\d+",extract_numbers)
print(digits)