import sys
sys.path.append("/media/Tardis/Python the hard way rawr/Python-exercises")
import is_member

lst1 = [2, 4, "gssr", 45, "hallo2"]
lst2 = ["sg", 54, "hallo1", 2345, 2]

def overlapping(lst1, lst2):
	for item in lst2:
		if	is_member.is_member(lst1, item):
			return item
	return None

print overlapping(lst1, lst2)
