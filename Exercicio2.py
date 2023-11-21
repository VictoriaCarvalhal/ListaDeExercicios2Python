#Leia um vetor de 40 posições e conte quantos elementos pares se encontram no
#vetor.
vetor = []
pares = 0
N = 40
for i in range(0,N):
    vetor.append(int(input("Escreva um numero:")))
    if(vetor[i]%2==0):
        pares += 1
print("O numero de elementos pares dentro desse vetor é: ",pares)