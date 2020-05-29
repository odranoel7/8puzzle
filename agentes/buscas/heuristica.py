
def heuristica_busca_gulosa(estado):
    #return 1
    valor = 0
    estado_resultante = estado.estado
    
    aux = 0
    bAux = False
    esperado = [1,2,3,4,5,6,7,8,0]
    #print('Entrou na heuristica')
    #print(str(range(len(estado_resultante))))
    #print(str(range(0,len(esperado))))
    for i in range(0,len(estado_resultante)):
        j=0
        aux=0
        for j in range (0,len(esperado)):
            
            if esperado[i] == estado_resultante[j]:
                #print('valor de i -> '+str(i))                
                #print('valor de j -> '+str(j))

                if (esperado[i] == 0) and (j == 1):
                    aux = 3
                elif (i == 7 and j == 0) or (i == 7 and j == 2):
                    aux = 3
                #elif 
                
                elif i == 2 and j == len(estado_resultante)-3:
                    aux = 4
                elif i == 1 and j == len(estado_resultante)-1:
                    
                    aux = 3
                elif i == 0 and j == len(estado_resultante)-2:
                    #print('esperado segundo')
                    aux = 3
                    
                elif i == 0 and j == len(estado_resultante)-1:
                    #print('entrou no que jdfbc')
                    aux = 4
                    
                else:
                    if i > j: 
                        if i-j == 3:
                            aux=3
                            bAux=True
                        elif (i-j) > 2:
                            aux=(i-j)-2
                            bAux = False
                        else:
                            #print('entrou')
                            aux=i-j
                            bAux = True
                    else:
                        if i == j:
                            #print('é igual')                        
                            aux=0
                        else:
                            #print('foi pro else')
                            if j-i == 3:
                                aux=3
                                bAux=True
                            elif (j-i) > 2:
                                aux=(j-i)-2
                                bAux = False
                            else:
                                aux=j-i
                                bAux=True
                    if aux ==4:
                        aux=2
                    elif aux==1 and bAux and ((i==2 and j==3) or (i==5 and j==6)):
                        aux=3
                    elif aux==3 and bAux:
                        aux=1
                    #elif aux==4 and bAux:
                    #    aux=2
                    #print('valor do aux -> '+str(aux))
                valor = valor+aux
                #print('valor do valor  '+str(valor))
                break
        #print('continua sim')
        #print()
        #print()
    #print()
    #print('vai retornar')
    #print(valor)
    return valor
