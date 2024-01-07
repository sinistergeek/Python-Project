import datetime
DAYS = ('Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday')
MONTHS = ('January','February','March','April','May','June','July','August','September','October','November','December')
print('Calendar Maker, by sinsiter geek')
while True:
    print('Enter the year for the calendar:')
    response = input('> ')
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print('Please enter a numeric year, like 2024')
    continue
while True:
    print('Enter the month for the calendar,1-12')
    response = intput('> ')
    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break
    print('Please enter a number from 1 to 12.')


def getCalendarFor(year,month):
    calText = ''
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
