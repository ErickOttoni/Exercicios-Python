print('Bem vindo ao Sistema de Erick de Oliveira Ottoni:')
valor_base=float(input('Informe o valor base do plano: R$')) 
idade=int(input('Informe a idade do cliente: '))

#Agora irei calcular o valor mensal, multiplicando o VALOR BASE informado pelo cliente com a porcentagem que irá variar de acordo com a respectiva IDADE, também informada pelo cliente. 
#Lembrando que divido a porcentagem por 100 antes de realizar o cálculo!
if idade>=0 and idade<19:
    valor_mensal=valor_base*1 #100/100
elif idade>=19 and idade<29:
    valor_mensal=valor_base*1.50 #150/100
elif idade>=29 and idade<39:
    valor_mensal=valor_base*2.25 #225/100
elif idade>=39 and idade<49:
    valor_mensal=valor_base*2.40 #240/100
elif idade>=49 and idade<59:
    valor_mensal=valor_base*3.50 #350/100
else: #de 59 anos pra cima
    valor_mensal=valor_base*6   #600/100

print(f'O valor do plano mensal do cliente com {idade} anos de idade é de: R${valor_mensal:.2f}') #:.2f = Tirar as casas decimais