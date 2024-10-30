tot=0
dinheiro=0
totid=0
while True:
    idade=int(input('Qual sua idade? '))
    if idade==0:
        break
    if idade<=3:
        tot+=1
        totid+=idade
        ing=0
        print('Seu ingresso será gratuíto!')
    elif idade<=12:
        tot+=1
        totid+=idade
        ing=15
        print('Seu ingresso custará R$15,00')
    elif idade>12:
        tot+=1
        totid+=idade
        ing=30
        print('Seu ingresso custará R$30,00')
    dinheiro+=ing
    med=totid/tot
    
print(f'Um total de {tot} ingressos foram adquiridos, com o valor total de R${dinheiro}')
print(f'Média de idade dos clientes {med}')
    
