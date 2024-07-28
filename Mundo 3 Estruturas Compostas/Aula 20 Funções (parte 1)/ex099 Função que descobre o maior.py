def maior(*num):
    cont = maior = 0
    while True:
        for c in num:
            if cont == 0 or c > maior:
                maior = c
            cont += 1
        print('-='*25)
        print(f'analisando os valores passados...')
        print(f'{num} foram informados {len(num)} valores ao todo.')
        print(f'o maior valor informado foi {maior}')
        break


maior(1, 5, 6, 8, 1, 5)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
