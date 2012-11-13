user_input = raw_input("Tell me your sentence: ").lower()

d_exclamation = user_input.replace("!", "")
d_questionmark = d_exclamation.replace("?", "")
d_dot = d_questionmark.replace(".", "")
d_comma = d_dot.replace(",", "")
d_slash = d_comma.replace("/", "")
d_space = d_slash.replace(" ", "")
d_single_quote = d_space.replace("'", "")
d_double_quote = d_single_quote.replace('"', '')

usr_inp = list(d_double_quote)
output = list(d_double_quote)
output.reverse()

if usr_inp == output:
	print "This is a Palindrome!\n", usr_inp, output
else:
	print "This is not a Palindrome!\n", usr_inp, output
