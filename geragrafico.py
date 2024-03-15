from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt


def main():
    leitor = LeitorArquivo('data.txt')
    listavalores = leitor.getValores()
    print(listavalores)

    plt.plot(listavalores)
    plt.show()

main()
