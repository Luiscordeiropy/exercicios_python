pessoas = list()
idade = list()
while True:
    lista = list()
    lista.append(str(input('Digite seu nome: ')))
    lista.append(int(input('Digite seu peso: ')))
    idade.append(lista[1])
    pessoas.append(lista[:])
    sn = str(input('Quer continuar? [S/N]'))
    if sn in 'Nn':
        break
maior = max(idade)
menor = min(idade)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for nome, peso in pessoas:
    if peso == maior:
        print(nome, end=' ')
print(f'\nO menor peso foi de {menor}Kg. peso de', end=' ')
for nome, peso in pessoas:
    if peso == menor:
        print(nome, end=' ')
