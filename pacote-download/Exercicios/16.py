def fatorial(x):       #X VAR LOCAL
    fat=1
    if x==0:
        return fat
    for cont in range (1,x+1):
        fat*=cont
    return fat

def valida(pergunta,min,max):
    n=int(input(pergunta))
    while n<min or n>max:   #N<0 OU N>9999999
         n=int(input(pergunta))
    return n

        
n=valida('Calcular o fatorial do número: ', 0, 9999999) #PERGUNTA/VALOR MININO/VALOR MÁXIMO  
print(f'{n}! = {fatorial(n)}')