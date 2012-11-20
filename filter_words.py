import random

def filter_words(lst, n):
	list_n = map(len, lst)
	output = []
	x = 0
	for item in list_n:
		if item >= n:
			output.append(lst[x])
		x = x + 1
	return n, output

if __name__ == "__main__":
	lst = ["hond", "kat", "olifant", "giraffe", "walvis", "krokodil", "sgbedbsdbwr"]
	n = random.randint(0, 9)
	print filter_words(lst, n)
