def main():
    import Exercicio43Funcoes as funcoes
    print("Escreva as coordenadas dos pontos do triangulo")
    coordenadas = funcoes.criar_matriz(3,2)
    lados = funcoes.calcular_lado_do_triangulo(coordenadas)
if __name__ == "__main__":
    main()