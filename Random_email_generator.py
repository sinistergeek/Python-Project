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

