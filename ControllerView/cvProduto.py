from Model.Produto import Produto
import tkinter as tk


class ProdutoController:

    def __init__(self, viewMain, root):

        self.produtos = []

        self.newproduto("banana", 50, 50)
        self.newproduto("ovo", 50, 50)

        self.viewMain = viewMain
        self.viewProduto = ProdutoView(root, self)



    def newproduto(self, nome, preco, quantidade):
        self.produtos.append(Produto(nome,preco,quantidade))

    def listprodutos(self):
        rprodutos = []
        for produto in self.produtos:
            rprodutos.append(produto.__str__())
        return rprodutos


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

        self.novo = tk.Button(self, text="Novo", command=self.newproduto())
        self.novo.pack(side="top", padx = 10, pady = 10)

        self.salva = tk.Button(self, text="Salvar", command=self.salvarproduto())
        self.salva.pack(side="top", padx = 10, pady = 10)

        self.listprodutos()


    def say_hi(self):
        print("hi there, everyone!")

    def listprodutos(self):

        rprodutos = self.ct.listprodutos()
        for produto in rprodutos:
            self.lista.insert("end", produto)
    def newproduto(self):
        return
    def salvarproduto(self):
        return


