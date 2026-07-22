food={"Samosa","Pasta","Pizza","Samosa"}
print(type(food))
print(food)

food.add("Noodle")
print(food)
food.remove("Pasta")
print(food)

# Sets do not entertain duplicacy

empty_set=set()      # Empty set
print(type(empty_set))
nums={1,2,3,4,5}       # Non-emty set
print(type(nums))

print(food.union(nums))
