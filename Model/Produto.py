class Produto:
    def __init__(self, nome, preco = 0, quantidade = 0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return "Nome : " + self.nome + " | Preço : " + str(self.preco)  + " | Estoque : " +  str(self.quantidade)

class Entrada:
    def __init__(self):
        return
class Saida:
    def __init__(self):
        return



