# Printing a countdown before something exciting happens(like "Launching or Happy new year")
import time
count=int(input("Enter the counter time"))
print("Countdown starts now")
for i in range(count,0,-1):
    print(i)
    time.sleep(1);
print("Happt Birthday")
