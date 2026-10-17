# Creating a class named student
class student:
    def __init__(self,name="",roll="",course=""):
        self.name=name
        self.roll=roll
        self.course=course
    def get_details(self):
        # Taking input from the user for student details
        self.name=input("Enter the name of the student: ")
        self.roll=input("Enter the roll no. of the student: ")
        self.course=input("Enter the course of the student: ")
    def display(self):
        print("Student details:")
        print("Name:",self.name)
        print("Roll no.:",self.roll)
        print("Course:",self.course)

s1=student()    # Init method will be called
s1.get_details()
s1.display()
