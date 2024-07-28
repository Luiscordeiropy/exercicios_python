matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna3 = 0
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para {c + 1, i + 1}: '))
        if matriz[c][i] % 2 == 0:
            soma_pares += matriz[c][i]
        if i == 2:
            soma_coluna3 += matriz[c][i]
print(*matriz, sep='\n')
# for c in range(0, 3):
#     for i in range(0, 3):
#         print(f'[ {matriz[c][i]} ]', end='')
#     print()
print(f'A soma de todos os valores pares digitados : {soma_pares}')
print(f'A soma de todos os valores digitados na coluna 3: {soma_coluna3}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')
