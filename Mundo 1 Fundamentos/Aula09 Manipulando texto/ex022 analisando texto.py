nome = str(input('Escreva seu nome:')).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
letras1 = len(nome) - nome.count(' ')
nome1 = nome.find(' ')
print('''Seu nome maiúsculo: {}\nSeu nome minúsculo: {}
Seu nome tem {} letras\nA primeira palavra do seu nome tem {} letras'''
      .format(maiuscula, minuscula, letras1, nome1))
