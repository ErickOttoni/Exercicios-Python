print('PRODUTOS LANCHONETE:')
print('1 - Coxinha R$5,00')
print('2 - Pastel R$7,00')
print('3 - Café R$4,00')
print('4 - Suco R$6,00')
print('5 - SAIR:')
total=0
while True:
    esc=int(input('Qual sua escolha? '))
    
    if(esc==1):
        qnt=int(input('Quantas unidades: '))
        total+=qnt*5

    elif(esc==2):
        qnt=int(input('Quantas unidades: '))
        total+=qnt*7

    elif(esc==3):
        qnt=int(input('Quantas unidades: '))
        total+=qnt*4

    elif(esc==4):
        qnt=int(input('Quantas unidades: '))
        total+=qnt*6
    
    elif(esc==5):
        break
        print('Saindo...')

    else:
        print('Essa escolha não existe!')
print(f'\n Total do seu pedido: R${total}')