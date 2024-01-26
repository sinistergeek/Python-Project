import random,sys
GARBAGE_CHARS = '~!@#$%^&*()_+={}[]|;:,.<>?/'
with open('sevenword.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()
