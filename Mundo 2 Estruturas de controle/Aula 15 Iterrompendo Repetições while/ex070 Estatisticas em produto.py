p = contp = contn = menor = 0
nomemenor =''
print('\033[32m-=\033[m'* 30)
print('LISTA DE COMPRAS')
print('\033[32m-=\033[m'* 30)
while True:
    nome = str(input('Qual o nome do produto?'))
    preco = int(input('Qual o preço do produto'))
    p += preco
    c = 0
    contn += 1
    if preco > 1000:
        contp += 1
    if contn == 1 or preco < menor:
        menor = preco
        nomemenor = nome
    while c != 'S' and c != 'N':
        c = str(input('Quer continuar?[S/N]')).upper()[0]
    if c in 'N':
        break
print(f'O total da compra foi de {p}.\nTemos {contp} produtos custando mais de R$1000.\nO produto mais barato foi a {nomemenor} que custa R${menor} ')