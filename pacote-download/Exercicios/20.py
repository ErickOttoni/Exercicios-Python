def mulheres30(sexo,idade):
    global mulher30
    if sexo=='f' and idade<30:
        mulher30+=1


cadastro={'nome':[], 'sexo':[], 'ano':[], 'idade':[]} #DICIONÁRIO 3 PALAVRAS CHAVE: SEGUIDOS DE 3 DADOS [VAZIOS]
cont=0
idadetot=0
mulher30=0


while True:
    terminar=input('Deseja cadastrar uma pessoa? [S/N]') 
    if terminar.upper() in 'N': 
        break
    elif terminar.upper() not in 'S': #ele só vai executar isso se a pessoa não digitar N, caso não digite
        print('Digite S para sim ou N para não')#S também, irá continuar, voltando pro começo do loop
        continue
    elif terminar.upper() in 'S':
        cont+=1

    nome=input('Digite o nome: ')
    sexo=input('Digite o sexo: ')
    ano=int(input('Qual o ano de nascimento: '))
    anoat=int(input('E qual o ano atual? '))
    idade=anoat-ano
    idadetot+=idade
    cadastro['nome'].append(nome) #AQUI A VAR CADASTRO É O DICIONÁRIO, ENTRE COLCHETES[] PALAVRAS CHAVE E 
    cadastro['sexo'].append(sexo) #APPEND PRA ADICIONAR ITEM AO FINAL DA LISTA, SEGUIDO DO DADO() QUE
    cadastro['ano'].append(ano)   #SÃO AS LISTAS VAZIAS LÁ EM CIMA
    cadastro['idade'].append(idade)
    
med=(idadetot/cont)
print(cadastro)
print(cont)
print(idadetot)
print(med)

