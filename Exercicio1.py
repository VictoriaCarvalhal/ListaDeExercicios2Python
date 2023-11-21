#Faça um programa para ler 50 valores de temperaturas em graus Celsius.
#Transformar essas temperaturas em Farenheit e imprimir a media das temperaturas
#em Celsius e Farenheit e quantas temperaturas ficaram acima da media em Farenheit
Celsius = []
Farenheit = []
somaCelsius = somaFarenheit = mediaCelsius = mediaFarenheit = numeroCelsius = numeroFarenheit = acimadamediaFarenheit = 0 
N = 50
for i in range(0,N):
    temp = float(input("Escreva uma temperatura em celcius: "))
    Celsius.append(temp)
    print("Temperatura escrita: ",Celsius[i])
    somaCelsius += Celsius[i]
    print("Soma de temperaturas Celsius: ",somaCelsius)
    numeroCelsius += 1
    print("Temperaturas adicionadas em celcius: ", numeroCelsius)
    convertor = (Celsius[i]*9/5)+32
    print("Temperatura convertida ", convertor)
    Farenheit.append(convertor)
    print("Temperatura no vetor Farenheit: ", Farenheit[i])
    somaFarenheit += Farenheit[i]
    print("Soma de temperaturas Farenheit: ", somaFarenheit)
    numeroFarenheit += 1
    print("Temperatura no vetor Farenheit: ", numeroFarenheit)
mediaCelsius = somaCelsius/numeroCelsius
mediaFarenheit = somaFarenheit/numeroFarenheit
for i in range(0,N):
    if(Farenheit[i]>mediaFarenheit):
        acimadamediaFarenheit += 1
print("A media das temperaturas em Celcius:{:f}\n"
      "A media das temperaturas em Farenheit:{:f}\n"
      "O numero de temperaturas acima da media em Farenheit:{:d}\n".format(mediaCelsius,mediaFarenheit,acimadamediaFarenheit))
