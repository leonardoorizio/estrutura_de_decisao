#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      #Média de Aproveitamento  Conceito
      #Entre 9.0 e 10.0        A
      #Entre 7.5 e 9.0         B
      #Entre 6.0 e 7.5         C
      #Entre 4.0 e 6.0         D
      #Entre 4.0 e zero        E

def alura():

    nota1 = float(input('1º nota do aluno:'))
    nota2 = float(input('2º nota do aluno:'))
    nota3 = float(input('3º nota do aluno:'))
    media = (nota1+nota2+nota3) / 3

    if (media >= 9) and (media <= 10):
        print('Nota: A')
    elif (media >= 7.5) and (media < 9):
        print('Nota: B')
    elif (media >= 6) and (media < 7.5):
        print('Nota: C')
    elif (media >= 4) and (media < 6):
        print('Nota: D')
    elif (media >= 0) and (media < 4):
        print('Nota: E')
    else:
        print('')

alura()

