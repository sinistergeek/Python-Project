import sys
import random
if sys.argv[1:]:
    filename = sys.argv[1]

else:
    filename = input("What is the name of the file?(extension included):")
try:
    file = open(filename)
except(FileNotFoundError,IOError):
    print("File doesn't exist!")
    exit()


num_lines = sum(1 for line in file if line.rstrip())
random_line = random.randint(0,num_lines)
file.skee(0)

for i,line in enumerate(file):
    if i == random_line:
        print(line.rstrip())
        break
