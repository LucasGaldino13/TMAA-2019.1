#--------------------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#--------------------------------------------------------------------------------------------------
#21 de março de 2019 - Lista 2 - Problema 3 - "Qual é o maior fator primo do número 3852914583882?"
#--------------------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#--------------------------------------------------------------------------------------------------

print('\n\t\tQual é o maior fator primo do número 3852914583882?')

n = 3852914583882 # O número

primo = [] # Uma lista vazia para armazenar os fatores primos
p = 2 # Primeiro primo

while n > 1: # Enquanto o número for maior que 1
	if n%p == 0: # Se o número for multiplo de p
		n = n/p # n será igual a n sobre p
		primo.append(p) # Insere p na lista
		
	else:
		p += 1 # Caso o número não seja multiplo de p, p é acrescido 1

print ('\nO maior fator primo do número 3852914583882 é {}.'.format(primo[len(primo)-1])) # Mostrando o resultado

saida = input()
