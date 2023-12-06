import random

def randChar(chars):
    ranChar = random.choice(char)
    return ranChar

def randomPass(chars,passLen):
    password=""
    for i in range(passLen):
        char =randChar(chars)
        password += char
        print(password)
        return password
