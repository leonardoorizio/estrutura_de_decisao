#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
#isósceles ou escaleno.

    #Dicas:
    #Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    #Triângulo Equilátero: três lados iguais;
    #Triângulo Isósceles: quaisquer dois lados iguais;
    #Triângulo Escaleno: três lados diferentes;

def triangulo():

    a = float(input('Entre com a medida do 1º lado do triângulo:'))
    b = float(input('Entre com a medida do 2º lado do triângulo:'))
    c = float(input('Entre com a medida do 3º lado do triângulo:'))

    if a<=0 or b<=0 or c<=0:
        print('Não existe triângulo com essas medidas!')
    elif a>=b+c or b>=c+a or c>=a+b:
        print('Triângulo inexistente!')
    elif a==b and b==c:
        print('Triângulo Equilátero')
    elif a==b or b==c or c==a:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')

triangulo()



