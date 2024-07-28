from random import choice
j = input('Escolha Pedra, Papel ou Tesoura').strip().upper()
m = ['PEDRA', 'PAPEL', 'TESOURA']
a = choice(m)
if j == 'PEDRA' and a == 'TESOURA':
    print('Você ganhou! Escolhi {}'.format(a))
if j == 'PAPEL' and a == 'PEDRA':
    print('Você ganhou! Escolhi {}'.format(a))
if j == 'TESOURA' and a == 'PAPEL':
    print('você ganhou! Escolhi {}'.format(a))
if j == 'PEDRA' and a == 'PAPEL':
    print('Você perdeu! Escolhi {}'.format(a))
if j == 'PAPEL' and a == 'TESOURA':
    print('Você perdeu! Escolhi {}'.format(a))
if j == 'TESOURA' and a == 'PEDRA':
    print('Você perdeu! Escolhi {}'.format(a))
if j == a:
    print('Empatou! Escolhi {}'.format(a))
