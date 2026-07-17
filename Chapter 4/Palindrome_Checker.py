# Checking whether the no. is palindrome or not using if else condition

num=int(input("Enter a no.: "))
original=num
rev=0

while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10

if original==rev:
    print("No. is palindrome");
else:
    print("No. is not palindrome");
