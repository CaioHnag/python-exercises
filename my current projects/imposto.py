lista=[1500,1111,900,1000,5000,500,7000]
impostoa=0.1
impostob=0.15
vf=0
for numero in lista:
    if numero>1000:
        a=numero*impostob
        b=numero+a
        print(f'VALOR ORIGINAL = R${numero}')
        print(f'O VALOR DO IMPOSTO= R${a}\n VALOR FINAL=R${b}')
    else:
        a=numero*impostoa
        b=numero+a
        print(f'VALOR ORIGINAL = R${numero}')
        print(f'VALOR DO IMPOSTO=R${a}\n VALOR A PAGAR= R${b}')
    vf+=a #poderiamos ter feito como vf=vf+a
print(f'soma de imposto:R${vf}')