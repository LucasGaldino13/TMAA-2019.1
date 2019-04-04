#--------------------------------------------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#--------------------------------------------------------------------------------------------------------------------------
#21 de março de 2019 - Lista 2 - Problema 2 - "Soma dos termos ímpares da sequencia de Fibonacci, cujo valor não exceda X"
#--------------------------------------------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#--------------------------------------------------------------------------------------------------------------------------
print('\n\tQual a soma dos termos ímpares da sequencia de Fibonacci, cujo valor não exceda X?')

x = int(input
        ('Digite um valor máximo para os termos ímpares: '))
f1 = 1 # Primeiro termo
f2 = 1 # Segundo termo
soma = 0

while f2 <= x: # Condição para que não passe de x
    if f2 % 2 == 1: # Testando se o número da sequência é ímpar
        soma += f2 # Somando os ímpares
    f1, f2 = f2, f1 + f2 # Obtendo o promixo número da sequência
    
print ('\nA soma dos termos ímpares da sequencia de Fibonacci, cujo valor não exceda 4000000 é: {}.'.format(soma)) # Mostrando o resultado

saida = input()
