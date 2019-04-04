#--------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#--------------------------------------------------------------------------------
#21 de março de 2019 - Lista 2 - Problema 5 - "Soma e subtração de vetores"
#--------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#--------------------------------------------------------------------------------

print('\n\t\tSoma e subtração de vetores')


while True :
    
    o = input('\nEscolha uma opção\n1)Somar vetores\n2)Subtrair vetores\n3)Sair do programa\n')
    
    if o == '1' :
        N = int(input('\nDigite o númro de coordenadas: ')) # Número de coordendass
        v1 = list(map(int, input('Digite as coordenadas do vetor 1 (dê espaço entre cada cordenada): ').split())) # Coordenadas do vetor 1
        v2 = list(map(int, input('Digite as coordenadas do vetor 2 (dê espaço entre cada cordenada): ').split())) # Coordenadas do vetor 2
        vsoma = [0]*N # Coordenadas do vetor da soma

        if len(v1) != N or len(v2) != N : # Caso os vetores não tenham mesmo número de coordenadas ou o número de coordenadas de qualquer vetor não seja igual a N
            print('\nOs vetores possuem {} cordenada(s). Foi digitado um número diferente de coordenadas.\n'.format(N))
            break # O programa é encerrado

        for i in range(N) : # Somando as coordenadas
            vsoma[i] = v1[i] + v2[i]
            
                
        print('\n\tO resultado da soma do vetor 1 com vetor 2 é ( ', end = '')
                
        for item in vsoma : # Mostando as coordenadas da soma dos vetores
            print(item, end = ' ')

        print(')')
        break

    if o == '2' :
        N = int(input('\nDigite o númro de coordenadas: ')) # Número de coordenda
        v1 = list(map(int, input('Digite as coordenadas do vetor 1 (dê espaço entre cada cordenada): ').split())) # Coordenadas do vetor 1
        v2 = list(map(int, input('Digite as coordenadas do vetor 2 (dê espaço entre cada cordenada): ').split())) # Coordenadas do vetor 2
        vsub = [0]*N # Coordenadas do vetor da subtração

        if len(v1) != N or len(v2) != N : # Caso os vetores não tenham mesmo número de coordenadas ou o número de coordenadas de qualquer vetor não seja igual a N
            print('\nOs vetores possuem {} cordenada(s). Foi digitado um número diferente de coordenadas.\n'.format(N))
            break # O programa é encerrado

        for k in range(N) : # Subtraindo as coordenadas
            vsub[k] = v1[k] - v2[k]
                
        print('\n\tO resultado da subtração do vetor 1 com vetor 2 é ( ', end = '')
                
        for item in vsub : # Mostando as coordenadas da subtrações dos vetores
            print(item, end = ' ')
            
        print(')')
        break # O programa é encerrado
            
    if o == '3' :
        print('programa encerrado')
        break # O programa é encerrado
    else :
        print('\nOpção inválida, tente novamente!')

saida = input('')

