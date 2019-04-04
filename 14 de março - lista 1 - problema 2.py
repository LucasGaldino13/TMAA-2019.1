#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
#14 de março de 2019 - Lista 1 - Problema 2 - "Múltiplos de X e Y"
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------

print('\n\t\tMúltiplos de X e Y')

a1 = int(input('digite um valor: ')) # Valor 1
b1 = int(input('digite um valor: ')) # Valor 2
l = int(input('digite um valor maximo dos multiplos: ')) # Múltiplos abaixo desse valor

an = int(l // a1) # Números de múltiplos de um valor
la =[]

bn = int(l // b1) # Números de múltiplos de outro valor
lb = []

abn = int (l // (a1*b1)) # Números de múltiplos iguais aos dois valores
lab = []

i = 1
j = 1
k = 1

if l % a1 == 0: # Caso o resto for zero, retirar 1, pois o 'l' não faz parte da lista
    an = an - 1

if l % b1 == 0:
    bn = bn - 1
 
while len(la) < an : # Adicioando os múltiplos a lista (1° valor)
    la.append(a1*i)
    i = i + 1
    
    
print('\nOs múltiplos de {} abaixo de {} é ou são {}.'.format(a1, l, la), end = " ")

while len(lb) < bn : # Adicioando os múltiplos a lista (1° valor)
    lb.append(b1*j)
    j = j + 1

print('Os múltiplos de {} abaixo de {} é ou são {}'.format(b1, l, lb))

while len(lab) < abn : # Adicioando os múltiplos a lista (valores igual)
    lab.append(a1*b1*k)
    k = k + 1

s1 = sum(la) # somando a lista 1
s2 = sum(lb) # somando a lista 2
s12 = sum(lab) # somando a lista combinada de 1 e 2

s3 = 0
s3 = s1 + s2 - s12 # Calculando a soma dos múltiplos 

print('Portando a soma dos múltiplos de {} e {} é {}.'.format(a1, b1, s3))

saida = input('')
