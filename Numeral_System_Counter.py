print('''
Numeral System Counters
      This program shows you equivalent numbers in decimal(base 10),hexadecimal(base 16), and binary(base 2) numeral systems.
      (Ctrl-C to quit.)
      ''')

while True:
    response = input('Enter the starting number (e.g. 0) >')
    if response == '':
        response = '0'
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display(e.g. 1000) > ')
    if response == '':
        response = '1000'
        break

    if response.isdeciaml():
        break
    print('Please enter a number.')
amount = int(response)

for number in range(start, start + amount):
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC:',number,'   HEX:',hexNumber,'   BIN:',binNumber)
