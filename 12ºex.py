#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
#Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    #Desconto do IR:
    #Salário Bruto até 900 (inclusive) - isento
    #Salário Bruto até 1500 (inclusive) - desconto de 5%
    #Salário Bruto até 2500 (inclusive) - desconto de 10%
    #Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            #Salário Bruto: (5 * 220)        : R$ 1100,00
            #(-) IR (5%)                     : R$   55,00
            #(-) INSS ( 10%)                 : R$  110,00
            #FGTS (11%)                      : R$  121,00
            #Total de descontos              : R$  165,00
            #Salário Liquido                 : R$  935,00

def salário():

    valor_hora = float(input('Valor hora de trabalho:'))
    horas_de_trabalho = float(input('Qtd de horas de trabalho:'))
    salario_mensal = float(valor_hora * horas_de_trabalho)

    #Inss e Sindicato

    inss = (salario_mensal * 10) / 100
    sincato = (salario_mensal * 3) / 100

    #Imposto de renda

    if (salario_mensal > 900) and (salario_mensal < 1500):
        ir = (salario_mensal * 5) / 100
    elif (salario_mensal >= 1500) and (salario_mensal < 2500):
        ir = (salario_mensal * 10) / 100
    elif (salario_mensal >= 2500):
        ir = (salario_mensal * 20) / 100
    else:
        ir = 0

    # (+) FGTS

    fgts = (salario_mensal * 11) / 100

    #Total de descontos

    descontos = ( inss + sincato + ir)

    #Salário liquido

    salario_liquido = (salario_mensal - descontos)

    print(f'\nSalário Bruto:R${salario_mensal:.2f}')
    print(f'(-)IR:R${ir:.2f}')
    print(f'(-)INSS:R${inss:.2f}')
    print(f'(-)Sindicato:R${sincato:.2f}')
    print(f'FGTS:R${fgts:.2f}')
    print(f'Total de descontos:R${descontos:.2f}')
    print(f'Salário Liquido:R${salario_liquido:.2f}')

salário()





