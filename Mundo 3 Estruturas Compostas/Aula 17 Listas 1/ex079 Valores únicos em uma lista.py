lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    c = str(input('Quer continuar? [S/N]')).upper().strip()
    if c in 'N':
        break
print(sorted(lista))
