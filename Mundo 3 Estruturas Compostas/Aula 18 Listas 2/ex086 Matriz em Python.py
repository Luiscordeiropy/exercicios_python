matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for n in range(0, 3):
        matriz[c][n] = (int(input(f'Digite um valor para {c + 1, n + 1}: ')))
for c in range(0, 3):
    for n in range(0, 3):
        print(f'[ {matriz[c][n]} ]', end=' ')
    print()
