#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
#14 de março de 2019 - Lista 4 - Problema 1 
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------

mat = [] 
m = n = 0

# Lendo uma matriz em formato TXT
def LendoMatriz():
  global m, n, mat
  arq = open('dado.txt')
  conteudo = arq.read()
  numeros = conteudo.split()

  m = int(numeros[0])
  n = int(numeros[1])

  print("A matriz tem {} linhas e {} colunas\n".format(m,n))

  for i in range(m):
    linha = []
    for j in range(n):
      try:
        linha += [float(numeros[2 + i*m + j])]
      except ValueError as err:
        print(err)
        linha += ['NaN']
    mat += [linha]

  print(mat)
  print('\n')
  
# Alinhando a matriz 
def Print_Matriz_Alinhada_Fixa():
  print('MATRIZ:\n')  
  print("+","-"*17,"+","-"*17,"+","-"*17,"+")
  for i in range(m):
    print("|",end=" ")
    for j in range(n):
      print(" {0:^15f} ".format(mat[i][j]), end=" | ")
    print() 
    print("+","-"*17,"+","-"*17,"+","-"*17,"+")
  
LendoMatriz()

Print_Matriz_Alinhada_Fixa()
