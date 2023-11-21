def convertor(frase):
    tamanho = len(frase)
    frasenova = frase
    for i in range(0,tamanho):
        if(frase[i] == "á" or frase[i] == "à" or frase[i] == "â" or frase[i]=="ã"):
            frasenova = frase.replace(frase[i],"a")
        elif(frase[i] == "é" or frase[i] == "ê"):
            frasenova =  frase.replace(frase[i], "e")
        elif(frase[i] == "í"):
            frasenova =  frase.replace(frase[i], "i")
        elif(frase[i] == "ú" or frase[i] == "ü"):
            frasenova =  frase.replace(frase[i], "u")
        elif(frase[i] == "ó" or frase[i] == "ô" or frase[i] == "õ"):
            frasenova = frase.replace(frase[i], "o")
        elif(frase[i] == "ç"):
            frasenova = frase.replace(frase[i], "c")
    return frasenova

def anagrama(frase1antiga,frase2antiga):
    frase1antiga = frase1antiga.lower()
    print("Frase 1 antiga: ",frase1antiga)
    frase2antiga = frase2antiga.lower()
    print("Frase 2 antiga: ",frase2antiga)
    frase1nova = convertor(frase1antiga)
    print("Frase 1 nova: ",frase1nova)
    frase2nova = convertor(frase2antiga)
    print("Frase 2 nova: ",frase2nova)
    anagrama = True
    tamanho1 = len(frase1nova)
    tamanho2 = len(frase2nova)
    if(tamanho1 == tamanho2):
        for i in frase1nova:
            if(frase2nova.find(i)<0):
                anagrama = False
    else:
        anagrama = False
    return anagrama

frase1 = str(input("Escreva uma frase: "))
frase2 = str(input("Escreva outra frase: "))
teste = anagrama(frase1,frase2)
if(teste):
    print("A segunda frase digitada é um anagrama da primeira frase digitada")
else:
    print("A segunda frase digitada não é um anagrama da primeira frase digitada")
