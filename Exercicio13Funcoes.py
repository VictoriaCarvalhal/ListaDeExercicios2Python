import copy
def ler_matriz(lin,colu):
    matriz = []
    for i in range(0,lin):
        a = []
        for j in range(0,colu):
            a.append(int(input("[{:d}][{:d}]:".format(i,j))))
        matriz.append(a)
    return matriz

def imprimir_matriz(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            print(f'[{mat[i][j]:^5}]', end='')
        print()

def multiplica_matriz(mat1,mat2):
    diferente = False
    cont = 0
    matriz = []
    mat3 = copy.deepcopy(mat1)
    mat4 = copy.deepcopy(mat2)
    if(len(mat3[0])!=len(mat4)):
        print("Impossivel multiplicar! Dimensões não casam")
        return []
    else:
        for i in range(len(mat3)):
            a = []
            for j in range(len(mat4[0])):
                soma = 0
                for k in range(len(mat4)):
                    soma += mat3[i][k] * mat4[k][j]
                    #print("[{:d}][{:d}]*[{:d}][{:d}] = {:d}".format(i,k,k,j,mat3[i][k] * mat4[k][j]))
                    print("Soma = ",soma)
                a.append(soma)
            matriz.append(a)
        return matriz