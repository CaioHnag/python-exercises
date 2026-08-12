print("-=" * 15)
print("Par ou Impar")
print("-=" * 15)
cont = 0
while True:
    computador = 0
    soma = 0
    num = 0
    print('Escolha Impar ou Par')
    user = str(input("Escolha aqui: ")).strip().upper()[0]
    while user not in 'PI':
        user = str(input("Escolha aqui: ")).strip().upper()[0]
    if user == 'I':
        print("Então eu sou Par")
        print('Agora então escolha um número.')
        num = int(input('Digite aqui: '))
        while num > 11 or num < 0:
            num = int(input('Número fora dos limites:   '))
        computador = randint(0, 10)
        soma = num + computador
        if soma % 2 == 0:
            print(f'Eu escolhi {computador}')
            sleep(1)
            print(f'Voce perdeu a soma deu {soma}')
            break
        else:
            print(f'Eu escolhi {computador}')
            print(f"Voce ganhou parabéns , a soma deu {soma}")
            cont += 1
# aqui se o if der True ele irá descosiderar este else de baixo
    else:
        print('Então eu sou Impar')
        print('Agora então escolha um número.')
        num = int(input('Digite aqui: '))
        while num > 11 or num < 0:
            num = int(input('Número fora dos limites: '))
        computador = randint(0, 10)
        soma = num + computador
        if soma % 3 == 0:
            print(f'Eu escolhi {computador}')
            sleep(1)
            print(f'Voce perdeu a soma deu {soma}')
            break
        else:
            print(f'Eu escolhi {computador}')
            print(f"Voce ganhou parabéns , a soma deu {soma}")
            cont += 1
print(f'Você ganhou {cont} vezes')