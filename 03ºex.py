#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def genero():
    sexo = str.upper(input('Digite seu sexo M ou F:'))

    if sexo == 'M':
        print('M - Masculino')
    elif sexo == 'F':
        print('F - Feminino')
    else:
        print('Sexo inválido')
genero()