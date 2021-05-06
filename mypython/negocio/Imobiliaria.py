class Imobiliaria:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco
