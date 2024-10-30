def valida(pergunta,min,max):
    n=int(input(pergunta))
    while n<min or n>max:   
         n=int(input(pergunta))
    return n

def existeArquivo(nomeArquivo):
    try:                             #Não posso esquecer do TRY
        a= open(nomeArquivo, 'rt')  #Sempre vai esse t acompanhando e o r vai ler o arquivo
        a.close()          #FECHANDO O ARQUIVO (SEMPRE FAÇO ISSO)
    except FileNotFoundError: #ERRO DE SEMPRE QND NÃO ENCONTRADO
        return False
    else:
        return True
    
def criarArquivo(nomeArquivo):
    try:
        a=open(nomeArquivo, 'wt+') #Aqui ele abrirá o arquivo de qlq jeito (criará um se for preciso)
        a.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso! \n')

def cadastrarJogo(nomeArquivo,nomeJogo,nomeVideogame):
    try:
        a=open(nomeArquivo, 'at') #ABRINDO ELE PRA ESCRITA E PRESERVANDO SEU CONTEÚDO
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write (f'{nomeJogo};{nomeVideogame}\n') #Aqui jaz o conteúdo que vai direto pra dentro do arq
    finally:
        a.close() #Aqui eu só fecho no fim pois quero escrever dentro do arquivo antes!

def listarArquivo(nomeArquivo):
    try:
        a=open(nomeArquivo, 'rt') #r de read
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read()) #Já estou printando a leitura do arquivo aqui
    finally:
        a.close()  #Aqui eu só fecho no fim pois quero ler e listar oq está dentro do arquivo antes!


#PROGRAMA PRINCIPAL=====================
arquivo='games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado!')
else:
    print('Arquivo inexistente!')
    criarArquivo(arquivo) #Caso não exista, aqui chamo a função para cria-lo

while True:
    print('|  MENU  |:')
    print('1- Cadastrar novo item')
    print('2- Listar cadastros')
    print('3- Sair')

    op=valida('Escolha sua opção: ',1,3)
    if op==1:
        print('Opção de cadastrar novo item selecionada... \n')
        nomeJogo=input('Nome do jogo: ')
        nomeVideogame=input('Nome do videogame: ')
        cadastrarJogo(arquivo,nomeJogo,nomeVideogame)

    elif op==2:
        print('Opção de listar selecionada... \n')
        listarArquivo(arquivo)

    elif op==3:
        print('Encerrando...')
        break