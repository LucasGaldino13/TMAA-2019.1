#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
#Lista 4 - Problema 3
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------
def abrirArq():
    l = []
    with open('zeroseuns.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                l.append(list(map(int(line.split(','))))
    return l

def completar(matriz):
    NumZerosLinha = []
    print("matriz original\n")
                         
    for g in range(len(matriz)):
        print(matriz[g])
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            if matriz[i][k] == 0:
                NumZerosLinha.append(1)
        if len(NumZerosLinha) == 1:
            return MatrizToda(matriz)
        
        for j in range(len(matriz[i])):
            if matriz[i][j] == int(0):
                for h in range(len(matriz[i])):
                    if matriz[i][-h] == int(0):
                        for t in range(len(matriz[i])-h):
                            if t > j:
                                matriz[i][t] = 0
            else:
                pass
    print("\n"*7,"nova matriz\n")
    return matriz

def Matrizcompleta(matriz):
    print("\n"*7,"nova matriz (com zero)\n")
    for j in range(len(matriz)):
        for i in range(len(matriz[j])):
            matriz[j][i] = 0
        print(matriz[j])
                         
l = abrirArq()
completar(l)
