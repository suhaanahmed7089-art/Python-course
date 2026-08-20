# Function named show(name,age) that prints your name and age.

def show(name="John",age=25):   #Giving default values to the function parameters
    print(f"{name} is {age} years old")

show("Suhaan",19)     # Function is being called here with arguments
show()                 # Function is being called here with default values
