from random import randint
from time import sleep
mega_sena = []
print('', '-'*35, '\n         JOGA NA MEGA SENA\n', '-'*35)
jogos = int(input('Quantos jogos você quer gerar? '))
for n in range(0, jogos):
    lista = list()
    mega_sena.append(lista)
    for c in range(0, 6):
        l = randint(1, 60)
        if l not in lista:
            lista.append(l)
        else:
            lista.append(randint(l+1, 60)-2)
print('-='*4, f' SORTEANDO {jogos} JOGOS ', '-='*4)
for i, c in enumerate(mega_sena):
    sleep(1)
    print(f'jogo {i+1}: {c}')
