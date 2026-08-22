radar = {
   "EMB-100": {"distancia": 85.0, "velocidade": 750},
   "GOL-400": {"distancia": 250.0, "velocidade": 800}
}
alertas = {}
menor = [ 100 , '']
while True:
    print('Comandos\nAdicionar\nAlertas\nEmergências\nSair')
    comando = str(input('Digite o comando: ')).lower()
    while comando not in ['sair' , 'adicionar','alertas','emergências'] :
        print('Comandos\nAdicionar\nAlertas\nEmergências\nSair')
        comando = str(input('Digite os comandos possíveis , por favor: ')).lower()
    if comando == 'adicionar':
       try:
        nome = input('Digite o nome do voo:  ')
        distancia , velocidade = str(input('Digite aqui a distância e a velocidade do voo:  ')).split()
        distancia = float(distancia)
        while distancia > 500 or distancia < 0:
            distancia = float(input('Digite valores a taxa de captação do radar, (0 a 500):  '))
        velocidade = float(velocidade)
        radar[nome] = {'distancia' : distancia, 'velocidade' : velocidade}
        if distancia < 100:
            alertas[nome] = {'distancia' : distancia, 'velocidade' : velocidade}
       except ValueError:
           print('Valores invalidos')
           comando = 'adicionar'
    elif comando == 'alertas' :
        if not radar:
            print('Sem voos pertos')
        else:
            for item in alertas :
                print(f'{item} = {alertas[item]['velocidade']}km ')
    elif comando == 'emergências':
        if not radar:
            print('Sem voos pertos')
        else:
            for name in alertas:
                if alertas[name]['distancia'] < menor[0]:
                    menor = [name, alertas[name]['distancia'] ]
            print(f'{menor[0]} = {menor[1]}')
    else:
        break