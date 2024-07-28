def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita varias)
    :param sit:Valor opcional, indicando se deve ou não adicionar a situção
    :return: dicionário com varias informações sobre a situação da turma.
    '''
    d = dict()
    d['total'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['media'] = sum(num) / len(num)
    if sit:
        if d['media'] < 5:
            d['situaçao'] = 'péssimo'
        elif 5 <= d['media'] < 7:
            d['situaçao'] = 'ruim'
        else:
            d['situaçao'] = 'boa'
    return d


resp = notas(5, 6, 9, 1, 5, 4, 3, 4, sit=True)
print(resp)