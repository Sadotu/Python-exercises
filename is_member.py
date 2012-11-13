#a = ["a", "b", 34, 4624, "dsaf"]
#x = "dsaf"
#y = 546

def is_member(lst, value):
	for item in lst:
		#print item, value
		if item == value:
			return True
	return False

#print is_member(a, x)
#print is_member(a, y)
