def vencedor(jog1,jog2):
    global v1,v2,empate #TORNANDO AS VARIÁVEIS LOCAIS ACUMULATIVAS GLOBAIS
    if jog1==1: #PEDRA
        if jog2==1: #PEDRA
            empate+=1 
        elif jog2==2: #PAPEL
            v2+=1
        elif jog2==3: #TESOURA
            v1+=1

    elif jog1==2: #PAPEL   #AQUI FIZ O ELIF ALINHADO AO PRINCIPAL (1°)
        if jog2==1: #PEDRA
            v1+=1
        elif jog2==2: #PAPEL
            empate+=1
        elif jog2==3: #TESOURA
            v2+=1 

    elif jog1==3: #TESOURA  #ELIF PRINCIPAL
        if jog2==1: #PEDRA
            v2+=1
        elif jog2==2: #PAPEL
            v1+=1
        elif jog2==3: #TESOURA
            empate+=1 
    
    resultado=[v1,v2,empate] #COLOCANDO OS RESULTADOS DENTRO DAS LISTAS
    return resultado


def validacao(pergunta,min,max):
    x=int(input(pergunta))
    while (x<min) or (x>max):
        x=int(input(pergunta))
    return x

import random  #FUNÇÃO DO PYTHON QUE SORTEIA UM NÚMERO ALEATÓRIO


#PROGRAMA PRINCIPAL
print('-' *20)
print('      Jokenpo')
print('-' *20)
print('1- PEDRA')
print('2- PAPEL')
print('3- TESOURA')

jogadas=[] #Listas vazias
resultados=[]
       #Listas acumulativas
v1=0
v2=0
empate=0

while True: #laço infinito
    j1=validacao('Escolha sua jogada: ',0,3) #PERGUNTA, MIN, MAX FEITOS NA FUNÇÃO LA EM CIMA
    if not j1: #MESMA COISA QUE DIZER QUE DIGITOU ZERO
        break
    j2=random.randint(1,3) #randint vai sortear números no intervalo desejado pelo programador (1,3)
    jogadas.append([j1,j2]) #Aqui irei jogar os resultados pra dentro da lista JOGADAS
    resultados=vencedor(j1,j2)

for jogada in jogadas: #INDEXAÇÃO DUPLA, TENHO 2 LISTAS DENTRO DE JOGADAS(J1,J2)
    for dado in jogada:
        print(dado, end='  ')
    print()

print(f'Número de vitórias do Jogador 1: {resultados[0]}') #Como são listas primeiro coloco o nome da
print(f'Número de vitórias do Jogador 2: {resultados[1]}') #lista e depois o índice, lembrando que o
print(f'Número de empates: {resultados[2]}')               #índice sempre começa por zero