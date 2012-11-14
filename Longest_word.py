import sys
sys.path.append("/home/nicker/Desktop/Python-exercises")
import max_in_list

def longest_word(lst):
	chars = map(len, lst)
	output = max_in_list.max_in_list(chars)
	return output

if __name__ == "__main__":
	lst = ["hond", "kat", "olifant", "giraffe", "walvis", "krokodil", "sgbedbsdbwr"]
	print longest_word(lst)
