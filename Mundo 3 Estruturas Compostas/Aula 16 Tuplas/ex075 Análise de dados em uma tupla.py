lista = (int(input('Digite um valor:')), int(input('Digite um valor:')), int(input('Digite um valor:')), int(input('Digite um valor:')))
print(f'O número 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O número 3 apareceu na {lista.index(3)+1}° posição')
else:
    print('O número 3 não apareceu nenhuma vez!')
print('Os números pares são ', end='')
for n in lista:
    if n % 2 == 0:
        print(f'{n}', end=' ')

