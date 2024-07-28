from random import randint
jogadores = dict()
print('-='*5, 'Valores sorteados', '-='*5)
for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(0, 6)
for j in jogadores.items():
    print(f'O {j[0]} tirou {j[1]}')
print('-='*5, 'Ranking dos jogadores', '-='*5)
ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
for e, n in enumerate(ranking.items()):
    print(f'{e + 1}º lugar: {n[0]} com {n[1]}')
