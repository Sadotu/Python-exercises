def filter_long_words(word):
	n = 4
	print n
	if len(word) > n:
		return True
	return False

def fil(lst):
	return filter(filter_long_words, lst)

if __name__ == "__main__":
	lst = ["hond", "kat", "olifant", "giraffe", "walvis", "krokodil", "sgbedbsdbyjwr"]
	print fil(lst)
