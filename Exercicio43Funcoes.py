def criar_matriz(linha,coluna):
    matriz = []
    for i in range(0,linha):
        a = []
        for j in range(0,coluna):
            a.append(int(input("[{:d}][{:d}]: ".format(i,j))))
        matriz.append(a)
    return matriz

def calcular_lado_do_triangulo(matriz):
    x = []
    y = []
    l = []
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if(j==0):
                x.append(matriz[i][j])
                print("Coordenada X {:d}: {:d}".format(i,x[i]))
            if(j==1):
                y.append(matriz[i][j])
                print("Coordenada Y {:d}: {:d}".format(i,y[i]))
            
    print("Lados do triangulo: ",l)
    return l

def calcular_semiperimetro(vetor):
    soma = 0
    for i in range(0,len(vetor)):
        soma += vetor[i]
    semiperimetro = soma//2 
    return semiperimetro