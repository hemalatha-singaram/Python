def is_palindrome(string):
	reversed_string = string[::-1]
	return string == reversed_string
string="mom"
print(is_palindrome(string))
string="stupid man"
print(is_palindrome(string))