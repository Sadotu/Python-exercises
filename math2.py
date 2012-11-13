lst = [1, 2, 3, 4]

def plus(lst):
	output = lst[0]
	for number in lst:
		result = output + number
	return result

print plus(lst)
