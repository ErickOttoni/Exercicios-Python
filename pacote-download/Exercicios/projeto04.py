#Mensagem inicial de boas vindas
print('Bem vindos a lista de contatos do Erick de Oliveira Ottoni')
print('-'*58)
print('-'*21, 'MENU PRINCIPAL', '-'*21)

lista_contatos=[] #lista vazia para armazenar contatos
id_global=4962074 #id de acordo com meu RU

def cadastrar_contato(id): #função para cadastro de contatos
    print('-'*58)
    print('-'*17, 'MENU CADASTRAR CONTATOS', '-'*16)
    id_contato=input('ID do contato: ')
    nome=input('Nome: ')
    atividade=input('Atividade: ')
    telefone=input('Telefone: ')
    #Dicionário para armazenar os dados das variáveis
    contato={'id':id,
            'nome':nome,
            'atividade':atividade,
            'telefone':telefone}
    #Adicionar o contato à lista de contatos
    lista_contatos.append(contato.copy())
    print ('Contato criado com sucesso!')

def consultar_contatos(): #função para consultar os contatos
    print('-'*58)
    print('-'*17, 'MENU CONSULTAR CONTATOS', '-'*16)
    while True:
        print('Escolha a opção desejada:')
        print('1 - Consultar todos os contatos')
        print('2 - Consultar contato por id')
        print('3 - Consultar contatos por atividade')
        print('4 - Retornar')
        op=int(input('>>'))
        if op==1:
            if not lista_contatos: #Verifica se tem algum contato na lista
                print('Nenhum contato cadastrado.')
            else:
                for contato in lista_contatos:
                    print(f'ID: {contato['id']}')
                    print(f'Nome: {contato['nome']}')
                    print(f'Atividade: {contato['atividade']}')
                    print(f'Telefone: {contato['telefone']}')
                    print()
        elif op==2: #Busca por ID
            id_consulta=int(input('Digite o id: '))
            for contato in lista_contatos:
                if contato['id']==id_consulta: #Caso o id seja igual a de um contato, seus dados irão ser printados na tela
                    print(f'ID: {contato['id']}')
                    print(f'Nome: {contato['nome']}')
                    print(f'Atividade: {contato['atividade']}')
                    print(f'Telefone: {contato['telefone']}')
                    print()
                    break
                else:
                    print('Contato não encontrado.')
        elif op==3: #Consulta por atividade
            atividade_consulta=input('Informe a atividade: ')
            for contato in lista_contatos:
                if contato['atividade'].lower()==atividade_consulta.lower(): #Caso as atividades dos contatos sejam iguais, seus dados irão ser printados na tela
                    print(f'ID: {contato['id']}')
                    print(f'Nome: {contato['nome']}')
                    print(f'Atividade: {contato['atividade']}')
                    print(f'Telefone: {contato['telefone']}')
                    print()
        elif op==4: #Retornar ao menu principal
            return
        else:
            print('Opção inválida!')

def remover_contato(): #função para remover contatos
    print('-'*58)
    print('-'*17, 'MENU REMOVER CONTATOS', '-'*18)
    while True:
        id_remover=int(input('Digite o ID do contato que deseja remover: '))
        for contato in lista_contatos:
            if contato['id']==id_remover: #Caso o id digitado seja igual ao do contato, ele irá ser removido
                lista_contatos.remove(contato)
                print('Contato removido!')
                return
            

#Código principal:
while True:
    print('Escolha a opção desejada:') #MENU INICIAL
    print('1 - Cadastrar contato')
    print('2 - Consultar contato(s)')
    print('3 - Remover contato')
    print('4 - Sair')
    opcao_menu=int(input('>>'))
    #Agora uso as estruturas de condição para que o usuário escolha o que deseja fazer e para que cada escolha chame sua respectiva função, ou até encerre o programa com o break (4)
    if opcao_menu==1: 
        id_global+=1
        cadastrar_contato(id_global)
    elif opcao_menu==2:
        consultar_contatos()
    elif opcao_menu==3:
        remover_contato()
    elif opcao_menu==4:
        print ('Encerrando programa...')
        break
    else:
        print ('Opção inválida, responda com 1,2,3 ou 4.')
    





