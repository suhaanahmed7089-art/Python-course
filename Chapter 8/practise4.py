# printing only first line of the file named bio.txt

with open("bio.txt", "r") as file:
    line1=file.readline()
    print(line1)