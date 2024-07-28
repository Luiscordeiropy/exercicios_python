from moeda import *
p = float(input('Digite um número '))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando em 10%, temos {aumentar(p, 10, True)} ')
print(f'Diminuindo em 13%, temos {diminuir(p, 13, True)}')
