#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
#14 de março de 2019 - Lista 4 - Problema 2
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------

# Definição da Classe Pilha
class CPilha:
    def __init__(self):
        self.pilha = []
        

    def push(self, dado):
        self.pilha.append(dado)

    def pop(self):
        return self.pilha.pop()

    def Print(self):
        print(self.pilha)

class CPino(CPilha):
    def __init__(self, n = 0):
        CPilha.__init__(self)
        for i in range(n,0,-1):
            self.push(i)

def PrintHanoi():
    print('Pino 1:', pino1.pilha)
    print('Pino 2:', pino2.pilha)
    print('Pino 3:', pino3.pilha, '\n')

def MoveDisco(pino_origem, pino_destino):
    pino_destino.push(pino_origem.pop())
    

def Resolve2Discos(pino_origem, pino_destino, pino_intermediario):
    MoveDisco(pino_origem, pino_intermediario)
    MoveDisco(pino_origem, pino_destino)
    MoveDisco(pino_intermediario, pino_destino)

def ResolveHanoi_N_Discos(n, pino_origem, pino_destino, pino_intermediario):
    if n > 1:
        ResolveHanoi_N_Discos(n-1, pino_origem, pino_intermediario,pino_destino)
        MoveDisco(pino_origem, pino_destino)
        ResolveHanoi_N_Discos(n-1, pino_intermediario, pino_destino, pino_origem)
    else:
        MoveDisco(pino_origem, pino_destino)

        
x = int(input(print('Escolha um valor para n:')))

pino1 = CPino(x)
pino2 = CPino()
pino3 = CPino()
PrintHanoi()
ResolveHanoi_N_Discos(x,pino1,pino3,pino2)
PrintHanoi()

