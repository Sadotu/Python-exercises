import random

def filter_words(lst, n):
	output = []
	for item in lst:
		if len(item) >= n:
			output.append(item)
	return n, output

if __name__ == "__main__":
	lst = ["hond", "kat", "olifant", "giraffe", "walvis", "krokodil", "sgbedbsdbwr"]
	n = random.randint(0, 9)
	print filter_words(lst, n)
