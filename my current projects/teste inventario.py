opcao = 0
dicop ={}
cont = 0
quant = 0
while opcao != 3:
    print('[1] == Adicionar item\n[2] == Remover item\n[3] == Sair')
    opcao = int(input('O que você deseja fazer:  '))
    if opcao == 1:
        cont += 1
        print('Qual item vc deseja adicionar? ')
        dicop[f'Item {cont}'] = input('Digite aqui:  ')
        print(f'Item {cont} adicionado com sucesso!')
        quant += 1
    if opcao == 2:
        if quant > 0:
            print('Qual item vc deseja remover?')
            delete = input('Digite aqui:  ')
            del dicop[delete]
            print(f'{delete} removido com sucesso!')
        else:
            print('N existe nenhum item no inventario para remover!\nTente outra coisa')
            continue
    if opcao == 3:
        continue
print('Você saiu')
print(f'Esses são seus items:\n{dicop}')