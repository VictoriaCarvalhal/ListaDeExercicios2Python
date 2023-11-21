#Crie a função multiplica_matriz(mat1, mat2) que deve retornar o produto 
#de duas matrizes bidimensionais genéricas, sem alterar as matrizes originais. 
#A função deve imprimir uma mensagem de erro e retornar um vetor vazio ([]) caso não for possível realizar
# o produto das duas matrizes.
def main():
    import Exercicio13Funcoes as funcao
    linha = []
    coluna = []
    for i in range(0,2):
        linha.append(int(input("Escreva o numero de linhas da {:d} matriz: ".format(i+1))))
        coluna.append(int(input("Escreva o numero de colunas da {:d} matriz: ".format(i+1)))) 
        if(i==0):
            matriz1 = funcao.ler_matriz(linha[i],coluna[i])
            print("Primeira Matriz:")
            funcao.imprimir_matriz(matriz1)
        elif(i==1):
            matriz2 = funcao.ler_matriz(linha[i],coluna[i])
            print("Segunda Matriz:")
            funcao.imprimir_matriz(matriz2)
    matriznova = funcao.multiplica_matriz(matriz1,matriz2)
    print("Nova Matriz:")
    if(len(matriz1[0])==len(matriz2[0])):
        funcao.imprimir_matriz(matriznova)
    else:
        print([])
if __name__ == "__main__":
    main()

