user_input = raw_input("Tell me your sentence: ").lower()

"""r = user_input.replace("!", "")
r = r.replace("?", "")
r = r.replace(".", "")
r = r.replace(",", "")
r = r.replace("/", "")
r = r.replace(" ", "")
r = r.replace("'", "")
r = r.replace('"', '')"""

def no_marks(user_input):
	output = ""
	for char in user_input:
		if char in "abcdefghijklmnopqrstuvwxyz0123456789":
			output += char
	return output

r = no_marks(user_input)

usr_inp = list(r)
output = list(r)
output.reverse()

if usr_inp == output:
	print "This is a Palindrome!\n", user_input, "\n", user_input
else:
	print "This is not a Palindrome!\n", usr_inp, "\n", output


