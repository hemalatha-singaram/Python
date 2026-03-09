import re
text = "My number is 9876543210"
result = re.sub(r"\d", "*", text)
print(result)