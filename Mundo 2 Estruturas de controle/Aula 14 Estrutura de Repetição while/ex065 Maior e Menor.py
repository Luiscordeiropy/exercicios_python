q = ''
n1 = n2 = n3 = cont = maior = menor = 0
print('Digite N para terminar o programa!')
while q != 'N' and q != "n":
    n = int(input('Digite um valor'))
    n1 += 1
    n2 += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    q = input('Quer continuar?[S/N]').upper()
    if q == 'S':
        print(end='')
    elif q not in 'SN':
        print('tente novamente')
n3 = n2 / n1
print('A média dos valores digitados é {:.2f}. O maior valor é {}. O menor valor é {}'.format(n3, maior, menor))