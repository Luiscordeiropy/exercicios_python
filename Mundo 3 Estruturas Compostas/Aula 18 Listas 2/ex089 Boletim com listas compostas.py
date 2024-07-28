alunos = []
cont = 0
while True:
    alunos.append([str(input('Nome: '))])
    alunos[cont].append([float(input('Nota 1: '))])
    alunos[cont][1].append(float(input('Nota 2: ')))
    sn = str(input('Quer continuar? (S/N)'))
    if sn in 'Nn':
        break
    cont += 1
print('N°  NOME           MÉDIA')
for c, a, in enumerate(alunos):
    print(f'{c + 1}   {a[0]:15}{(a[1][0] + a[1][1]) / 2}')
while True:
    nota = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if nota == 999:
        break
    print(alunos[nota-1][1])
