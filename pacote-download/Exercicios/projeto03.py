print('Bem vindos a madeireira do Lenhador Erick de Oliveira Ottoni') #Mensagem inicial de boas vindas
def escolha_tipo(): #Função para escolher o tipo de madeira
    while True:
        print('Escolha o tipo de madeira: ')
        print('PIN - Tora de Pinho')
        print('PER - Tora de Peroba')
        print('MOG - Tora de Mogno')
        print('IPE - Tora de Ipê')
        print('IMB - Tora de Imbuia')
        tipo_madeira=input('>>').upper()
        #Agora irei retornar os valores por tipo de madeira escolhidas
        if tipo_madeira=='PIN':
            return 150.40
        elif tipo_madeira=='PER':
            return 170.20
        elif tipo_madeira=='MOG':
            return 190.90
        elif tipo_madeira=='IPE':
            return 210.10
        elif tipo_madeira=='IMB':
            return 220.70
        else: #Caso o cliente escreva um tipo de madeira inexistente, apresentará este print abaixo na tela e voltará a pergunta inicial
            print('Escolha inválida, entre com o modelo novamente')

def qtd_toras(): #Função para escolher a quantidade de toras
    while True:
        try:
            qtd=int(input('Agora escolha a quantidade de toras (m³): '))
            if qtd>2000: #Caso cliente deseje mais do que 2000 toras, apresentará este print abaixo na tela e voltará a pergunta inicial, pois ultrapassa o valor máximo do pedido
                print('Não aceitamos pedidos com essa quantidade de Toras, entre com a quantidade novamente!')
                #Caso quantidade seja válida, irá retornar seu valor e respectivamente o valor de seu desconto, separado por vírgula
            elif qtd<100:
                return qtd, 0.00 #quantidade,desconto
            elif qtd>=100 and qtd<500:
                return qtd, 0.04
            elif qtd>=500 and qtd<1000:
                return qtd, 0.09
            elif qtd>=1000 and qtd<=2000:
                return qtd, 0.16
        except ValueError: #Exceção para caso usuário digite uma string em quantidade
            print('Quantidade inválida, você deve entrar com um valor numérico.')

def transporte(): #Função para escolher o transporte
    while True:
        print('Escolha o tipo de transporte:')
        print('1 - Transporte Rodoviário  = R$1000.00')
        print('2 - Transporte Ferroviário = R$2000.00')
        print('3 - Transporte Hidroviário = R$2500.00')
        transp=int(input('>>'))
        if transp==1:
            return 1000.00
        elif transp==2:
            return 2000.00
        elif transp==3:
            return 2500.00
        else: #Caso opção escolhida seja diferente de 1,2 ou 3 irá printar essa frase abaixo e voltar para pergunta inicial
         print('Opção de transporte inválida, escolha entre as opções 1, 2 ou 3.')

#Código principal

tipo_madeira=escolha_tipo() #variáveis= chamando as funções 
qtd,desc=qtd_toras()
transp=transporte()
#Cálculo do valor final do pedido
valor_final=((tipo_madeira*qtd)*(1-desc))+transp
#Print final do código com o valor total
print(f'O valor final do seu pedido é: R${valor_final:.2f}')