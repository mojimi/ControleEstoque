from Model.Produto import Produto
import tkinter as tk


class ProdutoController:

    def __init__(self, viewMain, root):

        self.produtos = []
        self.viewMain = viewMain
        self.viewProduto = ProdutoView(root, self)


    def newproduto(self, nome, preco, quantidade):
        self.produtos.add(Produto(nome, preco, quantidade))

    def listprodutos(self):
        produtos = ()
        for produto in self.produtos:
            produtos.add(produto.__str__())
        return produtos

    def getproduto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto

class ProdutoView(tk.Frame):
    def __init__(self, root, ct):
        tk.Frame.__init__(self, root)
        self.createWidgets()
        self.ct = ct
        self.grid(row = 0, column = 0, sticky = "nsew")


    def createWidgets(self):

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.listProdutos
        self.hi_there.pack(side="top")

        self.lists = tk.PanedWindow(self)


    def say_hi(self):
        print("hi there, everyone!")

    def listProdutos(self):
        self.ct.listprodutos()



