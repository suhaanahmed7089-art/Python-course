# Taking user input for calculating sum of n terms

n=int(input("Enter the no. of terms: "))
sum=0
for i in range(1,n+1):
    number=int(input("Enter the nummber: "))
    sum=sum+number
print(sum)
