# Create a program using global keyword to modify a variable from inside the function.

def modify():
    global var
    var+=5
    print("Value of variable inside the function", var)

var=10
print("Value of variable outside the function", var)
modify()
