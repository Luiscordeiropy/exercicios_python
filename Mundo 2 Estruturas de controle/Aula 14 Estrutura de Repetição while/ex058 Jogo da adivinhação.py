from random import randint
n = randint(0,10)
p = ''
p1 = 0
print('\033[0;35mVou pensar em um número de 0 a 10, tente advinhar!\033[m')
while p != n:
    p = int(input('\033[32mDigite um número!\033[m'))
    p1 += 1
    if p < n:
        print('\033[31mmais... tente mais uma vez!\033[m')
    elif p > n:
        print('\033[31mmenos... tente mais uma vez!\033[m')
print('\033[32mVocê finalmente acertou! Você teve {} tentativas!\033[m'.format(p1))