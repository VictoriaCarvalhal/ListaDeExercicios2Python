#Um palíndromo é uma cadeia que pode ser lida de frente para trás e de trás para frente. 
#Ex: ‘SOMOS’ ‘1234321’. Implemente a função palindromo(palavra). O parâmetro palavra é uma string. 
#A função deverá retornar True se for um palíndromo e False caso contrário.
def palindromo(palavra):
    palin = True
    tamanho = len(palavra)
    for i in range(0,tamanho):
        aux = (i+1)*-1
        if(tamanho%2!=0):
            if(i==tamanho//2):
                break
        if(not(palavra[i]==palavra[aux])):
            palin = False
    return palin

palavra = str(input("Escreva uma palavra: "))
teste = palindromo(palavra)
if(teste):
    print("Essa palavra é um palindromo")
else:
    print("Essa palavra não é um palindromo")