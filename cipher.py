import string
#get user input
n = int(input("send me a number : "))
m = input("write me a message : ")

#create an alphabet to find the index of the position
#this is al ist of letters for the alphabet
alphabet = list(string.ascii_lowercase)

newmessage = []
print(n)
print(m)
print(alphabet)

#set up a for loop to loop through every letter in message m to get the index
for i in m:
    if i == " ":
        newmessage.append(i)
    else:
        currentposition = alphabet.index(i)
        print(currentposition)
        newposition = currentposition + n
        print(f"This is the new position {newposition}")
#use find method to get current positon of letter
        newmessage.append(alphabet[newposition])
print(f"This is the new alphabet list {newmessage}")

encryptednote = "".join(newmessage)
print(encryptednote)

#make the
