print('Escolha o quê deseja comprar:')
print('1- Maçã')
print('2- Banana')
print('3 Pera')

fruta=int(input('Qual sua escolha? '))
qnt=int(input('Quantidade: '))

if (fruta==1):
    preco=qnt*0.50
    fru='maçã'
else:
    if (fruta==2):
        preco=qnt*0.80
        fru='Banana'
    else:
        if (fruta==3):
            preco=qnt*1.10
            fru='Pera'
        else: 
            print('PRODUTO INESISTENTE!')

print(f'Você comprou {qnt} {fru}(s) e deve pagar R${preco}')

#ESCOLHA CASO (MATCH CASE)

print('Escolha o quê deseja comprar:')
print('1- Maçã')
print('2- Banana')
print('3 Pera')

fruta=int(input('Qual sua escolha? '))
qnt=int(input('Quantidade: '))

match (fruta):
    case 1:
        preco=qnt*0.50
        fru='maçã'
    case 2:
        preco=qnt*0.80
        fru='Banana'
    case 3:
        preco=qnt*1.10
        fru='Pera'
    case _: #outrocaso é representado por underline (_)
        print('PRODUTO INESISTENTE!')

print(f'Você comprou {qnt} {fru}(s) e deve pagar R${preco}')
