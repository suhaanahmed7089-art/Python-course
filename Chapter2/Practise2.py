x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

sum = x + y     # sum of x and y
print("Sum: " , sum)
print("Data type: " , type(sum))

difference = x-y    # difference of x and y
print("Difference: " , difference)
print("Data type: " , type(difference))

product = x*y    # product of x and y
print("Product: " , product)
print("Data type: " , type(product))

if x>y:     # comparison of x and y
    print("x is greater: ")
elif y>x:
    print("y is greater: ")
else:
    print("x and y are equal: ")

