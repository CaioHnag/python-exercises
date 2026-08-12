valorinicial = int(input('Digite o valor inicial:  '))
razao = int(input('Digite a razão da sua PA:  '))
qt = int(input('Quantos termos você quer saber:  '))
original = qt
while original > 0:
    if original == 1:
        print(f'\033[1;36m {valorinicial} \033[m ', end = ' ')
    else:
        print(f'{valorinicial}', end=' -> ')
    valorinicial += razao
    original -= 1