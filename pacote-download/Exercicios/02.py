nome=input('Digite o nome: ')
idade=int(input('Qual sua idade? '))
if(nome=='Vinicius'):
    print('Olá Vinicius!')
elif(idade>=18) and (idade<=99):
    print('Você não é o Vinicius e é maior de idade!')
elif(idade<=18):
    print('Você não é o Vinicius e é menor de idade!')
elif(idade>=100):
    print('Você não é o Vinicius e está querendo me sacanear!')
    