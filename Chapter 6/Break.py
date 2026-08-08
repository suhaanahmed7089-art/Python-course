# using break statement in for loop

for i in range(1,10):
    if i==7:
        break
    print(i);

print("Break statement ends here")

for j in range(1,10):
    if j==7:
        continue
    print(j);

print("Continue statement ends here")

for k in range(1,10):
    pass   #Future code will go here

print("Pass statement ends here")
