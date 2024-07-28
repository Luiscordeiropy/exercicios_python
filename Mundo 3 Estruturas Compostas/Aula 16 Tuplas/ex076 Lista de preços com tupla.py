lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
cont_lista = stop = 0
cont_preco = 1
for c in lista:
    print(f'{lista[cont_lista]:.<30}R${lista[cont_preco]:>7.2f}')
    cont_lista += 2
    cont_preco += 2
    stop += 1
    if stop == 9:
        break

