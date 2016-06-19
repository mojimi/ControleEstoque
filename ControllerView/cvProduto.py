from Model.Produto import Produto
import tkinter as tk


class ProdutoController:

    def __init__(self, viewMain, root):

        self.produtos = []

        self.addProduto("banana", 50, 50)
        self.addProduto("ovo", 50, 50)

        self.viewMain = viewMain
        self.viewProduto = ProdutoView(root, self)



    def addProduto(self, nome, preco, quantidade):
        self.produtos.append(Produto(nome,preco,quantidade))

    def listProdutos(self):
        rProdutos = []
        for produto in self.produtos:
            rProdutos.append(produto.__str__())
        return rProdutos


    def getproduto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto

class ProdutoView(tk.Frame):
    def __init__(self, root, ct):

        tk.Frame.__init__(self, root)
        self.ct = ct
        self.createWidgets()
        self.grid(row = 0, column = 0, sticky = "nsew")


    def createWidgets(self):

        flista = tk.Frame(self)

        flista.pack(fill="both")

        self.lista = tk.Listbox(flista, selectmode = "SINGLE")
        self.lista.pack()

        self.nome = tk.Entry(self)
        self.nome.pack(side="top", padx = 10, pady = 10)

        self.valor = tk.Entry(self)
        self.valor.pack(side="top", padx = 10, pady = 10)

        self.novo = tk.Button(self, text="Novo", command=self.addProduto())
        self.novo.pack(side="top", padx = 10, pady = 10)

        self.salva = tk.Button(self, text="Salvar", command=self.salvarproduto())
        self.salva.pack(side="top", padx = 10, pady = 10)

        self.listProdutos()


    def listProdutos(self):
        rProdutos = self.ct.listProdutos()
        for produto in rProdutos:
            self.lista.insert("end", produto)

    def addProduto(self):
        return
    def salvarproduto(self):
        return


