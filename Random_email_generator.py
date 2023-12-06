import random
import string
import csv
import progessbar

def getcount():
    rownums = input("How many email address?:")
    try:
        rowint = int(rownums)
        return rowint

    except ValueError:
        print("Please enter an integer value")
        return getcount()


def makeEmail():
    extensions = ['com','net','org','gov']
    domains =['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier']
    finalext = extensions[random.randinit(0,len(extensions)-1)]
    finaldom = domains[random.randint(0,len(domains)-1)]
    accountlen = random.randint(1,20)

    finalacc = ''.join(random.choice(string.ascii_lowercase + string.digits)for _ in range(accountlen))
    finale = finalacc + "@" + finaldom + "." + finalext
    return finale
howmany = getcount()

counter = 0

emailarray = []
print("Creating email address..")
print("Progess")

prebar = progessbar.ProgessBar(maxval=int(howmany))
for i in prebar(range(howmany)):
    while counter < howmany:
        emailarray.append(str(makeEmail()))
        counter += 1
        prebar.update(i)

print("Creation completed.")
for i in emailarray:
    print(i)
