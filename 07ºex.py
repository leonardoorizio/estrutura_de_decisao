#Faça um Programa que leia três números e mostre o maior e o menor deles.

def comparacao():

    numeros = []
    tentativas = 0

    while tentativas < 3:

        numeros.insert(tentativas,input('Digite um numero:'))
        tentativas += 1

        maior = max(numeros)
        menor = min(numeros)

    print(f'O maior nº foi {maior} e o menor foi {menor}.')

comparacao()