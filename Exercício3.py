# Leia uma frase e imprima o total de vogais, o total de brancos e o total do resto.
vogal = branco = resto = 0
frase = str(input("Escreva uma frase: "))
for i in range(0,len(frase)):
    if(frase[i]==" "):
        branco += 1
    elif(frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u"):
        vogal += 1
    else:
        resto += 1
print("Numero de vogais: ",vogal)
print("Numero de brancos: ",branco)
print("Numero do resto: ",resto)
