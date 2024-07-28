jogador = dict()
pessoas = list()
while True:
    print('-=' * 35)
    jogador['nome'] = str(input('Nome do jogador! '))
    jogador['jogos'] = int(input('Quantos jogos você jogou?'))
    gols = []
    for c in range(1, jogador['jogos'] + 1):
        gols.append(int(input(f'quantos gol você fez na {c}º partida?')))
    jogador['gols'] = gols
    pessoas.append(jogador.copy())
    while True:
        n = str(input('quer continuar? [S/N]'))
        if n in 'Nn':
            break
        if n not in 'NnSs':
            print('digite apenas "S" ou "N"')
        else:
            break
    if n in 'Nn':
        break
print('-=' * 35)
print('Cod  Nome       Gols       Total')
print('-'*40)
for e, v in enumerate(pessoas):
    print(f'  {e+1}  {pessoas[e]['nome']:<10}{pessoas[e]['gols']} {sum(pessoas[e]['gols']):>5}')
while True:
    print('-'*40)
    r = int(input('Mostrar o levantamento de qual jogador? (999 para parar)'))
    if r == 999:
        break
    if r > len(pessoas):
        print(f'ERRO! Não existe jogador com código {r}! Tente novamente')
    else:
        for c in range(1, len(pessoas)+1):
            if r == c:
                for e, g in enumerate(pessoas[r - 1]['gols']):
                    print(f'No jogo {e + 1} fez {g} gols')
print('<< VOLTE SEMPRE >>')
