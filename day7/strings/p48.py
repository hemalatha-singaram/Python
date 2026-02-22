def count_vowels(vowels):
	count = 0
	for char in vowels:
		if char in "aeiouAEIOU":
			count += 1
	return count
string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"The number of vowels in the string is: {vowel_count}")