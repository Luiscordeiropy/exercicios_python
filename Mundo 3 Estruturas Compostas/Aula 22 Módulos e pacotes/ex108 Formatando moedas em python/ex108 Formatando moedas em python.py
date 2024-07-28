from moeda import *
p = float(input('Digite um número '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando em 10%, temos {moeda(aumentar(p, 10))} ')
print(f'Diminuindo em 13%, temos {moeda(diminuir(p, 13))}')
