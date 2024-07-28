extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
numero_entre = int(input('Digite um número entre 0 e 20: '))
while numero_entre < 0 or numero_entre > 20:
    numero_entre = int(input('Por favor digite um número entre 0 e 20!'))
print(f'você digitou o número {extenso[numero_entre]}')
