import random

print("Number guessing Game")
number = random.randint(1,9)
chances=0
print("Guess a number(between 1 and 9)")

while True:
    guess = int(input())
    if guess == number:
        print(f'COngurATION! YOU HAVe GUeSS THE NUMBER {number} IN {chances} ATTEMPTs!')
        break

    elif guess < number:
        print("Your guess was too low: Guess a number high than",guess)
    else:
        print("Your guess was too hight: Guess a number lower than",guess)
chances  += 1
