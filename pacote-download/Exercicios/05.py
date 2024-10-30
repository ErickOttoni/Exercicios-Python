kwh=float(input('Quantidade de kwh consumida: '))
print('Residência (r)')
print('Indústria (i)')
print('Comércio(c)')
res=input("QUAL SEU TIPO DE INSTALAÇÃO? ")

if (res=='r'):
    if(kwh<=500):
        en=0.40
    else:
         en=0.65
    print(f'Total a pagar R${en*kwh}')

elif (res=='c'):
    if(kwh<=1000):
        en=0.55
    else:
        en=0.60
    print(f'Total a pagar R${en*kwh}')

elif (res=='i'):
    if(kwh<=5000):
        en=0.55
    else:
        en=0.60
    print(f'Total a pagar R${en*kwh}')

else:
    print("Você digitou errado!")