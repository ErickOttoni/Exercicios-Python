def defina_string(pergunta,min,max):
    s1=input(pergunta)
    tam=len(s1)
    while (tam<min) or (tam>max):
        s1=input(pergunta)
        tam=len(s1)
    return s1
x=defina_string('Digite uma string: ', 10, 30)
print('Você digitou uma string válida. \n Encerrando...')