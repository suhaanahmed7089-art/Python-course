# Write a code to open a file named mydata.txt in read mode
file=open("mydata.txt", "r")
data=file.read()
file.close()
print(data)