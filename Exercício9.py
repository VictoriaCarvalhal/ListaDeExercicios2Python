#Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições.
#Imprima a matriz no formato tradicional de linhas e colunas

matriz5x5 = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
#print('-='*30)
for i in range(0,5):
    for j in range(0,5):
        print(f'[{matriz5x5[i][j]:^5}]',end='')
    print()      