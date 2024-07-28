from math import factorial
n = int(input('digite um número!'))
c = n
print('{}! = '.format(c),end='')
for c in range(1, n):
    print('{}x'.format(c), end='')
    if c == n-1:
        print('{} = {}'.format(n,factorial(n)))