#  aruthematic operators

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

print("x + y: " ,x + y) #Addition  
print("x - y: " ,x - y)  #Subtraction
print("x * y: " ,x * y)   #Multiplication
print("x / y: " ,x / y)   #Division
print("x**y: " ,x**y)    # x to the power of y

# Comparision operators

print("x > y: " ,x > y)   #Greater than
print("x < y: " ,x < y)   #Less than
print("x == y: " ,x == y)  #Equal to
print("x != y: " ,x != y)  #Not equal to

# Logical operators

print("x > y and x < y: " ,x>y and x<y)   #Both conditions must be true
print("x > y or x < y: " ,x>y or x<y)    #At least one condition must be true
print("not(x > y): " ,not(x>y))   #Reverse the result of x>y
 
#  Assignment operators

a =4
b = 7

a+=4
b+=2
print("a: " , a)   # a = a + 4
print("b: " , b)   # b = b + 2