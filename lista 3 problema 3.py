#-------------------------------------------------------------------------------------
#UFRJ - IM - DMA - TMAA-2019.1
#-------------------------------------------------------------------------------------
# Lista 3 - Problema 3
#-------------------------------------------------------------------------------------
#Lucas Galdino de Souza (119039091)
#-------------------------------------------------------------------------------------

import os

def contagempasta(a='.'):
    arquivos=os.listdir(a)
    listatxt=[ ]
    
    for txt in arquivos:
        if txt[-4:]=='.txt': #Verifica se os ultimos 4 digitos  são .txt.
            listatxt.append(txt)  #Cria uma lista com o nome de todos os arquivos .txt
        else:                  
            pass
    palavras=[ ]  
    palavrasfrequencia=[ ]
    palavrasfrequenciadas=[ ]
    print(listatxt)
    
    for i in listatxt: # arquivos TXT
        arquivo=open(i,'r')
        q=arquivo.read()  # formando uma grande string       
        z=q.split(" ")
        
        for p in z:
            p.replace(',','')#remove ',' , '.' e ':' das palavras,            
            p.replace('.','')
            p.replace(':','')
        palavras+=z 

    for i in palavras:
        z=i.split('\n') 
        palavras.remove(i)
        palavras+=z
    
    palavrasunicas=list(dict.fromkeys(palavras)) # criando a lista de palavras unicas.    
    for x in palavrasunicas: # calcular a frequência das palavras.
        
        y=str(palavras.count(x))  # Verifica a frequência 
        palavrasfrequenciadas.append(x+' - '+y) # adiciona a palavra e sua frequencia 
    palavrasfrequenciadas.sort(key= lambda a: int(a.split(' - ')[1]) ,reverse=True) 
    
    return palavrasfrequenciadas 
