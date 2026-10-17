# Using concept of polymorphism to calculate area of rectangle, square and circle

# Creating a class to for calculating area of rectangle
class rectangle:
    def area(self, length="",width=""):
        print("Calculating area of rectangle")
        print("")
        # Taking user iinput for length and width of rectangle
        self.length=float(input("Enter the length of rectangle: "))
        self.width=float(input("Enter the width of rectangle "))
        area=self.length*self.width
        print("Area of rectangle is:",area)
        print("")

# Creating a class for calculating area of square
class square:
    def area(self,side=""):
        print("Calculating area of square")
        print("")
        # Taking user input for side of square
        self.side=float(input("Enter the side of square: "))
        area=self.side*self.side
        print("Area of square is:",area)
        print("")

# Creating a class for calculating area of circle
class circle:
    def area(self,radius=""):
        print("Calculating area of circle")
        print("")
        # Taking user input for radius of circle
        self.radius=float(input("Enter the radius of the circle: "))
        area=3.14*self.radius*self.radius
        print("Area of circle is:",area)
# creating a list of objects for rectangle, square and circle
# and calling area method for each object in the list

shape=[rectangle(),square(),circle()]
for i in shape:
    i.area()  
