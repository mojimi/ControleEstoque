from Model.Produto import Produto
from View.ProdutoView import ProdutoView


class ProdutoController:
    def __init__(self):
        self.produtos = []
        self.view = ProdutoView(controller=self)


    def newproduto(self, nome, preco, quantidade):
        self.produtos.add(Produto(nome, preco, quantidade))

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
