from collections import defaultdict

dic = dict()
def cadastrar(dicionario):
    lista = []
    nome = input('Digite o nome do aluno: ').capitalize()
    for a in range(0 , 3):
        nota = float(input('Digite a nota do aluno: '))
        while nota > 10 or nota < 0:
            try:
                nota = float(input('O sistema de notas só aceita valores de 0 a 10: '))
            except ValueError:
                print('O sistema só aceita números')
        lista.append(nota)
    lista.append(round(sum(lista) / len(lista) , 2))
    dicionario[nome] = lista
def situacao(dicionario , nome):
    media = dicionario[nome][3]
    if media >= 7:
        return 'Aprovado'
    elif 7 > media >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'
def mostrarboletim(dicionario):
    for nome in dicionario:
        print(f'{nome} | {dicionario[nome][0:3]} | {dicionario[nome][3]}')
def estatistica(dicionario):
    totalturma = 0
    new2 = defaultdict(int)
    for nome in dicionario:
        totalturma += dicionario[nome][3]
    new = sorted(dicionario.items() , key = lambda item: item[1][3], reverse = True)
    for nome in new:
        if nome[1][3] >= 7:
            obs = 'Aprovado'
        elif 7 > nome[1][3] >= 5:
            obs = 'Recuperacão'
        else:
            obs = 'Reprovado'
        new2[obs] += 1
    print(f'Media geral da turma = {round(totalturma / len(dicionario) , 2 )}')
    print(f'Aluno com a maior media = {new[0][0]}\nAluno com a menor media = {new[-1][0]}')
    for nome in new2:
        print(f'{nome}s = {new2[nome]}')
while True:
    print('[ 1 ] Cadastrar alunos \n[ 2 ] Situação do aluno \n[ 3 ] Mostrar boletins \n[ 4 ] Estatísticas da turma\n[ 5 ] Sair')
    user = input('Digite aqui :  ')
    while user not in ['1', '2', '3', '4', '5']:
        user = input('Digite uma opção possível :  ')
    if user == '1':
        cadastrar(dic)
    elif user == '2':
        name = input('Digite o nome do aluno: ').capitalize()
        while name not in dic.keys() and name != 'Sair' :
            name = input('Aluno não encontrado , digite novamente ou digite Sair para sair: ').capitalize()
        if name != 'Sair':
            print(f'{name} = {situacao(dic, name)} ')
    elif user == '3':
        mostrarboletim(dic)
    elif user == '4':
        estatistica(dic)
    else:
        break
print('Programa finalizado com sucesso')