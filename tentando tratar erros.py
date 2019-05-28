#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
#14 de março de 2019 - Lista 4 - Problema 1 - tentando tratar erros 
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------

mat = [] 
m = n = 0


def erros():
    arq = open('dado.txt')
    conteudo = arq.read()
    numeros = conteudo.split()
  
    if len(conteudo[0])!=2:
        raise IndexError('O documento está no formato errado.')
    
    for i in range(1,len(conteudo)):
        for q in range(conteudo[0][1]):
            assert(1 in bool(type(conteudo[i][q]==float))), "Um valor não é um ponto flutuante."
            
    if len(conteudo)!=conteudo[0][0]:
                   raise IndexError("identificador está incorrreto.")
                
    for i in range(1,len(conteudo)):
                   assert(1 in bool(len(conteudo[i]==conteudo[0][1]))),"identificador está incorreto."
erros()
