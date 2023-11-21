#Faça um programa que preencha uma matriz 3x3 com valores aleatórios e calcule o seu determinante.
# Uma vez a matriz lida, a parte que faz o cálculo do determinante não se pode ter mais de 4 linhas
# e não pode haver mais de três células especificadas por linha (em outras palavras, você não pode 
# colocar em uma única linha a fórmula do determinante).

def main():
    import Exercicio37Funcoes as funcoes
    determinante = 0
    linhas = 3
    colunas = 3
    print("O numero de linhas da matriz é: {:d}\nO numero de colunas da matriz é: {:d}".format(linhas,colunas))
    matriz = funcoes.criar_matriz(linhas,colunas)
    funcoes.imprimir_matriz(matriz)
    determinante = funcoes.calcular_determinante_3x3(matriz)
    print("Determinante igual a :",determinante)
if __name__ == "__main__":
    main()