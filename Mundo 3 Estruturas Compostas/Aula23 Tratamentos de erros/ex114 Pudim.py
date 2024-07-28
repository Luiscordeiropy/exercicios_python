import urllib.request

def verifica_conexao(url):
    try:
        site = urllib.request.urlopen(url)
        print('\n', site.read())
        return True
    except:
        return False

# Exemplo de uso
url = 'http://www.google.com'
if verifica_conexao(url):
    print('A página está acessível.')
else:
    print('A página não está acessível.')