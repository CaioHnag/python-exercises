def mostra(palavras):
    for letra in palavras:
        print(letra , end = ' - ')
def verificar( p1 , p2 ):
    cont = -1
    contp = 0
    for letra in p1:
        cont += 1
        if letra == p2[ cont ] :
            contp += 1
    if contp == len(p2) :
        return True
    return False
def verificar2( lista1 , lista2 , letra):
    cont = -1
    for letrass in lista1:
        cont += 1
        if letrass == letra :
            lista2[cont] = letra
    return lista2
def qtletras(lista):
    alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cont = 0
    for lt in lista:
        if lt in alfa:
            cont += 1
    return cont
op = 'S'
while op == 'S':
    player = str(input('Digite a palavra: ')).upper()
    tentativas = 9
    pl = []
    palpite = []
    for letras in player:
        pl.append(letras)
        palpite.append('_')
    print('Adivinhe a palavra: ')
    while tentativas > 0:
        print(' - '.join(palpite))
        jogador = str(input('Digite uma letra: ')).upper().strip()[0]
        while jogador not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            jogador = str(input('Digite uma letra: ')).upper().strip()[0]
        tentativas -= 1
        verificar2(pl , palpite , jogador)
        if verificar(pl, palpite):
            print('Você acertou!')
            print(f'A palavra era {''.join(pl)}')
            op = str(input('Deseja jogar de novo? [S/N] ')).upper()[0]
            while op not in 'SN':
                op = str(input('Digite sim ou não , por favor:  ')).upper()[0]
            break
        if tentativas == 0:
            print('Você perdeu!!')
            op = str(input('Deseja jogar de novo? [S/N] ')).upper()[0]
            while op not in 'SN':
                op = str(input('Digite sim ou não , por favor:  ')).upper()[0]
            break
        if qtletras(palpite) > 1:
            print(f'Você acertou ,{qtletras(palpite)} letras')
        elif qtletras(palpite) == 1:
            print(f'Você acertou ,{qtletras(palpite)} letra')
        else:
            print('Você não acertou nenhuma letra')
        if tentativas != 1:
            print(f'Você ainda tem {tentativas} tentativas')
        else:
            print(f'Você ainda tem {tentativas} tentativa')
