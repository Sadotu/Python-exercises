import random

def max_two(one, two):
	if one > two:
		return one
	elif one < two:
		return two
	else:
		return one

def accept_lst(lst):
	return reduce(max_two, lst)

lst = [1, 2, 3, 4, 5]
print accept_lst(lst)
