from Model.Produto import Produto
import tkinter as tk
from tkinter import messagebox
from Model.DataStorage import DataStorage


class ProdutoController:

    def __init__(self, viewMain, root):

        self.produtos = []

        self.main = viewMain
        self.viewProduto = ProdutoView(root, self)
        self.dstorage = DataStorage()
        self.carregarprodutos()


    def newproduto(self, nome, preco, quantidade=0):
        if not self.getproduto(nome):
            self.produtos.append(Produto(nome, preco, quantidade))
            self.salvarprodutos()
        else:
            messagebox.showinfo("Erro", "Um produto com esse nome já existe")

    def listprodutos(self):
        rprodutos = []
        for produto in self.produtos:
            rprodutos.append(produto.__str__())
        return rprodutos


    def getproduto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return False

    def editaproduto(self, nome, preco, quantidade=0):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.nome = nome
                produto.preco = preco
                produto.quantidade = quantidade
                self.viewProduto.listprodutos()
                self.salvarprodutos()
                return messagebox.showinfo("Info", "Produto atualizado com sucesso")

        return messagebox.showinfo("Erro", "Produto não encontrado")

    def entrada(self, entradas):
        for entry in entradas:
            for produto in self.produtos:
                if produto.nome == entry[0]:
                    print(produto)
                    produto.quantidade += int(entry[1])
                    print(produto)
        self.salvarprodutos()


    def saida(self, saidas):
        for entry in saidas:
            for produto in self.produtos:
                if produto.nome == entry[0]:
                    produto.quantidade -= int(entry[1])
        self.salvarprodutos()

    def carregarprodutos(self):
        self.produtos = self.dstorage.load()

    def salvarprodutos(self):
        self.dstorage.save(self.produtos)



class ProdutoView(tk.Frame):
    def __init__(self, root, ct):

        tk.Frame.__init__(self, root)
        self.ct = ct
        self.createWidgets()
        self.grid(row = 0, column = 0, sticky = "nsew")
        self.grid_columnconfigure(0, weight=1)



    def createWidgets(self):


        self.llista = tk.Label(self, text="Lista dos Produtos")
        self.llista.grid(row=0,column=0,sticky="ew", columnspan=2)

        self.lista = tk.Listbox(self, selectmode = "single")
        self.lista.grid(row=1,column=0, rowspan=2,sticky="ew", columnspan=2)


        self.leditar = tk.Label(self, text="Editar ou Adicionar Produtos :")
        self.leditar.grid(row=3, column=0, sticky="ew", columnspan=2)

        self.lnome = tk.Label(self, text="Nome : ")
        self.lnome.grid(row=4, column=0, sticky="w")
        self.nome = tk.Entry(self)
        self.nome.grid(row = 4, column =1, sticky="nsew", pady=5, padx=5)

        self.lvalor = tk.Label(self, text="Preço : ")
        self.lvalor.grid(row=5, column=0, sticky="w")
        self.valor = tk.Entry(self)
        self.valor.grid(row = 5, column = 1, sticky="ew", pady=5, padx=5)

        self.novo = tk.Button(self, text="Novo", command=self.newproduto)
        self.novo.grid(row = 6, column = 0, sticky="ew" ,pady=5, padx=5, columnspan=2)

        self.salva = tk.Button(self, text="Editar", command=self.salvarproduto)
        self.salva.grid(row = 7, column = 0,sticky="ew", pady=5, padx=5, columnspan=2)

        self.voltar = tk.Button(self, text="Voltar", command=self.ct.main.tomain)
        self.voltar.grid(row=8, column=0, sticky="ew", pady=5, padx=5, columnspan=2)

        self.listprodutos()

    def listprodutos(self):

        rprodutos = self.ct.listprodutos()
        self.lista.delete(0, "end")
        for produto in rprodutos:
            self.lista.insert("end", produto)

    def newproduto(self):

        if self.nome.get()=="" or self.valor.get()=="":
            messagebox.showinfo("Erro", "Favor preencher todos os valores")
        else:
            self.ct.newproduto(self.nome.get(), int(self.valor.get()))
            self.listprodutos()
            self.nome.delete(0, "end")
            self.valor.delete(0, "end")

    def salvarproduto(self):
        self.ct.editaproduto(self.nome.get(), int(self.valor.get()))


