def main():
    print('Soroban - The japanese Abacus')
    print()
    abacusNumber = 0

    while True:
        displayAbacus(abacusNumber)
        displayControls()
        commands = input('> ')
        if commands == 'quit':
            break
        elif commands.isdecimal():
            abacusNumber = int(commands)
        else:
            for letters in commands:
                if letter == 'q':
                    abacusNumber += 100000000000000
                elif letter == 'a':
                    abacusNumber -= 10000000000000
                elif letter == 'w':
                    abacusNumber += 1000000000000
                elif letter == 's':
                    abacusNumber -= 100000000000
                elif letter == 'e':
                    abacusNumber += 10000000000
                elif letter == 'd':
                    abacusNumber -= 1000000000
                elif letter == 'r':
                    abacusNumber += 100000000
                elif letter == 'f':
                    abacusNumber -= 10000000
                elif letter == 't':
                    abacusNumber += 1000000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        if abacusNumber < 0:
            abacusNumber = 0:
        if abacusNumber > 999999999:
            abacusNumber = 999999999


