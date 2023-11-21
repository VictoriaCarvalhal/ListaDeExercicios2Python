def criar_matriz(linha,coluna):
    print("Criando Matriz")
    matriz = []
    for i in range(0,linha):
        a = []
        for j in range(0,coluna):
            a.append(int(input("Escreva o valor da [{:d}][{:d}]: ".format(i,j))))
        matriz.append(a)
    return matriz
def ler_matriz(mat):
    print("Ler Matriz")
    linha = len(mat)
    coluna = len(mat[0])
    for i in range(0,linha):
        for j in range(0,coluna):
            print("[:^5d]".format(mat[i][j]))
        print()