# Function that takes a string and returns the count of vowels and consonants separately.

def count(str):
    vowel="aeiouAEIOU"    #This is a local variable and it is only accessinle iside the function.
    vowelcount=0
    consonantcount=0

    for i in str:
        if (i.isalpha()):
            if i in vowel:
                vowelcount+=1
            else:
                consonantcount+=1
    return vowelcount, consonantcount

vowels, consonants=count("Suhaan Ahmed")   # vowel and consonant are global variables and they are accessible outside the function.
print(vowels, consonants)
