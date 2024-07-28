from random import randint
print(f'Os valores sorteados foram:', end=' ')
maior = menor = 0
for c in range(1, 6):
    aleatorio = (randint(0, 9))
    print(aleatorio, end=' ')
    if c == 1 or maior > aleatorio:
        maior = aleatorio
    if c == 1 or menor < aleatorio:
        menor = aleatorio
print(f'\nO maior valor sorteado foi {maior}\nO menor valor sorteado foi {menor}')
