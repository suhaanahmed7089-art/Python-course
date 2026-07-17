
# List in python
marks=[65,87,58,94,65,65]

# Lists are mutable
marks[2]=78

print(marks[2])
print(len(marks))
print(marks[0:4])

# Prints minimum value in the index
print(min(marks))  

# Prints maximum value in the list
print(max(marks))   

# sorts the elements of the lists
marks.sort()
print(marks)

# Reverses the elements of the lists
marks.reverse()
print()

# inserts the elements at the end of the list
marks.append(88)
print(marks)

# Removes the first occurence of the list
marks.remove(65)
print(marks) 

# removes the element at the place of the index
marks.pop(2) 
print(marks)
