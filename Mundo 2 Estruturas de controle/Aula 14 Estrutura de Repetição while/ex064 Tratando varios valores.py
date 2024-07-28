n = 0
n1 = -1
n2 = -999
print(('\033[35mDigite varios números para somalos(Digite "999" para terminar o programa)'))
while n != 999:
    n = int(input('Digite'))
    n1 += 1
    n2 += n
print('você digitou {} NÚMEROS e a soma entre eles foi {}'.format(n1, n2))
