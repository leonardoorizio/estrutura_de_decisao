#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias_da_semana = ['Inválido','1 - Domingo', '2 - Segunda', '3 - Terça', '4 - Quarta', '5 - Quinta', '6 - Sexta', '7 - Sábado']

def semana():

    cliente = int(input('Digite um número entre 1 e 8, que vou lhe dizer qual dia da semana representa:'))

    if  (cliente >=0) and (cliente <=7):
        print(f'{dias_da_semana[cliente]}')
    else:
        print('Inválido')

semana()