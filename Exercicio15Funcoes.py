def encontrar_valor(elemento,vetor):
    soma = 0
    for i in range(0,len(vetor)):
        if (vetor[i] == elemento):
            soma += 1
    return soma

def condensar_lista(lista):
    somas = []
    condensar = []
    for i in range(0,len(lista)):
        valor = lista[i]
        somas.append(encontrar_valor(valor,lista))
        if(lista[i]==lista[i-1]):
            continue
        else:
            print("O valor {:d} aparece {:d} vezes".format(valor,somas[i]))
            if(somas[i]==1):
                condensar.append(str(valor))
            else:
                condensar.append(str(valor)+"^"+str(somas[i]))
    return condensar