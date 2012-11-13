string_input = raw_input("voer een letter in: ")

def vowel(string):
	vowels = "aeiuoAEIUO"
	if string in vowels:
		return True
	else:
		return False

print vowel(string_input)
