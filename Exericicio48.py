import Exericicio48Funcoes as funcoes
import copy
def main():
    num = int(input("Escreva um numero: "))
    vetor = copy.copy(funcoes.fat_primo(num))
    print("O vetor da decomposição desse numero em numeros primos é: ",vetor)

if __name__ == "__main__":
    main()