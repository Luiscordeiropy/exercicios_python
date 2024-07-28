from random import randint
from time import sleep
p = int(input('Vou pensar em um número de 0 a 5. Tente adivinhar :'))
n = randint(0, 5)
print('PROCESSANDO', end='')
for i in range(3):
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
print('')
if p == n:
    print('Você venceu! PARABÉNS!')
else:
    print('Eu pensei em {}. Você perdeu, OTÁRIO!'.format(n))
