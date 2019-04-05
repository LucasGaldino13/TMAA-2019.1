#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
#21 de março de 2019 - Lista 2 - Problema 4 - "Número por extenso"
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------

print('\n\t\tNúmero por extenso')

# Fazendo as listas

n1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze',
       'dezessies', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n2 = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

n3 = ('','cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novencentos')

# Condições

while True:
    numero = int(input('Digite um número: '))
    
    if 0<= numero <=19:
        print(f'\nFoi digitado o número {n1[numero]}')
        break
    

    if 20<= numero <=99:
        numero1 = numero // 10
        numero2 = numero % 10
        print(f'\nFoi digitado o número {n2[numero1]} e {n1[numero2]}')
        break
    

    if 100 <= numero <=999:
        numero1 = numero // 100
        numero2 = ((numero // 10) // 10)
        numero3 = numero % 10
        print(f'\nFoi digitado o número {n3[numero1]} e {n2[numero2]} e {n1[numero3]}')
        break

    if 1000<= numero <=99999:
        numeromil = numero // 1000
        numero1 = (((numero // 10) // 10) % 10)
        numero2 = ((numero // 10) % 10)
        numero3 = numero % 10
        print(f'\nFoi digitado o número {numeromil} mil e {n3[numero1]} e {n2[numero2]} e {n1[numero3]}')
        break

    else :
        print('\nValor inválido. Você deve digitar um valor entre 0 e 99999')

saida = input('')





