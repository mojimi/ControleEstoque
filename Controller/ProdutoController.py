from Model.Produto import Produto
from View.ProdutoView import ProdutoView


class ProdutoController:
    def __init__(self):
        self.produtos = []
        self.view = ProdutoView(controller=self)


    def newproduto(self, nome, preco, quantidade):
        self.produtos.append(Produto(nome, preco, quantidade))

    def listprodutos(self):
        sRet = ""
        for produto in self.produtos:
            sRet = sRet + "\n" + produto.__str__()

    def getproduto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto

