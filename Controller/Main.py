from Controller.ProdutoController import ProdutoController
from View.MainView import start

class Main:
    def __start__(self):

        self.ctProduto = ProdutoController()

        self.viewMain = start(self)

    def toProdutos(self):

        self.ctProduto.toProdutos()



if __name__ == "__main__":
    main = Main()
    main.__start__()
