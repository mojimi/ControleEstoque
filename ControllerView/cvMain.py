import tkinter as tk
import ControllerView.cvProduto as viewProduto
import ControllerView.cvEntrada as viewentrada
import ControllerView.cvSaida as viewsaida

class Main:
    def __start__(self):

        self.rooti = tk.Tk()
        self.rooti.geometry("300x400")
        self.root = tk.Frame(self.rooti)

        self.root.pack(fill="both", expand=True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.viewProduto = viewProduto.ProdutoController(self, self.root)
        self.viewMain = MainView(self, self.root)

        self.viewentrada = viewentrada.EntradaController(self, self.root)
        self.viewsaida = viewsaida.SaidaController(self, self.root)

        self.viewMain.tkraise()
        self.rooti.title("Tela Principal")
        self.rooti.mainloop()



    def toprodutos(self):

        self.viewProduto.viewProduto.tkraise()
        self.viewProduto.viewProduto.listprodutos()
        self.rooti.title("Tela Produtos")

    def tomain(self):

        self.viewMain.tkraise()
        self.rooti.title("Tela Principal")

    def toentrada(self):

        self.viewentrada.viewEntrada.tkraise()
        self.rooti.title("Tela Entrada")

    def tosaida(self):

        self.viewsaida.viewSaida.tkraise()
        self.rooti.title("Tela Saída")


class MainView(tk.Frame):

    def __init__(self, ct, root):
        tk.Frame.__init__(self,root)
        self.startUI()
        self.ct = ct
        self.grid(row=0, column=0 ,sticky = "nsew")
        self.grid_columnconfigure(0, weight=1)



    def startUI(self):

        titulo = tk.Label(self, text="Controle de Estoque", font=("Helvetica", 18))
        titulo.grid(row=0, column=0, stick="ew", pady=20)

        subt = tk.Label(self, text="Escolha uma das opções abaixo :")
        subt.grid(row=1, column=0, sticky="ew")

        botaoProdutos = tk.Button(self, text = "Produtos", command = self.toprodutos)
        botaoProdutos.grid(row = 2, column = 0, sticky="ew", padx=15, pady=15)

        botaoEntrada = tk.Button(self, text="Entrada", command=self.toentrada)
        botaoEntrada.grid(row = 3, column = 0, sticky="ew", padx=15, pady=15)

        botaoSaida = tk.Button(self, text="Saída", command=self.tosaida)
        botaoSaida.grid(row = 4, column = 0, sticky="ew", padx=15, pady=15)


    def toprodutos(self):
        self.ct.toprodutos()
    def toentrada(self):
        self.ct.toentrada()
    def tosaida(self):
        self.ct.tosaida()



if __name__ == "__main__":
    main = Main()
    main.__start__()
