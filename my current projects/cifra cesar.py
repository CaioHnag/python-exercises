frase = str (input('Digite aqui :  ')).lower()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
for letra in frase :
    if letra in alfabeto :
        a = alfabeto.find(letra)
        aa = (a+4)%26
        frase = frase.replace(letra , alfabeto[aa])
    elif letra in num :
        b = num.find(letra)
        bb = b+3
        frase = frase.replace(letra , num[bb] )
print(frase.capitalize())

