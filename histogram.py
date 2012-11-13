lst = [4, 6, 7]

def histogram(lst):
	output = ""
	for number in lst:
		output += "\n"
		for i in range(number):
			output += "*"
	return output[1:]

print histogram(lst)
