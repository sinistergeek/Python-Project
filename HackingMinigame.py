import random,sys
GARBAGE_CHARS = '~!@#$%^&*()_+={}[]|;:,.<>?/'
with open('sevenword.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()

def main():
    print('''
    Hacking Minigame, by sinistergeek Find the password in the couputer's money. You are given clues after each guess.For example, if the secret password is MONITOR but the player guess CONTAIN, the are given the hint that 2 out of 7 letters were correct, because both MONITOR and CONTAIN have the letter O and N as their 2 nd and 3rd letter. You get four guesses.''')
    input('Press Enter to begin...')
    gameWords = getWords()
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)
    print(computerMemory)
    for triesRemaining in range(4,0,-1):
        playerMove= askForPlayerGuess(gameWords,triesRemaining)
        if playerMove == secretPassword:
            print('ACCESS GRANTED')
            return
        else:
            numMatches = numMatchingLetters(secretPassword,playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries.Secret password was {}.'.format(secretPassword))

def getWords():
    secretPassword = random.choice(WORDS)
    words = [secretPassword]
    while len(words) < 3:
        randomWord = getOneExcept(words)
        if numMatchingLetters(secretPassword,randomWord) == 0:
            words.append(randomWord)

    for i in range(500):
        if len(words) == 5:
            break
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword,randomWord) == 3:
            words.append(randomWord)

    for i in range(500):
        if len(words) == 12:
            break
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword,randomWord) != 0:
            words.append(randomWord)

    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    if blocklist == None:
        blocklist = []
    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord

def numMatchingLetters(word1,word2):
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches

def getComputerMemoryString(words):
    linesWithWords = random.sample(range(16 * 2),len(words))
    memoryAddress = 16 * random.randint(0,4000)
    computerMemory = []
    nextWord = 0
    for lineNum in range(16):
