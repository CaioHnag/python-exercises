from random import randint
from time import sleep
inventario = [['Espada Curta' , 1 , 10] , ['Poção Cura' , 3 , 5 ]]
nome , qt , efeito = inventario[1]
life = ['Armadura leve' , 10 , 20 ]
nomearmadura , ca , hp = life
hp += ca
mortovivo = [ 15 , 5 ]
hpm , dn = mortovivo
def atacar( qtdamage ) :
    a = randint(1 , qtdamage)
    return a
def curar (vida , qtpottion , qthealth) :
    a = qthealth * qtpottion
    b = vida + a
    return b
def chester (lista) :
    for name , qnt , efect in lista :
        print(f'Name = {name} - Qt = {qnt} - Efect = {efect}')
def inimigovida(danouser , vidainimigo) :
    a = vidainimigo - danouser
    return a
def critico (num) :
    a = randint(1 , num)
    return a
print('Olá player,vamos começar a jornada ?  ')
op = str(input('Digite aqui,[S/N] :   ')).strip().upper()[0]
while op not in 'SN' :
    op = str(input('Digite sim ou não , por favor :  ')).strip().upper()[0]
if op == 'S' :
    print(f'Esses são seus atributos :\nHp = {hp} ' , end = ' ')
    print(f'Dano = {inventario[0][2]}')
    print('Inventario: ')
    chester(inventario)
    op = str(input('Deseja fazer um tutorial , [S/N] ?  ')).strip().upper()[0]
    while op not in 'SN' :
        op = str(input('Digite sim ou não, por favor:   ')).strip().upper()[0]
    if op == 'S' :
        print('Então um morto-vivo aparece na sua frente')
        while hpm > 0 and hp > 0 :
            print(f'Atacar [1] : {inventario[0][2]}    Curar-se [2] = {inventario[1][2]}')
            user = int(input('Oque deseja fazer : '))
            while user not in [1,2] :
                print(f'Atacar [1] : {inventario[0][2]}    Curar-se [2] = {inventario[1][2]}')
                user = int(input('Digite um número entre 1 e 2 : '))
            if user == 1 :
                d = atacar(inventario[0][2])
                critic = critico(20)
                if critic >= 15 :
                    d = d * 2
                    print('Você ganhou um bônus de crítico , o seu dano foi dobrado.')
                hpm -= d
                mortovivo[0] = hpm
                sleep(1)
                print(f'Você deu = {d} de dano.')
                if hpm <= 0 :
                    sleep(1)
                    print(f'A vida do morto-vivo zerou , você o matou.')
                    break
                else:
                    sleep(1)
                    print(f'A vida do morto-vivo agora é {hpm}.')
            elif user == 2 :
                if qt > 0:
                    if qt != 1 or qt != -1 :
                        sleep(1)
                        print(f'Você tem {qt} {nome} , em seu inventário.')
                        d = int(input('Quantas você quer usar ? '))
                    else:
                        sleep(1)
                        print(f'Você tem {qt} Poção de cura , em seu inventário.')
                        d = int(input('Quantas você quer usar ? '))
                    while d < 0 or d > qt :
                        d = int(input('Digite um valor entre os possíveis, por favor? '))
                    hp = curar(hp , d , efeito)
                    life[2] = hp
                    qt -= d
                    inventario[1][1] = qt
                    sleep(1)
                    print(f'Você curou {d*efeito}.')
                    print(f'Hp = {hp}')
                else:
                    print('Você não tem poções o suficiente.')
                    continue
            sleep(1)
            print('Agora é o turno do morto-vivo !')
            sleep(1)
            d = atacar(dn)
            critic = critico(20)
            if critic >= 15 :
                d = d * 2
                print('O boss tirou um bônus de crítico, o dano dado por ele foi dobrado.')
            print(f'Ele te atacou\nDano Causado = {d}')
            hp -= d
            life[2] = hp
            print(f'Hp = {hp}')
            if hp <= 0 :
                print('Você morreu!!')
else :
    print('Está tudo certo,quando estiver pronto volte.')
if hpm <= 0 :
    print('O morto vivo doprou um item.')
    us = str(input('Deseja pegar, [S/N] ?  ')).strip().upper()[0]
    while us not in 'SN' :
        us = str(input('Digite sim ou não , por favor :  ')).strip().upper()[0]
    if us == 'S' :
        print('Ele doprou 100 moedas')
        sleep(1)
        print('Moeda em seu inventário')
        inventario.append([ 'Moeda' , 100 ])
print('Obrigado por jogar este teste.')