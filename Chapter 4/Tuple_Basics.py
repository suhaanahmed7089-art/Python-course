# Tuples basic

mytuple=(56,64,57)
studenttuple=("Suhaan","Swaraj","Sumit","Tarunya")

# Tuples are immutable

print(studenttuple[2])
print(mytuple[1])

# Empty tuple
emptytuple=()
print(type(emptytuple))

# Singletuple
singletuple=(5,)
print(type(singletuple))

print(studenttuple.index("Sumit"))
print(studenttuple.count("Sumit"))
