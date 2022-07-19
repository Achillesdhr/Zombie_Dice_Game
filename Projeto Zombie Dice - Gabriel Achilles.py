# Nome: Gabriel Achilles da Silva. Curso: Tecnologia em Análise e Desenvolvimento de Sistemas

import Funcoes_Zombie

from time import sleep # Módulo importado, contem o comando sleep que define um tempo para o computador executar a proxima ação

print ('\033[1;31m Olá Zumbis, Bem vindos ao jogo. \033[m\n') # Mensagem inicial do jogo
sleep(1) #comando para esperar 1 segundo

## Definindo quantidade de jogadores

quantidadeJogadores = Funcoes_Zombie.quantJogadores() #usuario insere quantidade de jogadores
jogadores = [] #variavel que irá armazenar os nomes dos jogadores em lista
listajogadores = []

for z in range (1,quantidadeJogadores+1): #Loop para inserir os nomes dos jogadores na lista, dependendo do numero de jogadores
    jogadores.append(str(input(f'Insira o nome do {z}º jogador: ').upper()))
    jogadores.append(0)
    listajogadores.append(jogadores[:])
    jogadores.clear()

print('')
print('\033[32mOlá \033[m', end='')
for j in listajogadores:
    print(f'\033[32m{j[0]}\033[m', end=', ')
print('\033[32m vamos ao jogo:\033[m')


## DEFININDO OS DADOS

import random # Módulo importado, contem os comandos para gerar aleatoriedade

Funcoes_Zombie.inserirCopo()
#Lista de todos os dados do jogo
tiposDados = ('Dado Verde', 'Dado Amarelo', 'Dado Vermelho')
copo = Funcoes_Zombie.inserirCopo() #FUNÇÃO PARA INSERIR OS 13 DADOS NO COPO EM FORMA DE TUPLA
listaDados = list(copo) #TRANSFORMA A TUPLA EM LISTA, PARA SER EDITAVEL
dados_no_copo = len(listaDados)

jogadorAtual = 0 #Variavel que define qual é o jogador da rodada, onde 0 é o primeiro da lista
faceSorteada = [] #Variavel que armazena as faces dos dados que foram sorteados
tiro = 0 #Variavel que armazenda os tiros
cerebro = 0 #Variavel que armazena os cerebros
passos = 0  #Variavel que armazena os passos

sleep(2)
print('=-'*20)
print('\033[1;31mO JOGO VAI COMEÇAR...\033[m')
print('=-'*20)
sleep(2)



while True:  #INICIA O LOOP
    print('\033[32mÉ a vez de: \033[m',listajogadores[jogadorAtual][0]) #Mostra qual jogador é da vez, inicia com 0 e soma +1 a cada final do turno
    sleep(2)
    print('')
    print('\033[32mRolando os dados...\033[m')
    sleep(2)

    faceSorteada = Funcoes_Zombie.pegaDado(listaDados) #FUNÇÃO IMPORTADA PARA SORTEAR OS 3 DADOS DO COPO

    sleep(2)
    print('')
    print('\033[32mO resultado dos dados foi:\033[m')

    #LOOP PARA SORTEAR A FACE DOS 3 DADOS QUE FORAM SORTEADOS
    for f in range(0, 3):
        numFaceDado = random.randint(0, 5)  # Sorteia um numero de 0 a 5 (6 faces)

        if faceSorteada[f][numFaceDado] == 'C':
            print('\033[31mCEREBRO\033[m', end=' (Dado adicionado á mesa) ')
            cerebro += 1 # Adiciona 1 ponto a variavel cerebro
            Funcoes_Zombie.delDado(listaDados, faceSorteada[f]) #FUNÇÃO PARA DELETAR DO COPO O DADO SORTEADO

        if faceSorteada[f][numFaceDado] == 'T':
            print('\033[32mTIRO\033[m', end=' (Dado adicionado á mesa) ')
            tiro += 1 # Adiciona 1 ponto a variavel tiro
            Funcoes_Zombie.delDado(listaDados, faceSorteada[f]) #FUNÇÃO PARA DELETAR DO COPO O DADO SORTEADO

        if faceSorteada[f][numFaceDado] == 'P':
            print('\033[36mPASSOS\033[m', end=' (Dado Voltou ao Copo) ')
            passos += 1 # Adiciona 1 ponto a variavel passos


    sleep(2)
    print('')
    print('')
    print(f'\033[31mDados na mesa de {listajogadores[jogadorAtual][0]}:\033[m ')
    print('Cerebros', cerebro)
    print('Tiros: ', tiro)

    print('')
    continuar = Funcoes_Zombie.continuar() #FUNÇÃO QUE PERGUNTA AO JOGADOR SE ELE DESEJA CONTINUAR JOGANDO

    #CONDIÇÃO SE O JOGADOR RETIRAR A FACE TIRO 3 VEZES NOS DADOS
    if tiro >= 3:
        print('Você recebeu 3 Tiros')
        sleep(1)
        print('Seu turno Acabou')
        continuar = 'n'

    if len(listaDados) < 3:
        listaDados = list(copo)

    #Condição se a resposta for negativa:
    if continuar == 'n':
        listaDados = list(copo)
        listajogadores[jogadorAtual][1] = cerebro
        jogadorAtual += 1
        faceSorteada = []
        tiro = 0
        cerebro = 0
        passos = 0


        #condição para mudar para o proximo jogador:
    if jogadorAtual == len(listajogadores):
        sleep(1)
        print('')
        print('FIM DO JOGO')
        print('')
        sleep(2)

        Funcoes_Zombie.pontuacao(listajogadores) #FUNÇÃO IMPORTADA QUE MOSTRA A PONTUAÇÃO DOS JOGADORES

        sleep(2)

        Funcoes_Zombie.vencedor(listajogadores) #FUNÇÃO IMPORTADA QUE MOSTRA O VENCEDOR
        print('')

        print('#-' * 16)
        sleep(1)
        print('Finalizando prototipo do jogo...')

        break

    #Condição se o jogador desejar encerrar o seu turno:
    else:
        print('')
        Funcoes_Zombie.contaDados(listaDados) #FUNÇÃO QUE IRÁ ADICIONAR NOVAMENTE OS 13 DADOS AO COPO
        print('')
        print('\033[32mIniciando mais uma rodada ...\033[m')
        dadoSorteados = []
        faceSorteada.clear()
    sleep(1)


