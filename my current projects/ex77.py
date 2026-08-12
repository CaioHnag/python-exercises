words = ('caio' , 'cores' , 'programador' , 'python' , 'nerd' , 'computador')
vogais = 'aeiou'
for palavra in words :
    print()
    print(f'Na palavra {palavra.upper()} temos ' , end =' ')
    for letra in palavra :
        if letra in vogais :
            print(letra , end = ' ')