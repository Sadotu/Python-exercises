def translate(lst):
	output = []
	swed = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	for item in lst:
		if item in swed:
			#print item
			output += [swed[item]]
	return output

if __name__ == "__main__":
	lst = ["merry", "christmas", "and", "happy", "new", "year"]
	print translate(lst)
