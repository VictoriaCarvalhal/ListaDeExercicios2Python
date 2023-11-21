vetor = [7.5, 8.0, 5.5, 9.0, 4.5, 8.0, 5.5, 6.0, 10.0]
valor = float(input('Entre com o valor a procurar: '))
posicao = 0
achou = False
while (not achou) and (posicao < len(vetor)):
    if vetor[posicao] == valor:
        achou = True
    else:
        posicao = posicao + 1
if achou:
    print('Valor encontrado na posição {}.'.format(posicao))
else:
    print('Valor não encontrado.')
