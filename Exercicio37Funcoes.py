def criar_matriz(linha,coluna):
    matriz = []
    for i in range(0,linha):
        a = []
        for j in range(0,coluna):
            a.append(int(input("[{:d}][{:d}]: ".format(i,j))))
        matriz.append(a)
    return matriz

def imprimir_matriz(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            print("[{:^5d}]".format(matriz[i][j]), end='')
        print()

def calcular_determinante_3x3(matriz):
    det = []
    determinante = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    coluna = coluna + 2
    for i in range(0,linha):
        a = []
        for j in range(0,coluna):
            if(j == 0 or j == 1 or j == 2):
                a.append(matriz[i][j])
            elif(j == 3):
                a.append(matriz[i][0])
            elif(j == 4):
                a.append(matriz[i][1])
        det.append(a)
    print("Nova Matriz Criada para Calcular Determinante:")
    imprimir_matriz(det)
    d1 = d2 = d3 = d4 = d5 = d6 = 1
    for i in range(0,linha):
        for j in range(0,coluna):
            if(i==j):
                d1 *= det[i][j]
            if(i-j==-1):
                d2 *= det[i][j]
            if(i-j==-2):
                d3 *= det[i][j]
            if(i+j==2):
                d4 *= det[i][j]
            if(i+j==3):
                d5 *= det[i][j]
            if(i+j==4):
                d6 *= det[i][j]
    determinante = ((d1+d2+d3)-(d4+d5+d6))
    return determinante