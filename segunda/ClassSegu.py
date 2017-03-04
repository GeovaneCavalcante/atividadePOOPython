class estoque(object):

    def __init__(self, nome, quantidade, quantidade_min):
        self.nome = str(nome)
        if (quantidade>=0):
            self.quantidade = int(quantidade)
        if (quantidade_min>=0):
            self.quantidade_min = int(quantidade_min)

    def getNome(self):
        return (self.nome)

    def setNome(self, nome):
        self.nome = str(nome)

    def getQuantidade(self):
        return (self.quantidade)

    def setQuantidade(self, quantidade):
        self.quantidade = int(quantidade)

    def getQuantidade_min(self):
        return (self.quantidade_min)

    def setQuantidade_min(self, q_m):
        self.quantidade_min = int(q_m)

    def repor(self, qtd):
        self.quantidade += int(qtd)

    def darbaixa(self, baixa):
        if (baixa< self.getQuantidade()):
            self.quantidade -= baixa

    def descriçao(self):
        des = str("Produto: %s, quantidade em estoque: %i, quantidade_min: %i" %(self.getNome(), self.getQuantidade(), self.getQuantidade_min()))
        return (des)

    def check(self):
        return (self.getQuantidade()<self.getQuantidade_min())
