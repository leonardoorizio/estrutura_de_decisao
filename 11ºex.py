#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    #Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    #salários até R$ 280,00 (incluindo) : aumento de 20%
    #salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    #salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    #salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    #o salário antes do reajuste; X
    #o percentual de aumento aplicado; X
    #o valor do aumento; X
    #o novo salário, após o aumento. X


def reajuste_salarial():

    salario = float(input('Digite o salário atual:'))

    if salario < 280:
        salario_junior = (salario * 20) / 100
        print(f'\nSALÁRIO ATUAL:R${salario:.2f}')
        print(f'PERCENTUAL DE AUMENTO:20%')
        print(f'VALOR DO AUMENTO:R${salario_junior:.2f}')
        print(f'NOVO SALÁRIO:R${salario + salario_junior:.2f}')

    elif (salario >= 280) and (salario < 700):
        salario_pleno = (salario * 15) / 100
        print(f'\nSALÁRIO ATUAL:R${salario:.2f}')
        print(f'PERCENTUAL DE AUMENTO:15%')
        print(f'VALOR DO AUMENTO:R${salario_pleno:.2f}')
        print(f'NOVO SALÁRIO:R${salario + salario_pleno:.2f}')

    elif (salario >= 700) and (salario < 1500):
        salario_senior = (salario * 10) / 100
        print(f'\nSALÁRIO ATUAL:R${salario:.2f}')
        print(f'PERCENTUAL DE AUMENTO:10%')
        print(f'VALOR DO AUMENTO:R${salario_senior:.2f}')
        print(f'NOVO SALÁRIO:R${salario + salario_senior:.2f}')

    else:
        salario_master = (salario * 5) / 100
        print(f'\nSALÁRIO ATUAL:R${salario:.2f}')
        print(f'PERCENTUAL DE AUMENTO:5%')
        print(f'VALOR DO AUMENTO:R${salario_master:.2f}')
        print(f'NOVO SALÁRIO:R${salario + salario_master:.2f}')

reajuste_salarial()

