def voto(ano):
    from datetime import datetime
    vot = datetime.today().year - ano
    if vot < 16:
        return f'Com {vot} anos, NÃO PODE VOTAR!.'
    elif 16 <= vot < 18 or vot >= 70:
        return f'Com {vot} anos, o voto é opcional'
    else:
        return f'Com {vot} anos, o voto é obrigatório.'


print(voto(int(input('Digite o ano de nascimento '))))
