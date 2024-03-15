from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt


def main():
    leitor = LeitorArquivo('data.txt')
    listavalores = leitor.getValores()
    print(listavalores)

    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    
    plt.plot(listavalores)
    plt.show()

main()
