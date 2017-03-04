class funcionario(object):
    def __init__(self, nome, horas, valor_hora):
        self.nome = str(nome)
        self.horas = float(horas)
        self.valor_hora = float(valor_hora)

    def getNome(self):
        return (self.nome)

    def setNome(self, nome):
        self.nome = str(nome)

    def getHoras(self):
        return (self.horas)

    def setHoras(self, horas):
        self.horas = float(horas)

    def getValor_hora(self):
        return (self.valor_hora)

    def setValor_hora(self, valor):
        self.valor_hora = float(valor)

    def calcular(self):
        return (self.valor_hora*self.horas)
