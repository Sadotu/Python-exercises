x = 100

def bottles(count):
	for x in range(count):
		print "%d bottles of beer on the wall, %d bottles of beer. Take one down, pass it around, %d bottles of beer on the wall." % (count, count, count-1)
		count = count-1

print bottles(x)

