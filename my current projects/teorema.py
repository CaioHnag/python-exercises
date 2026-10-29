import math
def validar():
    i = str(input('Deseja saber o resultado? [S/N]')).upper().strip()[0]
    while i not in 'SN':
        i = str(input('Valor invalido , digite sim ou não ? [S/N]')).upper().strip()[0]
    return i
def mostrartriangulo(catetoop , catetoad , hipote):
    lista = [catetoop ,catetoad ,hipote]
    if sum(lista) == 0:
        print(f'''
                                   /|
                                  / |
                                 /  |
                          c <-  /   | -> a
                               /    |
                              /     |
                             /______| 
                                |
                                v
                                b''')
    else:
      print(f'''
                 /|
                / |
               /  |
  {hipote}      <- /   | -> {catetoop}
             /    |
            /     |
           /______| 
              |
              v
             {catetoad}''')
print('\033[1;34m-=\033[m'*20)
print('TEOREMA DE PITAGORAS')
print('\033[1;34m-=\033[m'*20)
a = '0'
b = '0'
c = '0'
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cond = 0
while True :
    print('[ 1 ] ACHAR HIPOTENUSA \n[ 2 ] ACHAR CATETO OPOSTO \n[ 3 ] ACHAR CATETO ADJACENTE\n[ 4 ] ACHAR O TIPO DE CONTA ')
    opcao = input('Digite aqui sua escolha :  ').strip()
    while opcao not in '1234':
        opcao = input('Digite aqui sua escolha :  ').strip()
    if opcao == '4':
        mostrartriangulo(0 , 0 , 0)
        print('OBSERVER O TRIANGULO E DIGA OS VALORES DE ACORDO COM O CALCULO PROPOSTO NO SEU LIVRO , CADERNO OU PAPEL')
        a = input('Digite aqui seu a :  ').upper().strip()[0]
        b = input('Digite aqui seu b : ').strip().upper()[0]
        c = input('Digite aqui seu c : ').strip().upper()[0]
        if c in alfabeto :
            print('Sua expressão é para achar a hipotenusa')
            user = validar()
            if user == 'S':
                a = float(a)
                b = float(b)
                c = 0
                cond += 1
                opcao = '1'
        elif a in alfabeto :
            print('Sua conta é para achar o cateto oposto')
            user = validar()
            if user == 'S':
                a = 0
                b = float(b)
                c = float(c)
                cond += 1
                opcao = '2'
        elif b in alfabeto :
            print('Sua conta é para achar o cateto adjacente')
            user = validar()
            if user == 'S':
                a = float(a)
                b = 0
                c = float(c)
                cond += 1
                opcao = '3'
    if opcao == '1' :
        if cond < 1 :
            a = float(input('Digite o valor do cateto oposto :  '))
            b = float(input('Digite o valor do cateto adjacente :  '))
        c = round(math.hypot(a, b) , 2)
        print(f'Sua Hipotenusa é {c}')
        mostrartriangulo(a , b , c)
        cond = 0
    elif opcao == '2' :
        if cond < 1 :
            b = float(input('Digite o valor do cateto adjacente :  '))
            c = float(input('Digite o valor da hipotenusa :  '))
        a = round(math.sqrt(math.pow(max(b , c), 2) - math.pow( min (c  , b), 2)) , 2 )
        print(f'Seu cateto oposto é {a}')
        mostrartriangulo(a , b , c)
        cond = 0
    elif opcao == '3':
        if cond < 1:
            a = float(input('Digite o valor do cateto oposto :  '))
            c = float(input('Digite o valor da hipotenusa :  '))
        b = round(math.sqrt(math.pow(max( a , c ),2) - math.pow(min( a , c ) , 2)) , 2)
        print(f'Seu cateto adjacente é {b}')
        mostrartriangulo(a , b , c)
        cond = 0
    op = input('Deseja continuar ? [S/N]').strip().upper()[0]
    while op not in 'SN':
        op = input('Digite aqui sua escolha :  ').strip().upper()[0]
    if op == 'N':
        break
print('Obrigado por usar o meu programa')
