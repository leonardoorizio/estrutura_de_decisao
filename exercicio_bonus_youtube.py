class Carro:
    def __init__(self,marca,ano,cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def Ligando(self):
        print('Ruuuuuuuuuuum')
    def Desligando(self):
        print('@#$@%$%#¨&*&')
    def Agradecimento(self):
        print('Thanks')
    def ExibiInformacoes(self):
        print(self.marca,self.ano,self.cor)

carro1 = Carro('Tesla 3','2024','Black')
carro1.Ligando()
carro1.Desligando()
carro1.Agradecimento()
carro1.ExibiInformacoes()