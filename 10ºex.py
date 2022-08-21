#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def turno():

    periodo = input('Digite o periodo que você estuda, M - matutino / V - vespertino / N - noturno:')

    if periodo == 'M - matutino':
        print('Bom dia!')
    elif periodo == 'V - vespertino':
        print('Boa tarde!')
    elif periodo == 'N - noturno':
        print('Boa noite!')
    else:
        print('Valor inválido!')
turno()

