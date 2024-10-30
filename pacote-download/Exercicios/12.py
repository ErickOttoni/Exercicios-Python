val=int(input('Digite um valor em R$: '))
while True:
    if val>=100:
        cont100=val//100
        val=val-cont100*100
        print(f'Células de R$100: {cont100}')
        if not val:
            break
    elif val>=50:
        cont50=val//50
        val=val-cont50*50
        print(f'Células de R$50: {cont50}')
        if not val:
            break
    elif val>=20:
        cont20=val//20
        val=val-cont20*20
        print(f'Células de R$20: {cont20}')
        if not val:
            break
    elif val>=10:
        cont10=val//10
        val=val-cont10*10
        print(f'Células de R$10: {cont10}')
        if not val:
            break
    elif val>=5:
        cont5=val//5
        val=val-cont5*5
        print(f'Células de R$5: {cont5}') 
        if not val:
            break
    elif val:
        cont1=val
        print(f'Células de R$1: {cont1}')
        break

