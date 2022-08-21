#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def pos_neg():
    n1 = int(input('Digite um nº:'))

    if n1 > 0:
        print(f'O nº {n1} é positivo!')
    else:
        print(f'O nº {n1} é negativo!')
pos_neg()

