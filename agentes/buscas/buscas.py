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
    folha = None
    fn = []
    while borda:
        folha = borda.pop(0)
        aux = heuristica_busca_gulosa(folha.estado)
        fn.append(aux)
        #print(str(folha.estado))
        
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
