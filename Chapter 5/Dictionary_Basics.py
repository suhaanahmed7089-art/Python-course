# Dictionary Basics

# Creating Dictionary

student={
    "name":"Suhaan Ahmed",
    "age":19,
    "city":"Punjab"
}
print(type(student))

# Accessing values

print(student["name"])   # Suhaan Ahmed
print(student["age"])    # 19
print(student["city"])   # Punjab
print(student)

# Adding or updating new values

student["college"]="CGC Landran"     # Adding new value
student["age"]=20     # Updating existing value
print(student)

# Removing values

student.pop("city")

# Performing various methods of dictionary

print(student.keys())     # Return ALL keys
print(student.values())   #Return all values
print(student.items())    #Return all keys and values as tuples
print(student.get("name"))  #returns the valye of a key safely
