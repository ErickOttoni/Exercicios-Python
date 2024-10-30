A=int(input('Digite o 1° valor: '))
B=int(input('Digite o 2° valor: '))
C=int(input('Digite o 3° valor: '))

if (A>0 and B>0 and C>0) and (A+B>C and B+C>A and A+C>B):
    print('Temos um triângulo!')
    if (A==B, B==C, C==A):
        print('TRIÂNGULO EQUILÁTERO!')
    elif (A!=B, B!=C, C!=A):
        print('TRIÂNGULO ESCALENO!')
    else:
        print('TRIÂNGULO ISÓSCELES!')
    