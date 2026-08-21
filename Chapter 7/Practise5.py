# Function named num(a,b) that prints both sum and difference of two numbers.

def num(a=15,b=10):     # Giving default value to the function parameters
    sum=a+b
    diff=a-b
    print(f"Sum = {sum} \nDifference = {diff}")

num(54,44)   # Function is being called here with arguments
num()       # Function is being called here with default values
