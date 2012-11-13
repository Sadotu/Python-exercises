getal_1 = raw_input("Voer getal 1 in: ")
getal_2 = raw_input("Voer getal 2 in: ")
getal_3 = raw_input("Voer getal 3 in: ")

def max_of_three(getal1, getal2, getal3):
	output = [getal1]
	if getal2 >= getal1:
		output.remove(output[0])
		output.append(getal2)
	if getal3 >= getal2:
		output.remove(output[0])
		output.append(getal3)
	else:
		return "Je verneukt iets"
	return output.pop()

print max_of_three(getal_1, getal_2, getal_3)
