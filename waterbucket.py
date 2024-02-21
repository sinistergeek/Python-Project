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
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print('Good job! You solved it in',steps,'steps!')
            sys.exit()
    print('You can:')
    print('(F)ill the bucket')
    print('(E)mpty the bucket')
    print('(P)our one bucket into another')
    print('(Q)uit')
    while True:
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()
        if move in ('F','E','P'):
            break
        print('Enter F,E,P, or Q')
    while True:
        print('Select a bucket 8,5,3 or QUiT:')
        srcBucket = input('> ').upper()
        if srcBucket == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if srcBucket in ('8','5','3'):
            break
    if move == 'F':
        srcBucketSize = int(srcBucket)
        waterInBuckett[srcBucket] = srcBucketSize
        steps += 1
    elif move == 'E':
        waterInBucket[srcBucket] = 0
        steps += 1

