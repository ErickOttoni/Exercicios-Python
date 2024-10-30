palavras=('banana','mochila','chimarrão','botafogo','grêmio')
for palavra in palavras:
    print (f'\n{palavra} VOGAIS: ') #INDEXAÇÃO DUPLA, NO PRIMEIRO PEGO PALAVRA POR PALAVRA
    for letra in palavra: #E AQUI NA SEGUNDA PEGO A LETRA DE CADA PALAVRA
        if letra.lower() in 'aeiou': #TESTE DE EXPRESSÃO
            print(letra, end=' ')