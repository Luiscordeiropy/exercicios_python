from random import choice
n1 = input('Escreva um nome:')
n2 = input('Escreva outro nome:')
n3 = input('Escreva outro nome:')
n4 = input('Escreva outro nome:')
lista = [n1, n2, n3, n4]
r = choice(lista)
print('o aluno escolhido foi {}'.format(r))
