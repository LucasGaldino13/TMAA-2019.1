#-----------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-----------------------------------------------------------------------------------
#21 de março de 2019 - Lista 2 - Problema 1 - "Qual a soma dos dígitos do número 2^1001?"
#-----------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-----------------------------------------------------------------------------------
print('\n\t\tQual a soma dos dígitos do número 2^1001?')

x = int(input('Digite um valor para x onde 2^x: ')) # Pedindo o valor de x

n = 2**x

soma = 0

while (n > 0): # Condição para até q n seja igual a zero
    
    r = n % 10 # Calculando o resto da divisão de n por 10
    n = n // 10 # n se torna o quociente da divisão de n por 10
    soma = soma + r # Adicionando o resto a soma
    
print("\n\tA soma dos dígitos de 2^1001 é:", soma) # Mostrando o resultado

saida = input()
