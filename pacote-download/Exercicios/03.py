print('+')
print('-')
print('*')
print('/')
op=input('Qual operação deseja fazer?')
x=int(input('Digite o primeiro número: '))
y=int(input('Digite o segundo número: '))
if(op=='+'):
    res=x+y
    print(res)
elif (op=='-'):
    res=x-y
    print(res)
elif (op=='*'):
    res=x*y
    print(res)
elif (op=='/'):
    res=x//y
    print(res)