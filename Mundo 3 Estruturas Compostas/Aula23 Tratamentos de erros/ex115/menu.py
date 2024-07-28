from interface import *
from arquivo import *

arq = 'ex115menu.txt'
if not arquivoExiste(arq):
    criarAquivo(arq)

while True:
    menu(['Pessoas cadastradas', 'cadastrar nova pessoa', 'terminar programa'])
    while True:
        resposta = leiaint('Sua opção: ')
        if resposta == 1:
            listagem(arq)
            break
        elif resposta == 2:
            cabeçalho('NOVO CADASTRO')
            adicionar(arq)
            break
        elif resposta == 3:
            cabeçalho('Opção 3')
            print('Saindo do sistema... até logo!')
            break
        else:
            print('\033[31mDigite um número que esteja na tabela!\033[m')
    sleep(2)
    if resposta == 3:
        break
