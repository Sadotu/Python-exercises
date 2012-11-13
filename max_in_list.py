lst = [2, 4, 5, 6, 3, 7]

def max_in_list(lst):
	output = 0
	for item in lst:
		if item >= output:
			output = item
	return output

print max_in_list(lst)
		
