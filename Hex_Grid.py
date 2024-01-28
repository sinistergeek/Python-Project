X_REPEAT = 19
Y_REPEAT = 12
for y in range(Y_REPEAT):
    for x in range(X_REPEAT):
        print(r'/ \_', end = '')
    print()
    for x in range(X_REPEAT):
        print(r'\_/',end='')
    print()
