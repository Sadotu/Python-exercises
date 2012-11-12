string = 'I am testing'

def reverse(string):
	totaal = ""
	for char in string:
		totaal = char + totaal
	return totaal

print reverse(string)
