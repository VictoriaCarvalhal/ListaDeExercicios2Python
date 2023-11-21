vetor = [7.5, 8.0, 5.5, 9.0, 4.5, 8.0, 5.5, 6.0, 10.0]
valor = float(input('Entre com o valor a procurar: '))
posicoes = []
for i in range(0, len(vetor)):
    if vetor[i] == valor:
        posicoes.append(i)
if len(posicoes) == 1:
    print('Valor encontrado na posição: ', posicoes)
elif len(posicoes) != 0:
    print('Valor encontrado nas posições: ', posicoes)
else:
    print('Valor não encontrado.')
