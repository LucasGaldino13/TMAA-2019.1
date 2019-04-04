
#---------------------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#---------------------------------------------------------------------------------------------------
#14 de março de 2019 - Lista 1 - Problema 4 - "Quais os postos no raio de X Km da minha localização"
#---------------------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#---------------------------------------------------------------------------------------------------

l = [(92,4), (33,50), (42,17), (24,22), (11,4), (15,44), (86,12), (29,11), (1,3), (31,33),
     (2,45), (1, 22), (4,44), (0,37), (22,0), (66,82), (76,99), (55,97), (69,76), (76,90)] # Lista de pontos

print('\n\t\tQuais os postos no raio de X Km da minha localização')

x = float(input('\nDigite a primeira coordenada que você está: ')) # Primeira coordenada
y = float(input('Digite a segunda coordenada que você está: ')) # Segunda coordenada

pi = [x,y] # Ponto inicial

r = float(input('Digite a distância máxima que deseja andar: ')) # Raio (distância)

print('\n\tOs postos que você pode ir são: ', end = "")

n = 0

for p in (l) :
    d = ((pi[0]-p[0])**2 + (pi[1]-p[1])**2)**(1/2) # Calculando a distância de pi até os postos
    if d <= r :
        print(p, end = " ")# Mostrando os postos
        n = n + 1
if n == 0:
    print('\nnão há nenhum posto dentro do raio de distância dado.')
    

    
saida = input()

