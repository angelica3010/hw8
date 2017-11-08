import string
#get user input

#make sure that is not divisible by 26, othwerwise it will not encrypt
while True:
    n = int(input("send me a number that is not a multiple of 26: "))
    if n % 26 != 0:
        break
    else:
        print("I will not accept your input if it is a multiple of 26")

m = input("write me a message : ")

#create an alphabet to find the index of the position
#this is al ist of letters for the alphabet
alphabet = list(string.ascii_lowercase)

newmessage = []
print(n)
print(m)
print(alphabet)

#trying to make sure that the user input is not a muliple of 26





#set up a for loop to loop through every letter in message m to get the index
for i in m:
    if i == " ":
        newmessage.append(i)

    elif i in alphabet:
        currentposition = alphabet.index(i)
        #print(currentposition)
        newposition = currentposition + n
        #print(f"This is the new position {newposition}")
#use find method to get current positon of letter
        moduleposition = newposition % 26
        #print(f"This is the module position {moduleposition}")
        #newmessage.append(moduleposition)
        newmessage.append(alphabet[moduleposition])
#print(f"This is the new alphabet list {newmessage}")
    else:
        continue
encryptednote = "".join(newmessage)
print(encryptednote)

#make the decryption
