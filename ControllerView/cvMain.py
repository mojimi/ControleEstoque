import tkinter as tk
import ControllerView.cvProduto as viewProduto

class Main:
    def __start__(self):

        self.rooti = tk.Tk()
        self.root = tk.Frame(self.rooti)

        self.root.pack(side="top", fill="both", expand=True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.viewProduto = viewProduto.ProdutoController(self, self.root)
        self.viewMain = MainView(self, self.root)

        self.viewMain.tkraise()
        self.viewMain.master.master.title("Tela Principal")
        self.rooti.mainloop()



    def toprodutos(self):

        self.viewProduto.viewProduto.tkraise()

    def tomain(self):

        self.viewMain.tkraise()


class MainView(tk.Frame):

    def __init__(self, ct, root):
        tk.Frame.__init__(self,root)
        self.startUI()
        self.ct = ct
        self.grid( row = 0 , column = 0, sticky = "nsew")



    def startUI(self):

        botaoProdutos = tk.Button(self, text = "Produtos", command = self.toprodutos , padx = 5 , pady = 5)
        botaoProdutos.pack(side = "top")

        botaoEntrada = tk.Button(self, text="Entrada", command=self.toentrada, padx=5, pady=5)
        botaoEntrada.pack(side="top")

        botaoSaida = tk.Button(self, text="Saída", command=self.tosaida, padx=5, pady=5)
        botaoSaida.pack(side="top")

    def toprodutos(self):
        self.ct.toprodutos()
    def toentrada(self):
        return
    def tosaida(self):
        return



if __name__ == "__main__":
    main = Main()
    main.__start__()
