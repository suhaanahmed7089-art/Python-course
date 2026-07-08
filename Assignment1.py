# take diameter as input and calculate area of circle
import math
diameter = float(input("Enter the diameter of the circle: "))
radius = diameter/2
area = math.pi*radius**2
print("Area of the circle is: " , area)