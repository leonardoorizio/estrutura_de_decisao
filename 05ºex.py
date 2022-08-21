#aça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    #A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    #A mensagem "Reprovado", se a média for menor do que sete;
    #A mensagem "Aprovado com Distinção", se a média for igual a dez.

def notas_trimeste():

    n1 = float(input('Digite a 1º nota:'))
    n2 = float(input('Digite a 2º nota:'))
    n3 = float(input('Digite a 3º nota:'))
    media = round((n1+n2+n3) / 3)

    if media == 10:
        print(f'Nota {media} - Aprovado com Distinção.')
    elif media >= 7 < 10:
        print(f'Nota {media} - Aprovado.')
    else:
        print(f'Nota {media} - Reprovado.')
notas_trimeste()