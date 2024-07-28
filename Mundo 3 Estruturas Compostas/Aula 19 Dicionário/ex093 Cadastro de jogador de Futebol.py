jogador = {'nome': str(input('Escreva seu nome: '))}
jogos = int(input('Quantos jogos você jogou? '))
gols = list()
jogador['gols'] = gols
for c in range(1, jogos + 1):
    j = int(input(f'Na partida {c}, quantos gols você fez? '))
    gols.append(j)
jogador['total'] = sum(gols)
print(jogador)
for k, v in jogador.items():
    print(f'{k} = {v}')
for e, v in enumerate(jogador['gols']):
    print(f'Na partida {e + 1}, fez {v} gols')
