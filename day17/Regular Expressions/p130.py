import re
# validate phone number (10 digits)
def is_valid_phone(phone):
    pattern = r"^\d{10}$"
    return bool(re.match(pattern, phone))
print(is_valid_phone("9876543210"))  # True
print(is_valid_phone("123"))         # False
# extract emails from text
text = "Contact us at hema@gmail.com or support@python.org"
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)  # ['hema@gmail.com', 'support@python.org']
# replace all digits with *
text = "My number is 9876543210"
result = re.sub(r"\d", "*", text)
print(result)  # My number is **********