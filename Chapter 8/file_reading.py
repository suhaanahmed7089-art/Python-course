# Read entire file

with open("mydata.txt", "r") as file:
    data=file.read()
    print(data)
print("\nThe first operation ends here")
print("")

# Read by line

with open("mydata1.txt", "r") as file:
    line1=file.readline()
    line2=file.readline()
    line3=file.readline()
    line4=file.readline()
    line5=file.readline()
    line6=file.readline()
    data=file.read()
    print("Line 1", line1)
    print("Line 2", line2)
    print("Line 3", line3)
    print("Line 4", line4)
    print("Line 5", line5)
    print("Line 6", line6)
    print("Data of the file is:", data)   # The file is empty so it will not print anything

print("\nSecond operation ends here")
print("")
    # Read all lines

with open("mydata1.txt", "r") as file:
    lines=file.readlines()
    print(lines)           # It prints list of stringsf