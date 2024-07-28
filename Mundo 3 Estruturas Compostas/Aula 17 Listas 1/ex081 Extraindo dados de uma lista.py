lista = list()
while True:
    lista.append(int(input('Digite um valor')))
    sn = str(input('Quer continuar? [S/N]')).upper()
    if sn in 'N':
        break
print(f'{len(lista)} números foram digitados')
lista.sort(reverse=True)
print(f'A lista de forma decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e esta na lista')
else:
    print('O valor 5 nao foi digitado e não esta na lista')
