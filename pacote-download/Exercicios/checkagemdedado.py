def check (dado):
    match dado:
        case str(dado): #caso dado seja STRING
            print(f'STRING: ', {dado})
        case int(dado): #caso dado seja INTEIRO
            print(f'INTEIRO: ', {dado})
        case float(dado): #caso dado seja FLUTUANTE
            print(f'FLOAT: ', {dado})
        case _:
            print('DADO INEXISTENTE')

dados=['Olá mundo', 51, 98, 5.6, 'Erick']
for dado in dados:
    check(dado)