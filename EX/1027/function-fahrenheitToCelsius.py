def fahrenheitToCelsius (temp) :
	fahrenheit = (5 / 9) * (temp - 32)
	return fahrenheit

fahrenheit = eval (input ("Enter a temperature in degrees Fahrenheit: "))
celsius = fahrenheitToCelsius (fahrenheit)

print ("Celsius equivalent: ", celsius, "degrees")
