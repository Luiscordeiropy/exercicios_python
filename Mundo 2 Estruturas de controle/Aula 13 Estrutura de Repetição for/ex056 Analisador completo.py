media = homemv = idade1 = 0
nome1 = ''
for p in range(1, 5):
    print('-'*5,'{}° PESSOA'.format(p), 5*'-')
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('SEXO [M/F]:')
    media += idade / 4
    if sexo in 'Mm'and p == 1:
        homemv = idade
        nome1 = nome
    if idade > homemv:
        homemv = idade
        nome1 = nome
    if sexo in 'Ff' and idade < 20:
        idade1 += 1
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(homemv, nome1))
print('Ao todo são {} mulheres com menos de 20 anos'.format(idade1))