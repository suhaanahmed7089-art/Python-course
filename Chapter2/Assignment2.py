# Bill split calculator

total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the no. of people: "))

print("Total bill amount: " , total_bill)
print("No. of people: " , num_people)

split_amount = total_bill/num_people
print("Each person will pay: " , split_amount)