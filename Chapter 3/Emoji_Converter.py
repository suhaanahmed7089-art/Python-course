# Emoji Converter
# This program converts a sentence into emojis.

msg=input("Enter a sentence: ")

msg=msg.replace(":)","😀")
msg=msg.replace(":(","😞")
msg=msg.replace("<3","❤️")
msg=msg.replace(":D","😃")

print(msg)
