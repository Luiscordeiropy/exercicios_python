sacar = int(input('Qual é o valor a ser sacado?'))
onca = macaco = macaco1 = arara = arara1 = moeda = moeda1 = 0
if sacar >= 50:
    onca = sacar // 50
    macaco = sacar % 50
    arara = macaco % 20
    moeda = arara % 10
    if macaco >= 20:
        macaco1 = macaco // 20
        arara = macaco % 20
        if arara >= 10:
            arara1 = arara // 10
            moeda = arara % 10
            if moeda >= 1:
                moeda1 = moeda // 1
    if arara >= 10:
        arara1 = arara // 10
        moeda = arara % 10
        if moeda >= 1:
            moeda1 = moeda // 1
    if moeda >= 1:
        moeda1 = moeda // 1
elif sacar >= 20:
    macaco1 = sacar // 20
    arara = sacar % 20
    moeda = arara // 1
    if arara >= 10:
        arara1 = arara // 10
        moeda = arara % 10
        if moeda >= 1:
            moeda1 = moeda // 1
    if moeda >= 1:
        moeda1 = moeda // 1
elif sacar >= 10:
    arara1 = sacar // 10
    moeda = sacar % 10
    if moeda >= 1:
        moeda1 = moeda // 1
elif sacar >= 1:
    moeda1 = sacar //1
if onca >= 1:
    print(f'Total de {onca} cédulas de R$50')
if macaco1 >= 1:
    print(f'Total de {macaco1} cédulas de R$20')
if arara1 >= 1:
    print(f'totol de {arara1} cédulas de R$10')
if moeda1 >= 1:
    print(f'Total de {moeda1} cédulas de R$1')
print(onca, macaco1, arara1, moeda1)

# valor = int(input('Que valor você quer sacar? R$ '))
# cedulas = [50,20,10,1]
# for cedula in cedulas:
#     if valor > cedula or valor == cedula:
#         resultado = (valor//cedula)
#         valor %= cedula
#         print (f'Total de {resultado} cedulas de R$ {cedula}.')
