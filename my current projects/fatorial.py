print('Digite qualquer número para saber sua fatorial.')
number = int(input('Número:  '))
original = number
fatorial = 1
loop = 0
while number > 0:
    fatorial *= number
    loop += 1
    if loop < original:
       print(f'{number} x', end= ' ')
    else:
        print(f'1 = {fatorial}')
    number -= 1