lst = [1, 2, 3, 4]

def sum_plus(lst):
	total = 0
	for number in lst:
		total = total + number
	return total

print sum_plus(lst)

def multiply(lst):
	total = 1
	for number in lst:
		total = total * number
	return total

print multiply(lst)
