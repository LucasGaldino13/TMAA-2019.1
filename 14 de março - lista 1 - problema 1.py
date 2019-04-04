#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
#14 de março de 2019 - Lista 1 - Problema 1 - "Uma calculadora de equação do 2° grau"
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------

print ("\n\t\t uma calculadora de equação do 2° grau") # Informar ao usuário o intuito do programa

print ("\nLembre-se que a equação do 2° grau é da forma: ax^2 + bx + c ") # Mostrar a forma de uma equação do 2° grau ao usuário

a = float(input("\nDigite um valor para o coeficiente 'a': ")) # Pedir ao usuário que digite o valor do coeficiente "a"


if a == 0 : # Caso o usuário digite um valor para 'a' igual a zero
    print ("\tSe o coeficiente 'a' for igual a zero, a equação não é do 2° grau.\n") # Informar que o valor do coeficiente 'a' não pode ser zero 

if a != 0 : # Caso o usuário digite um valor para 'a' diferente de zero
    
    b = float(input("\nDigite um valor para o coeficiente 'b': ")) # Pedir ao usuário que digite o valor do coeficiente "b"
    c = float(input("\nDigite um valor para o coeficiente 'c': ")) # Pedir ao usuário que digite o valor do coeficiente "c"
    
delta = b**2 - 4*a*c # Calculando o valor de delta

if delta > 0 : # Caso delta for maior que zero
     print ("\n\tComo o delta é {}, ou seja, um valor positivo, há duas raízes reais.".format(delta))
     
     x1 = (-b + (delta ** (1/2)) )/2*a # Calculando as duas raízes reais
     x2 = (-b - (delta ** (1/2)) )/2*a
     
     print ("As raizes reais são {} e {}.\n".format(x1, x2)) # Mostrando as raízes ao usuário


if delta == 0 : # Caso delta for igual a zero
    print ("\n\tComo o delta é {}, há uma única raíz real.".format(int(delta)))
                                                                   
    x = (-b + (delta ** (1/2)) )/2*a # Calculando a raíz real
    
    print ("A raiz real é {}.\n".format(x)) # Mostrando a raíz real ao usuário

    

if delta < 0 : # Caso delta for menor que zero
    print ("\n\tComo o delta é {}, ou seja, um valor negativo, há duas raízes complexas.".format(delta))

    delta = -delta

    x1c = (-b + (delta ** (1/2)) )/2*a # Calculando as duas raízes complexas 
    x1c = round (x1c, 2)
    x2c = (-b - (delta ** (1/2)) )/2*a
    x2c = round (x2c, 2)
    
    print ("As raizes complexas são {}i e {}i.\n".format(x1c, x2c)) # Mostrando as duas raízes complexas ao usuário
    
saida = input('')



