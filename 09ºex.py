#Faça um Programa que leia três números e mostre-os em ordem decrescente.

def decrescente():

    variavel = []
    tentativas = 0

    while tentativas < 3:

        variavel.insert(tentativas,input('Digite um nº:'))
        tentativas += 1

    ordem_decrescente = sorted(variavel, reverse =True)

    print(f'Segue lista em ordem decrescente: {ordem_decrescente}')

decrescente()