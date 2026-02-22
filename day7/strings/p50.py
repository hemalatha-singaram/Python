def reverse_words(string):
	words = string.split()
	reversed_words = words[::-1]
	return " ".join(reversed_words)
string="hello world how are you"
print(f"Reversed string: {reverse_words(string)}")