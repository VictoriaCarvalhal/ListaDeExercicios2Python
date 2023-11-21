import copy

def mat_maior_10(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    print("Coluna da Matriz passada: {:d}\nLinha da Matriz passada: {:d}".format(linhas,colunas))
    maiorque10 = []
    for i in range(0,linhas):
        for j in range(0,colunas):
            if(matriz[i][j]>10):
                maiorque10.append(matriz[i][j])
    return maiorque10

def criarmatriz(linha,coluna):
    matrizgenerica = []
    for i in range(0, linha):
        a = []
        for j in range(0, coluna):
            a.append(int(input("[{:d}][{:d}]: ".format(i, j))))
        matrizgenerica.append(a)
    print("Matriz escrita: ")
    for i in range(0, linha):
        for j in range(0, coluna):
            print(f'[{matrizgenerica[i][j]:^5}]', end='')
        print()
    return matrizgenerica

matriz = []
linha = int(input("Numero de linhas da matriz: "))
coluna = int(input("Numero de colunas da matriz: "))
matriz = copy.deepcopy(criarmatriz(linha,coluna))
valoresmaioresque10 = copy.copy(mat_maior_10(matriz))
print("Os valores maiores que 10 dentro da matriz foram: ",valoresmaioresque10)