# Write a program to find a certain word from a file named mydata.txt

file=open("mydata.txt", "r")
data=file.read()

data=data.lower()

word=input("Enter the word to found: ")

if word in data:
    print(f"Yes {word} is present file")
else:
    print(f"No {word} is not present in th file ")