pessoa = dict()
galera = list()
media = 0
while True:
    pessoa['nome'] = str(input('Escreva seu nome!'))
    pessoa['sexo'] = str(input('Qual o seu sexo? [M/F] ')).upper()
    pessoa['idade'] = int(input('Quantos anos você tem?'))
    media += pessoa['idade']
    galera.append(pessoa.copy())
    co = str(input('Você quer continuar?'))
    if co in 'Nn':
        break
print(f'A) O total de pessoas cadastradas foi: {len(galera)}')
print(f'B) A media de idade do grupo é {media / len(galera)}')
print('C) Lista só com mulheres ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=' ')
print('\nD) Lista com todas as pessoas com idade acima da média')
for p in galera:
    if p['idade'] > media / len(galera):
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
