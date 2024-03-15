from leitorarquivo import LeitorArquivo

def main():
    leitor = LeitorArquivo('data.txt')
    listavalores = leitor.getValores()
    print(listavalores)

main()