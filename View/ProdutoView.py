import tkinter as tk

class ProdutoView(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.pack()
        self.createWidgets()
        self.ct = controller


    def createWidgets(self):

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.listProdutos
        self.hi_there.pack(side="top")

        self.lists = tk.PanedWindow(self)


    def say_hi(self):
        print("hi there, everyone!")

    def listProdutos(self):
        lista = self.ct.listprodutos

