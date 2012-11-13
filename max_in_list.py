def max_in_list(lst):
	output = 0
	for item in lst:
		if item >= output:
			output = item
	return output

if __name__ == "__main__":
	lst = [2, 4, 5, 6, 3, 7]
	print max_in_list(lst)
		
