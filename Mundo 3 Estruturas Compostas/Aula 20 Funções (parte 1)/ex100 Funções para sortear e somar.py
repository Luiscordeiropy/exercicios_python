from random import randint
from time import sleep


def sorteia():
    print('Sorteando os valores: ', end='')
    for c in range(1, 6):
        r = randint(0, 10)
        numeros.append(r)
        print(r, end=' ')
        sleep(0.5)
    print('Pronto!')


def somaPar(txt):
    soma = 0
    for c in txt:
        if c % 2 == 0:
            soma += c
    print(f'somando os valores pares de {numeros}, temos {soma}')


numeros = list()
sorteia()
somaPar(numeros)
