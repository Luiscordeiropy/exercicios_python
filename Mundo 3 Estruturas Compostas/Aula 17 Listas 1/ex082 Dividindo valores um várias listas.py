lista = list()
listapar = list()
listaimpar = list()
while True:
    l = (int(input('digite um número')))
    lista.append(l)
    if l % 2 == 0:
        listapar.append(l)
    else:
        listaimpar.append(l)
    sn = str(input('Você quer continuar?(S/N)'))
    if sn in 'Nn':
        break
print(f'Sua lista é {lista}\nSua lista só com os pares{listapar}\nSua lista so com impar{listaimpar}')