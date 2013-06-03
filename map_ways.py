def map_type_for(words):
	integer = []
	for word in words:
		integer.append(len(word))
	return integer

def map_help(words):
	integer = 0
	for word in words:
		integer += len(word)
	return integer

def map_type_map(words):
	integer = map(map_help, words)
	return integer

words = ["one", "two", "three", "four"]
print map_type_for(words)
print map_type_map(words)
