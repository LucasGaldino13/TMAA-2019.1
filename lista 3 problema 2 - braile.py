def tabela(inicio = 10240, fim = 10495, tamanho = 5):
    
    print('+', '-'*8, '+', '-'*5, '+')
    print('TABELA DE BRAILE (todos os pontos)\n')
    print('+', '-'*8, '+', '-'*5, '+')
    print('|  Dec    ', '|  Chr  |')
    print('+', '-'*8, '+', '-'*5, '+')
    print('|  {0:03}   |   {0:1c}   |'.format(inicio))
 
    for k in range(inicio + 1, fim + 1):
        print('|  {0:03}   |   {0:1c}   |'.format(k))

        if (k+1) % tamanho == 0:
            print('+', '-'*8, '+', '-'*5, '+')
            print('\n')
            print('+', '-'*8, '+', '-'*5, '+')
        
tabela()
