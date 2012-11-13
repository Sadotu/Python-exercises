getal_1 = raw_input("Voer getal 1 in: ")
getal_2 = raw_input("Voer getal 2 in: ")

def the_max(getal1, getal2):
	if getal1 <= getal2:
		return getal2
	if getal1 >= getal2:
		return getal1
	else:
		return "Je verneukt iets"

print the_max(getal_1, getal_2)
