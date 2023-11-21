#Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas posições. 
#Imprima o vetor original e o vetor trocado.
#VetorOriginal = VetorTrocado = []
VetorOriginal = []#[0,2,3,4]
N = 16
add = N//2
for i in range(0,N): 
    VetorOriginal.append(int(input("Escreva um numero:")))
print("Vetor Original: ",VetorOriginal)
for i in range(0,add):
    print("i = ",i)
    for j in range(i+add,N):
        print("j = ",j)
        aux = VetorOriginal[i]
        VetorOriginal[i] = VetorOriginal[j]
        VetorOriginal[j] = aux
print("Vetor Trocado: ",VetorOriginal)