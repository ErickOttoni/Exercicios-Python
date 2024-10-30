#Aqui crio o Menu que irá aparecer para o cliente com as informações necessárias para realização do pedido, onde usei algumas manipulações de strings como aprendido nas aulas.
print('-'*10, 'Bem vindo a Pizzaria do Erick de Oliveira Ottoni', '-'*9) 
print('-'*25, 'Cardápio', '-'*34)
print('-'*69)
print('---|',  ' TAMANHO' '  | ', '   Pizza Salgada(PS)', '   |', '    Pizza Doce(PD)', '  |---')
print('---|  ', '  P',  '    | ', '       R$30,00', '         |',      '      R$34,00',     '       |---')
print('---|  ', '  M',  '    | ', '       R$45,00', '         |',      '      R$48,00',     '       |---')
print('---|  ', '  G',  '    | ', '       R$60,00', '         |',      '      R$66,00',     '       |---')
print('-'*69)

valor_total=0 #Variável acumulativa (preço final).

#Agora em um laço de repetição(que poderá ser encerrado com S ou N ao fim do pedido) irei pedir ao cliente suas escolhas e as salvar em variáveis(sabor e tamanho), lembrando que tamanho só será executada caso o cliente escolha um sabor existente (PS ou PD).
while True:
    sabor=input('Informe o sabor desejado (PS/PD): ') #Pergunta inicial do laço.
    if (sabor.upper()=='PS'): #Caso o cliente escolha pizza salgada, este código será executado.
        tamanho=input('Agora escolha o tamanho desejado (P/M/G): ') #próximo passo escolher o tamanho.
        if tamanho.upper() in 'P':
            print('Você pediu uma pizza salgada no tamanho P: R$30.00')
            valor_total+=30
        elif tamanho.upper() in 'M':
            print('Você pediu uma pizza salgada no tamanho M: R$45.00')
            valor_total+=45
        elif tamanho.upper() in 'G':
            print('Você pediu uma pizza salgada no tamanho G: R$60.00')
            valor_total+=60
        else:   #Caso o cliente digite um tamanho que não seja P,M OU G irá retornar ao início do laço.
            print('Tamanho inválido, tente novamente!')
            continue 
    elif (sabor.upper()=='PD'): #Caso o cliente escolha pizza doce, este código será executado.
        tamanho=input('Agora escolha o tamanho desejado (P/M/G): ')
        if tamanho.upper() in 'P':
            print('Você pediu uma pizza doce no tamanho P: R$34.00')
            valor_total+=34
        elif tamanho.upper() in 'M':
            print('Você pediu uma pizza doce no tamanho M: R$48.00')
            valor_total+=48
        elif tamanho.upper() in 'G':
            print('Você pediu uma pizza doce no tamanho G: R$66.00')
            valor_total+=66
        else: #Caso o cliente digite um tamanho que não seja P,M OU G irá retornar ao inicio do laço.
            print('Tamanho inválido, tente novamente!')
            continue
    else: #Este se refere aos sabores, caso digite algo diferente de 'PS' ou 'PD' irá ser repetida a pergunta do início do laço até ele digitar um sabor válido.
        print('Sabor inexistente, tente novamente!')
        continue
    op=input('Deseja mais alguma coisa? (S/N): ') #Aqui vai ser a parte do código para o cliente escolher se quer finalizar o pedido ou pedir algo mais, sem essa parte o laço de repetição nunca se encerraria.
    if op.upper() in 'N':
        break
    elif op.upper() in 'S':
        continue
    #Usei o método 'upper' para converter todas as strings para maiúsculas e não dar erro quando o cliente digitasse letra minúscula nas escolhas.

print(f'O valor total a ser pago é de: R${valor_total}') #Print com o valor total do pedido, só executado depois que o cliente escolhar a opçaõ 'N' no código logo a cima.
    


