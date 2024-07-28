from random import sample
n1 = str(input('escreva um nome:'))
n2 = str(input('escreva outro nome:'))
n3 = str(input('escreva outro nome:'))
n4 = str(input('escreva outro nome:'))
lista = [n1, n2, n3, n4]
print('a ordem sorteada dos alunos é ')
print(sample(lista,4))