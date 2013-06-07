def translate(word):
	swed = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	if word in swed:
		return swed[word]
	else:
		return ''

def mapp(lst):
	return map(translate, lst)

if __name__ == "__main__":
	lst = ["merry", "christmas", "and", "happy", "new", "year", "seb"]
	print mapp(lst)
