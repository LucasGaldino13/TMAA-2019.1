def tabela(inicio = 945, fim = 969, tamanho = 5):
    
    print('+', '-'*6, '+', '-'*5, '+')
    print('TABELA DE LETRAS GREGAS\n')
    print('+', '-'*6, '+', '-'*5, '+')
    print('|  Dec  ', '|  Chr  |')
    print('+', '-'*6, '+', '-'*5, '+')
    print('|  {0:03}   |   {0:1c}   |'.format(inicio))
 
    for k in range(inicio + 1, fim + 1):
        print('|  {0:03}   |   {0:1c}   |'.format(k))

        if (k+1) % tamanho == 0:
            print('+', '-'*6, '+', '-'*5, '+')
            print('\n')
            print('+', '-'*6, '+', '-'*5, '+')
        
tabela()

