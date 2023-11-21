#Ler um vetor de números inteiros de 30 posições. 
#Depois, ler um número inteiro X, imprimir quantas vezes o número X aparece no vetor.
vetor = []
N = 30
cont = 0
print("Preencha o vetor com um numero inteiro: ")
for i in range(0,N):
    print("[{:d}] sera preenchido pelo numero:".format(i))
    vetor.append(int(input()))
print("Vetor atual: ",vetor)
print("Ordendando vetor...")
for i in range(0,N-1):
    for j in range(i+1,N):
        if (vetor[i]>vetor[j]):
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux
print("Vetor Ordenado!")
print("Vetor novo: ", vetor)
numero = int(input("Escreva o numero que quer checar se há no vetor:"))
for i in range(0,N):
    if vetor[i] == numero:
        cont += 1
print("O numero de vezes que {:d} aparece no vetor é: {:d} ".format(numero,cont))
