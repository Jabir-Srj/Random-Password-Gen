import random

# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''. join(tempList)

#Main prgram starts here
#Generates 2 random uppercase letters
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))

#Generates 2 random lowercase letters
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))

#Generates 2 random numbers
randomNumber1 = chr(random.randint(48, 57))
randomNumber2 = chr(random.randint(48, 57))

#Generates 2 random characters
randomCharacter1 = chr(random.randint(33, 152))
randomCharacter2 = chr(random.randint(33, 152))

#Any additions to the code may be added here

#Generate password using all the characters, in a random order
# You can add more stuff here
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + randomNumber1 + randomNumber2 + randomCharacter1 + randomCharacter2 + uppercaseLetter1 + lowercaseLetter1 +uppercaseLetter2 + lowercaseLetter2
password = shuffle(password)

#Output (the finale)
print(password)