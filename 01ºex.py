#Faça um Programa que peça dois números e imprima o maior deles.

def comparacao():
    n1 = int(input('Digite um nº:'))
    n2 = int(input('Digite um nº:'))

    if n1 > n2:
        print(f'O nº {n1} é o maior!')
    else:
        print(f'O nº {n2} é o maior!')
comparacao()
