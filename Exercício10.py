MatrizOriginal = []
MatrizTransposta = []
linha = int(input("Quantas linhas a matriz terá: "))
coluna = int(input("Quantas colunas a matriz terá: "))
for i in range(0,linha):
    a = []
    for j in range(0,coluna):
        a.append(int(input("[{:d}][{:d}]:".format(i,j))))
    MatrizOriginal.append(a)
print("Matriz Original:")
for i in range(0,linha):
    for j in range(0,coluna):
        print(f'[{MatrizOriginal[i][j]:^5}]',end='')
    print()
for j in range(0,coluna):
    b = []
    for i in range(0,linha):
        b.append(MatrizOriginal[i][j])
    MatrizTransposta.append(b)
print("Matriz Transposta:")
for j in range(0,coluna):
    for i in range(0,linha):
        print(f'[{MatrizTransposta[j][i]:^5}]',end='')
    print()
