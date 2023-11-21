def main():
    import Exercicio40Funcoes as funcoes
    numero = 5
    vetor = funcoes.vetor_aleatorio(numero)
    print("Vetor atual:",vetor)
    funcoes.arrumar_vetor(vetor)
    print("Vetor arrumado:",vetor)

if __name__ == "__main__":
    main()