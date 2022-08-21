#Faça um Programa que leia três números e mostre o maior deles.

#def comparacao():

    #n1 = int(input('Digite um nº:'))
    #n2 = int(input('Digite um nº:'))
    #n3 = int(input('Digite um nº:'))

    #if n1 > n2 & n3:
        #print(f'O nº maior é {n1}')
#elif n2 > n1 & n3:
        #print(f'O nº maior é {n2}')
#elif n3 > n1 & n2:
        #print(f'O nº maior é {n3}')
#comparacao()

def comparacao():

    numeros = []
    tentativas = 0

    while tentativas < 3:

        numeros.insert(tentativas,input('Digite um número:'))
        tentativas += 1

    nº = max(numeros)

    print(f'Entre os três números informado, o maior é {nº}.')
comparacao()


