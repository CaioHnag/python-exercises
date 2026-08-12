estoque = (( 4325 ,'Camisa' , 50) , (5467 , 'Oculos', 10) , (6891 , 'Calça' , 35) , (7962 , 'Casaco' , 25))
op = 's'
while op == 's' :
    user = int(input('Digite o codigo do produto :'))
    for cod , nome , qt in estoque:
        if user == cod :
            print(f'{cod} - {nome} - {qt}')
            op = str(input('Deseja continuar? ')).strip().lower()[0]
            while op not in 'sn' :
                op = str(input('Digite sim ou não , por favor :  '))
            break
        else:
            print(f'produto {user} não encontrado')
            op = str(input('Deseja continuar')).strip().lower()[0]
            while op not in 'sn':
                op = str(input('Digite sim ou não , por favor :  ')).strip().lower()[0]
            break


