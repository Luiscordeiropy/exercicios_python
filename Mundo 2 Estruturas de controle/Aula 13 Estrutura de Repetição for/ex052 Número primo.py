num = 0
while True:
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end='')
            tot += 1
        else:
            print('\033[31m', end='')

    if tot == 2:
        print(f'\033[mO número {num} foi divisivel {tot} vezes')
        print('\033[32mÉ PRIMO\033[m')
    num += 1
