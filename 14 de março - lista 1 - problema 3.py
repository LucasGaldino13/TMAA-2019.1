#--------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#--------------------------------------------------------------------------------
#14 de março de 2019 - Lista 1 - Problema 3 - "Soma de Vetores de N coordenadas"
#--------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#--------------------------------------------------------------------------------

print('\n\t\tSoma de vetores de N coordenadas')

N = int(input('\nDigite o númro de coordenadas: ')) # Número de coordenda
v1 = list(map(int, input('Digite as coordenadas do vetor 1 (dê espaço entre cada cordenada): ').split())) # Coordenadas do vetor 1
v2 = list(map(int, input('Digite as coordenadas do vetor 2 (dê espaço entre cada cordenada): ').split())) # Coordenadas do vetor 2
vsoma = [0]*N # Coordenadas do vetor da soma

if len(v1) != N or len(v2) != N : # Caso os vetores nãotenham mesmo número de coordenadas ou o número de coordenadas de qualquer vetor não seja igual a N
    print('\nOs vetores possuem {} cordenada(s). Foi digitado um número diferente de coordenadas.\n'.format(N))
    import sys
    sys.exit(0) # O programa é encerrado

for i in range(N) : # Somando as coordenadas
    vsoma[i] = v1[i] + v2[i]
        
print('\n\tO resultado da soma do vetor 1 com vetor 2 é ( ', end = '')
        
for item in vsoma : # Mostando as coordenadas da soma dos vetores
    print(item, end = ' ')

print(')')

saida = input('')

