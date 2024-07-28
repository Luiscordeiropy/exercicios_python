aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['Média'] = int(input(f'Média de {aluno["nome"]}: '))
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['situação'] = 'Recuperando'
else:
    aluno['situação'] = 'Reprovado'
print('-'*35)
for n, m in aluno.items():
    print(f'{n} é igual a {m}')
