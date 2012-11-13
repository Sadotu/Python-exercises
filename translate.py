string = "This is fun".lower()

def trans(string):
	vowels = "aeiou "
	output = ''
	for char in string:
		if char in vowels:
			output += char
		else:
			double = char+"o"+char
			output += double
	return output

print trans(string)
