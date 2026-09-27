# Writing a text in the file

file=open("report1.txt", "w")
file.write("Global warming is the long-term increase in Earth's average temperature")

# adding text in teh file
file=open("report1.txt", "a")
file.write("\nThis is the line that was not written in the file")