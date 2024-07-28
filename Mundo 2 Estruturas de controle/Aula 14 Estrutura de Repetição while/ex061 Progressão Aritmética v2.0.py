termo = int(input('Digite o primeiro termo!'))
razao = int(input('Digite a razão!'))
p = termo
while p < termo+10*razao:
    print(p, end=' ')
    p += razao
