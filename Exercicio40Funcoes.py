def vetor_aleatorio(n):
    import random
    v = []
    for i in range(0,n):
        v.append(int(random.randrange(0,100)))
    return v

def arrumar_vetor(vet):
    n = len(vet)
    for i in range(n-1):
        for j in range(i+1,n):
            if(vet[i]>vet[j]):
                aux = vet[i]
                vet[i] = vet[j]
                vet[j] = aux