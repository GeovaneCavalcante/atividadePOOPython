import math

class Massa_Corp(object):
    
    def __init__(self, nome, peso, altura):
        self.nome = str(nome)
        self.peso = float(peso)
        self.altura = float(altura)

    def getNome(self):
        return (self.nome)

    def setNome(self, nome):
        self.nome = nome

    def getPeso(self):
        return(self.peso)

    def setPeso(self, peso):
        self.peso= peso

    def getAltura(self):
        return (self.altura)

    def setAltura(self, altura):
        self.altura = altura

    def calcular(self):
        imc = float((self.getPeso()*(pow(self.getAltura(), 2))))
        return (imc)
