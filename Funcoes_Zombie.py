#FUNÇÃO PARA DEFINIR A QUANTIDADE DE JOGADORES
def quantJogadores():
    while True:
        x = int(input('\033[1;31m QUAL A QUANTIDADE DE JOGADORES? (min: 2) :\033[m'))
        if x < 2:
            print('Quantidade insuficiente de jogadores')
        else:
            break
    return x

#FUNÇÃO PARA INICIALIZAR OS DADOS NO COPO
def inserirCopo():
    copo = []
    for i in range(0, 6):
        copo.append('CPCTPC')
    for i in range(0, 4):
        copo.append('TPCTPC')
    for i in range(0, 3):
        copo.append('TPTCPT')
    return copo


#FUNÇÃO PARA PEGAR OS DADOS
def pegaDado(lista):
    from random import randint
    faceSorteada = []
    for d in range(1, 4):
        numSorteado = randint(0, len(lista))  # sorteia um numero de 0 a 12
        dadoSorteado = lista[numSorteado - 1]

        if 'CPCTPC' in dadoSorteado:
            corDado = '\033[32mDado Verde\033[m'
            faceSorteada.append('CPCTPC')

        if 'TPCTPC' in dadoSorteado:
            corDado = '\033[33mDado Amarelo\033[m'
            faceSorteada.append('TPCTPC')

        if 'TPTCPT' in dadoSorteado:
            corDado = '\033[31mDado Vermelho\033[m'
            faceSorteada.append('TPTCPT')

        print(f'{d}º Dado Sorteado: {corDado}')
    return faceSorteada


# FUNÇÃO PARA REMOVER OS DADOS DO COPO
def delDado(x, y):
        if 'CPCTPC' in y:
            del x[x.index('CPCTPC')]

        if 'TPCTPC' in y:
            del x[x.index('TPCTPC')]

        if 'TPTCPT' in y:
            del x[x.index('TPTCPT')]


#FUNÇÃO PARA APRESENTAR A PONTUAÇÃO DO JOGO
def pontuacao(x):

    print('      PLACAR DO JOGO        ')

    print('-'*26)
    print('\033[33mJOGADOR\033[m        \033[31mCEREBROS\033[m')
    print('-' * 26)
    for p in x:
        print(f'{p[0]}                {p[1]}')
    print('-' * 26)
    print('')

#FUNÇÃO PARA DEFINIR VENCEDOR
def vencedor(x):
    from time import sleep
    for v in range(0, len(x)):
        if v == 0:
            pontos = x[0][1]
            vencedor = x[0][0]
        elif x[v][1] > pontos:
            pontos = x[v][1]
            vencedor = x[v][0]
    print('O VENCEDOR FOI...')
    sleep(0.5)
    print(f'    \033[33m{vencedor}\033[m')


#FUNÇÃO PARA VERIFICAR SE O JOGADOR DESEJA PARAR OU CONTINUAR O TURNO
def continuar():
    while True:
        x = str(input('\033[32mVoce deseja continuar jogando os dados?(s=sim / n=não)\033[m'))
        if x not in 'SsNn':
            print('\n Valor incorreto digite novamente...')
        else:
            break
    return x

#FUNÇÃO PARA CONTAR OS DADOS DO COPO
def contaDados(x):
    print(f'''\033[32mO Copo contém:\033[m {len(x)} \033[32mdados\033[m
    {x.count("CPCTPC")} dados \033[32mVerdes\033[m
    {x.count("TPCTPC")} dados \033[33mAmarelos\033[m
    {x.count("TPTCPT")} dados \033[31mVermelhos\033[m''')







