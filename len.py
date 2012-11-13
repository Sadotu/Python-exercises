mylist = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ,9  , 10, "", "a"]

def count(lst):
	count = 0
	for item in lst:
		count = count + 1
	return count

print count(mylist)
