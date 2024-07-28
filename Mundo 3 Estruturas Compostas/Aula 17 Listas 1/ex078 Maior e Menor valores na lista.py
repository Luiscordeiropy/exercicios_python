lista = list()
for cont in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {cont+1}: ')))
maior = max(lista)
menor = min(lista)
# lista1 = lista[:]
print(f'O maior número digitado foi {maior} nas posições ', end='')
# for n in lista1:
#         if n == maior:
#             print(lista1.index(maior)+1, end='... ')
#             lista1[lista1.index(maior)] -= 1
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor número digitado foi {menor} nas posções ', end='')
# for n in lista:
#         if n == menor:
#             print(lista.index(menor)+1, end='... ')
#             lista[lista.index(menor)] -= 1
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
