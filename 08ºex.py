#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def comparador_de_preco():

    produto = []
    tentativas = 1

    while tentativas < 4:

        produto.insert(tentativas,input(f'Digite o valor do {tentativas}º produto:'))
        tentativas += 1

        menor_preco = min(produto)

    print(f'\nO melhor preço de compra é R${menor_preco}.')

comparador_de_preco()





