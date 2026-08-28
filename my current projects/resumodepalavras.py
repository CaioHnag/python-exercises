def cript(palavra):
    lista = []
    a = ''
    b = 0
    for letra in palavra:
        if letra != a :
                lista.append([a , b])
                a = letra
                b = 1
        else:
            b += 1
    lista.append([a , b])
    c = ''
    for nome , qt in lista[1:]:
        if nome == ' ':
            c += ' '
        else:
            c += nome
            c += str(qt)
    if len(c) < len(palavra):
        return c
    else:
        return palavra
