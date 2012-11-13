integer = 5
string = "x"

def generate_n_chars(integer, string):
	output = ""
	for i in range(integer):
		output += string
	return output

print generate_n_chars(integer, string)
