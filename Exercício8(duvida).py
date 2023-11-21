#Considere um vetor de trajetórias de 9 elementos onde
#cada elemento possui o valor do próximo elemento a ser lido.
#indice: 0,1,2,3,4,5,6,7,8
#valor: 4,6,5,8,1,7,3,0,2
#Fazer um programa que leia esse vetor e imprima a trajetória correta:
#sequência de impressão 4, 1, 6, 3, 8, 2, 5, 7, 0.

vetor = [4,6,5,8,1,7,3,0,2]
tamanho = len(vetor)
#print("tamanho =",tamanho)
#for i in range(0,tamanho):
#    print("Indice = {:d} Valor = {:d}".format(i,vetor[i]))
aux1 = aux2 = 0
while(aux1 != tamanho):
        print(" {:d}".format(vetor[aux2]), end="")
        aux2 = vetor[aux2]
        aux1 += 1
        if(aux1 != tamanho):
            print(",", end="")
        elif(aux1 == tamanho):
            print(".", end="")
    