#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.



consoante = ['b','c','d','f','g','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

vogal = ['a','e','i','o','u']

def verificacao():

    letra = str.lower(input('Digite uma letra:'))

    if letra in consoante:
        print(f'A letra {letra} é uma consoante.')
    elif letra in vogal:
        print(f'A letra {letra} é uma vogal.')

verificacao()