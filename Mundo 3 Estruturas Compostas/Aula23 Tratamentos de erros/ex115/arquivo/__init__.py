lista = dict()
pessoas = list()


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def listagem(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao abrir o aquivo')
    else:
        print('-' * 50)
        print('PESSOAS CADASTRADAS'.center(50))
        print('-' * 50)
        for n in a:
            dado = n.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} \t {dado[1]:>5} anos')

    finally:
        a.close()


def adicionar(arq):
    while True:
        nome = str(input('nome: '))
        if nome == '' or nome in '1234567890':
            print('Digite um nome válido!')
            continue
        break
    while True:
        try:
            idade = int(input('idade:'))
        except:
            print('Digite uma idade válida!')
            continue
        break
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o aquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
