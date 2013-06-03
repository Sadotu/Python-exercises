def max_two(one, two):
	if one > two:
		return one
	elif one < two:
		return two
	else:
		return one

def accept_lst(lst):
	return reduce(max_two, lst)

def longest_word(lst):
	chars = map(len, lst)
	output = accept_lst(chars)
	return output

if __name__ == "__main__":
	lst = ["hond", "kat", "olifant", "giraffe", "walvis", "krokodil", "sgbedbsdbyjwr"]
	print longest_word(lst)
