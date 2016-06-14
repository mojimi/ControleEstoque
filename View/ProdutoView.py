import tkinter as tk

class ProdutoView(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.pack()
        self.createWidgets()
        self.ct = controller
        self.mainloop()


    def createWidgets(self):

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.listProdutos
        self.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

    def listProdutos(self):
        self.ct.listprodutos