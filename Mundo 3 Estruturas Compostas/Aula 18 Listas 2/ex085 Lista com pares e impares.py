numeros = [list(), list()]
for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else: 
        numeros[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(numeros[0])} ')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])} ')
