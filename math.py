number1 = int(raw_input("input: "))
sum_multi = raw_input("+ or x? ")
number2 = int(raw_input("input: "))

def plus(nu1, nu2):
	result = nu1 + nu2
	return result

def multiply(nu1, nu2):
	result = nu1 * nu2
	return result

if sum_multi == "+":
	print plus(number1, number2)
if sum_multi == "x":
	print multiply(number1, number2)
else:
	"you re fucking things up"
