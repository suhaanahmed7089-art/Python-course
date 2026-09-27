# Printing how many lines are present in bio.txt

import os
try:    
    with open("bio.txt", "r") as file:
        lines=file.readlines()
        print(len(lines))
except FileNotFoundError:
    print("File not Found!")