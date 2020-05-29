from agentes.buscas.no_busca import No

def busca_arvore_bfs(problema):
    ''' Monta uma nova sequencia de acoes para resolver o problema atual.
    
        Ao final, self.seq deve conter uma lista de acoes.
    '''
    #from agentes.buscas.heuristica import heuristica_busca_gulosa
    borda = [ No(problema.estado_inicial()) ]
    
    while borda:
        
        

        folha = borda.pop(0)

        #print(str(folha.estado))
        #aux = heuristica_busca_gulosa(folha.estado)
        #print()
        #print('retorno da heuristica '+str(aux))
        #print()
        #print()
        #print('removeu -> '+str(folha.estado))
        #print()



        if problema.teste_objetivo(folha.estado):
            return folha
        
        for acao in problema.acoes(folha.estado):
            expandido = No.novoNoFilho(problema, folha, acao)
            borda.append(expandido)

def busca_arvore_dfs(problema, limitado=0):
    ''' Monta uma nova sequencia de acoes para resolver o problema atual.
    
        Ao final, self.seq deve conter uma lista de acoes.
    '''
    borda = [ No(problema.estado_inicial()) ]
    retorno = False
    while borda:        
        folha = borda.pop()
        if problema.teste_objetivo(folha.estado):
            return folha
        
        for acao in problema.acoes(folha.estado):
            expandido = No.novoNoFilho(problema, folha, acao)
            if limitado == expandido.calcularProfundidade():
                #print('profundidade -> '+str(expandido.calcularProfundidade()))
                return None
            borda.append(expandido)
    if retorno:
        return None

def busca_gulosa(problema):
    from agentes.buscas.heuristica import heuristica_busca_gulosa
    borda = [ No(problema.estado_inicial()) ]
    
    fn = []
    bordaAux = []
    
    while borda:
        i=0
        for i in range(0,len(borda)):
            bordaAux.append(borda[i])
            fn.append(heuristica_busca_gulosa(bordaAux[i]))
            #print()
            #print()
            #print()
            #print('removeu -> '+str(folha.estado))
            #print()
        borda.pop(0)
        auxMenor = 0
        auxJ = 0
        for j in range(0,len(fn)):
            if j == 0:
                auxMenor = fn[j]
            else:
                if fn[j] < auxMenor:
                    auxJ = j
                    auxMenor = fn[j]
        
        print('Achou a menor heurística - > '+str(auxMenor))
        print('Que é ->  '+str(bordaAux[auxJ].estado))
        print()


        if problema.teste_objetivo(bordaAux[auxJ].estado):
            print('Achou o objetivo')
            print()
            return bordaAux[auxJ]
        
        print('tamanho antes do for -> '+str(len(borda)))
        print()
        for acao in problema.acoes(bordaAux[auxJ].estado):
            expandido = No.novoNoFilho(problema, bordaAux[auxJ], acao)            
            borda.append(expandido)
        print('tamanho depois do for -> '+str(len(borda)))
        print()
        print('tamanho do fn antes de remover -> '+str(len(fn)))
        print('tamanho da bordaAux antes de remover -> '+str(len(fn)))
        print()
        fn.pop(auxJ)
        bordaAux.pop(auxJ)
        print('tamanho do fn depois de remover -> '+str(len(fn)))
        print('tamanho da bordaAux depois de remover -> '+str(len(fn)))

