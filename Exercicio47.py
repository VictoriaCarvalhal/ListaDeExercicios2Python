#Escreva um programa para converter números inteiros, 
#menores do que 4000 e escritos em algarismos arábicos, para romanos.

try:
    num = int(input("Escreva um numero menor que 4000: "))
    if(num>=4000):
        raise
except:
    print("Numero escrito é maior ou igual a 4000")
    num = int(input("Escreva o numero de novo: "))
    while(num>=4000):
        print("Numero escrito é maior ou igual a 4000")
        num = int(input("Escreva o numero de novo: "))
numstr = str(num)
tamanho = len(numstr)
vetor = []
#print("Tamanho do numero: ",tamanho)
for i in range(1,tamanho+1):
    resto = num%10**1
    num = num//10
    #print("O resto: ",resto)
    #print("O novo numero: ",num)
    vetor.append(resto)
#print("O vetor: ",vetor)
for i in range(0,tamanho):
    if(vetor[i]== 0):
            vetor[i] = ""
    elif(i==0):
        #print("Unidade em decimal:",vetor[i])
        if(vetor[i]==1):
            vetor[i] = "I"
        if(vetor[i]==2):
            vetor[i] = "II"
        if(vetor[i]==3):
            vetor[i] = "III"
        if(vetor[i]==4):
            vetor[i] = "IV"
        if(vetor[i]==5):
            vetor[i] = "V"
        if(vetor[i]==6):
            vetor[i] = "VI"
        if(vetor[i]==7):
            vetor[i] = "VII"
        if(vetor[i]==8):
            vetor[i] = "VIII"
        if(vetor[i]==9):
            vetor[i] = "IX"
        #print("Unidade em romanos: ",vetor[i])
    if(i==1):
        #print("Dezena em decimal:",vetor[i])
        if(vetor[i]==1):
            vetor[i] = "X"
        if(vetor[i]==2):
            vetor[i] = "XX"
        if(vetor[i]==3):
            vetor[i] = "XXX"
        if(vetor[i]==4):
            vetor[i] = "XL"
        if(vetor[i]==5):
            vetor[i] = "L"
        if(vetor[i]==6):
            vetor[i] = "LX"
        if(vetor[i]==7):
            vetor[i] = "LXX"
        if(vetor[i]==8):
            vetor[i] = "LXXX"
        if(vetor[i]==9):
            vetor[i] = "XC"
        #print("Dezena em romanos: ",vetor[i])
    if(i==2):
        #print("Centena em decimal:",vetor[i])
        if(vetor[i]==1):
            vetor[i] = "C"
        if(vetor[i]==2):
            vetor[i] = "CC"
        if(vetor[i]==3):
            vetor[i] = "CCC"
        if(vetor[i]==4):
            vetor[i] = "CD"
        if(vetor[i]==5):
            vetor[i] = "D"
        if(vetor[i]==6):
            vetor[i] = "DC"
        if(vetor[i]==7):
            vetor[i] = "DCC"
        if(vetor[i]==8):
            vetor[i] = "DCCC"
        if(vetor[i]==9):
            vetor[i] = "CM"
        #print("Centena em romanos: ",vetor[i])
    if(i==3):
        #print("Milhar em decimal:",vetor[i])
        if(vetor[i]==1):
            vetor[i] = "M"
        if(vetor[i]==2):
            vetor[i] = "MM"
        if(vetor[i]==3):
            vetor[i] = "MMM"
        #print("Milhar em romanos: ",vetor[i])
if(tamanho == 4):
    print("Numero convertido para numeros romanos:{:s}{:s}{:s}{:s}".format(vetor[3],vetor[2],vetor[1],vetor[0]))
elif(tamanho == 3):
    print("Numero convertido para numeros romanos:{:s}{:s}{:s}".format(vetor[2],vetor[1],vetor[0]))
elif(tamanho == 2):
    print("Numero convertido para numeros romanos:{:s}{:s}".format(vetor[1],vetor[0]))
elif(tamanho == 1):
    print("Numero convertido para numeros romanos:{:s}".format(vetor[0]))