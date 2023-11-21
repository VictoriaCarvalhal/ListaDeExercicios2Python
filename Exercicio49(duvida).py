#Considere alguma sequência de elementos (difere de um mero conjunto de elementos por definir uma ordem entre
#os seus membros). Enumere, então, todas as subsequências não contínuas de uma dada sequência.
from itertools import combinations
num = int(input("Quantos numeros terão sua sequencia? (A sequencia deve ter mais de um numero) "))
try:
    if(num <=1):
        raise
except:
    while(num <=1):
        print("A sequencia deve ter mais de um numero")
        num = int(input("Escreva uma quantidade correspondente ao pedido: "))
vetor = []
print("Escreva os numeros: ")
for i in range(0,num):
    vetor.append(int(input("")))

print("Sua sequencia: ",vetor)
vetor2 = []
