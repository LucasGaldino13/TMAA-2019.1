import csv
ficheiro = open('perfil_eleitorado_ATUAL.csv')
conteudo = csv.reader(ficheiro)

#Caso queira imprimir a tabela
#for linha in conteudo: 
#   print (linha)

elementos = conteudo.split()
numelementos = len(elementos)

linhas = conteudo.splitlines()
numlinhas = len(linhas)

numcolunas = numelementos / numlinhas
 
print('\nA matriz tem {} linhas e {} colunas'.format(numlinhas, int(numcolunas)))
