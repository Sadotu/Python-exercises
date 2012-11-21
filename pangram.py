def pangram(lst):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	lst_lower = lst.lower()
	for item in alphabet:
		if item not in lst_lower:
			return "This is not a pangram"
		else:
			return "This is a pangram"

if __name__ == "__main__":
	lst = "Because of your apparent audacity the depressed conqueror is willing to fight you."
	print pangram(lst)
