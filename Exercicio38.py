#Implemente a função Cramer(matriz, vetor) que calcule as raízes de um sistema de 3 equações e 3 incógnitas 
#pela Regra de Cramer e retorna a solução na forma de um vetor. 
#Se não houver solução para o sistema, deve imprimir uma mensagem de erro e retornar um vetor vazio ([]).
# Sua função pode (e deve) chamar a função det(matriz) que retorna o valor do determinante da matriz. 

def main():
    import Exercicio38Funcoes as funcoes
    matriz = resultado = d = []
    impossivel = False
    matriz = funcoes.criar_matriz(3,3)
    print("Matriz dos coeficientes: ")
    funcoes.imprimir_matriz(matriz)
    d = funcoes.criar_vetor(3)
    print("Vetor dos resultados das equações:")
    funcoes.ler_vetor(d)
    resultado = funcoes.Cramer(matriz,d)
    print("Vetor Resultado Das Icognitas:")
    if(impossivel == False):
        funcoes.ler_vetor(resultado)
    else:
        print([])

if __name__ == "__main__":
    main()