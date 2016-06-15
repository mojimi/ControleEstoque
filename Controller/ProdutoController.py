from Model.Produto import Produto
from View.ProdutoView import ProdutoView


class ProdutoController:
    def __init__(self):
        self.produtos = []
        self.view = ProdutoView(controller=self)


    def newproduto(self, nome, preco, quantidade):
        self.produtos.append(Produto(nome, preco, quantidade))

    def listprodutos(self):
        produtos = ()
        for produto in self.produtos:
            produtos.add(produto.__str__())
        return produtos

    def toProdutos(self):
        self.view.tkraise()



    def getproduto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto

    def filterPrecosMaioresX(self, preco):
        filtered = [i for i in self.produtos if i.preco >= preco]
        return filtered

    def filterPrecosMenoresX(self, preco):
        filtered = [i for i in self.produtos if i.preco <= preco]
        return filtered

    def filterQuantidadesMaioresX(self, quantidade):
        filtered = [i for i in self.produtos if i.quantidade >= quantidade]
        return filtered

    def filterQuantidadesMenoresX(self, quantidade):
        filtered = [i for i in self.produtos if i.quantidade <= quantidade]
        return filtered


pc = ProdutoController()
pc.newproduto("banana", 0, 4)
pc.newproduto("maça", 3, 3)
pc.newproduto("pera", 2, 5)
pc.newproduto("chocolate", 5, 8)

print(len(pc.filterPrecosMaioresX(3))) #1,3
print(pc.filterPrecosMaioresX(3))
print(len(pc.filterQuantidadeMenoresX(4))) #0,1
print(pc.filterQuantidadeMenoresX(4))

