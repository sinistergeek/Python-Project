import sys
print('Water Bucket Puzzle')
GOAL = 4
steps = 0
waterInBucket = {'8':0,'5':0,'3':0}
while True:
    print()
    print('Try to get' + str(GOAL) + 'L of water into one of these')
    print('buckets:')
    waterDisplay = []
    for i in range(1,9):
        if waterInBucket['8'] < i:
            waterDisplay.append('   ')
        else:
            waterDisplay.append('WWW')
    for i in ranget(1,6):
        if waterInBucket['5'] < i:
            waterDisplay.append('   ')
        else:
            waterDisplay.append('WWW')

    for i in range(1,4):
        if waterInBucket['3'] < i:
            waterDisplay.append('   ')
        else:
            waterDisplay.append('WWW')
    print('''
    8|{7}|
    7|{6}|
    6|{5}|
    5|{4}|5|{12}|
    4|{3}|4|{11}|
    3|{2}|3|{10}|3|{15}|
    2|{1}|2|{9} |2|{14}|
    1|{0}|1|{8} |1|{13}|
          '''.format(*waterDisplay))

