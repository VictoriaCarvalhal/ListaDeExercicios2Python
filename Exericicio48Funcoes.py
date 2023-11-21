import copy
def fat_primo(num):
    #print("Fatorando")
    decom = []
    prim = 2 
    checar = continuar = True
    aux = num
    while(continuar):
        cont = 0
        checar = checar_primo(prim)
        if(checar):
            #print("Prim: ",prim)
            while(aux%prim == 0):
                cont += 1
                aux = aux/prim
                #print("Aux: ",aux)
                #print("Cont: ",cont)
            primstr = str(prim)
            contstr = str(cont)
            decom.append(""+primstr+"^"+contstr+"")
            #print("Decomposição atual:",decom)
        prim += 1
        if(aux == 1):
            continuar = False
    return decom

def checar_primo(num):
    primo = True
    if(num==0 or num==1):
        primo = False
    else:
        for i in range (2,num):
            if(num%i == 0):
                primo = False
    return primo

#num = int(input("Escreva um numero: "))
#vetor = copy.copy(fat_primo(num))
