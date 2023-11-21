def criar_matriz(linha,coluna):
    print("Criando uma matriz {:d}x{:d}: ".format(linha,coluna))
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
            print("[{:^5d}]".format(matriz[i][j]),end='')
        print()

def det_3x3(matriz):
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
    d1 = M2 = M3 = d4 = d5 = d6 = 1
    for i in range(0,linha):
        for j in range(0,coluna):
            if(i==j):
                d1 *= det[i][j]
            if(i-j==-1):
                M2 *= det[i][j]
            if(i-j==-2):
                M3 *= det[i][j]
            if(i+j==2):
                d4 *= det[i][j]
            if(i+j==3):
                d5 *= det[i][j]
            if(i+j==4):
                d6 *= det[i][j]
    determinante = ((d1+M2+M3)-(d4+d5+d6))
    return determinante

def criar_vetor(numero):
    vetor = []
    print("Criando uma vetor de {:d} elementos: ".format(numero))
    for i in range(0,numero):
        vetor.append(int(input("O valor do elemento {:d} é: ".format(i))))
    return vetor

def ler_vetor(vetor):
    for i in range(0,len(vetor)):
        print("[{:^5d}]".format(vetor[i]))

def Cramer(matriz,vetor):
    import copy
    matrizaux = copy.deepcopy(matriz)
    vetoraux = copy.copy(vetor)
    print("Resolvendo as icoquinitas por Cramer")
    resultado = []
    M1 = Calculo_Det_De_Cramer(matrizaux,vetoraux,1)
    print("M1: ")
    imprimir_matriz(M1)
    D1 = det_3x3(M1)
    print("D1: ",D1)
    M2 = Calculo_Det_De_Cramer(matrizaux,vetoraux,2)
    print("M2: ")
    imprimir_matriz(M2)
    D2 = det_3x3(M2)
    print("D2: ",D2)
    M3 = Calculo_Det_De_Cramer(matrizaux,vetoraux,3)
    print("M3: ")
    imprimir_matriz(M3)
    D3 = det_3x3(M3)
    print("D1: ",D3)
    D = det_3x3(matrizaux)
    print("D: ",D)
    if(D!=0):
        x = (D1//D)
        print("D1//D ==",x)
        resultado.append(x)
        y = (D2//D)
        print("D2//D ==",y)
        resultado.append(y)
        z = (D3//D)
        print("D3//D ==",z)
        resultado.append(z)
    else:
        print("Sistema impossível de resolver")
        impossivel = True
    return resultado

def Calculo_Det_De_Cramer(matriz,vetor,numero):
    numero = numero - 1
    aux = []
    for i in range(0,len(matriz)):
        a = []
        for j in range(0,len(matriz[0])):
            if((i==0 and j==numero)or(i==1 and j==numero)or(i==2 and j==numero)):
                a.append(vetor[i])
            else:
                a.append(matriz[i][j])
        aux.append(a)
    return aux 