import tkinter as tk


class MainView(tk.Frame):

    def __init__(self, root, ct):
        tk.Frame.__init__(root)
        self.startUI()
        self.ct = ct

    def startUI(self):

        botaoProdutos = tk.Button(self, text = "Produtos", command = self.toProdutos , padx = 5 , pady = 5)
        botaoProdutos.pack(side = "top")

    def toProdutos(self):
        self.ct.toProdutos()


def start(ct):
    ct = ct
    root = tk.Tk()
    main = MainView(root, ct)
    main.tkraise()
    root.mainloop()
    return main







