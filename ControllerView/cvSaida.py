import tkinter as tk
from tkinter import messagebox


class SaidaController:

    def __init__(self, viewMain, root):

        self.saidas = []

        self.main = viewMain
        self.viewSaida = SaidaView(root, self)


    def getproduto(self, nome):
        return self.main.viewProduto.getproduto(nome)

    def listsaidas(self):
        return self.saidas


class SaidaView(tk.Frame):
    def __init__(self, root, ct):

        tk.Frame.__init__(self, root)
        self.ct = ct
        self.createWidgets()
        self.grid(row = 0, column = 0, sticky = "nsew")
        self.grid_columnconfigure(0, weight=1)



    def createWidgets(self):


        self.llista = tk.Label(self, text="Lista saida :")
        self.llista.grid(row=0,column=0,sticky="ew", columnspan=2)

        self.lista = tk.Listbox(self, selectmode = "single")
        self.lista.grid(row=1,column=0, rowspan=2,sticky="ew", columnspan=2)


        self.leditar = tk.Label(self, text="Adicionar produto")
        self.leditar.grid(row=3, column=0, sticky="ew", columnspan=2)

        self.lnome = tk.Label(self, text="Nome : ")
        self.lnome.grid(row=4, column=0, sticky="w")
        self.nome = tk.Entry(self)
        self.nome.grid(row = 4, column =1, sticky="nsew", pady=5, padx=5)

        self.lquantidade = tk.Label(self, text="Quantidade : ")
        self.lquantidade.grid(row=5, column=0, sticky="w")
        self.quantidade = tk.Entry(self)
        self.quantidade.grid(row = 5, column = 1, sticky="ew", pady=5, padx=5)

        self.novo = tk.Button(self, text="Adicionar", command=self.adicionar)
        self.novo.grid(row = 6, column = 0, sticky="ew" ,pady=5, padx=5, columnspan=2)

        self.salva = tk.Button(self, text="Salvar Saída", command=self.salvar)
        self.salva.grid(row = 7, column = 0,sticky="ew", pady=5, padx=5, columnspan=2)

        self.voltar = tk.Button(self, text="Voltar", command=self.ct.main.tomain)
        self.voltar.grid(row=8, column=0, sticky="ew", pady=5, padx=5, columnspan=2)


    def listsaidas(self):

        rsaidas = self.ct.listsaidas()
        self.lista.delete(0, "end")
        for saida in rsaidas:
            self.lista.insert("end", "Produto : " + saida[0] + " | Quantidade : " +  saida[1])


    def adicionar(self):

        if self.nome.get() == "" or self.quantidade.get() == "":
            messagebox.showinfo("Erro", "Favor preencher todos os valores")
        elif not (self.ct.getproduto(self.nome.get())):
            return messagebox.showinfo("Erro", "Não há produto com esse nome no inventário")
        else:
            self.ct.saidas.append((self.nome.get(), self.quantidade.get()))
            self.listsaidas()

            self.nome.delete(0, "end")
            self.quantidade.delete(0, "end")

    def salvar(self):
        self.ct.main.viewProduto.saida(self.ct.saidas)
        self.ct.saidas = []
        self.ct.main.tomain()
        messagebox.showinfo("Info", "Saída realizada com sucesso")
