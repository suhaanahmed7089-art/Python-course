# Tempreture converter

temp1 = float(input("Enter the temperature in celcius: "))

# take farenheit equivalent to celcius

temp2 = (temp1 * 9/5) + 32

# take kelvin equivalent to celcius

temp3 = temp1 + 273.15

print("Temperature in celcius: " , temp1)
print("Temperature in fahrenheit: " , temp2)

# Rounding off the values of farenheit and kelvin to 2 decimal places 

temp2 = round(temp2, 2)
temp3 = round(temp3, 2)

print("Temperature in kelvin: " , temp3)
temp3 = round(temp3,2)