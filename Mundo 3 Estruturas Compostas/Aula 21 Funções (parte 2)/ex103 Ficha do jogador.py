def ficha(jogador, gols):
    if jogador in '':
        jogador = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: ')).strip()
ficha(jogador, gols)
