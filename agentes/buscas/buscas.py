from agentes.buscas.no_busca import No

def busca_arvore_bfs(problema):
    borda = [ No(problema.estado_inicial()) ]
    
    while borda:
        folha = borda.pop(0)
        if problema.teste_objetivo(folha.estado):
            return folha
        
        for acao in problema.acoes(folha.estado):
            expandido = No.novoNoFilho(problema, folha, acao)
            borda.append(expandido)

def busca_arvore_dfs(problema, limitado=0):
    borda = [ No(problema.estado_inicial()) ]
    
    while borda:
        folha = borda.pop()
        

        if problema.teste_objetivo(folha.estado):
            return folha
        
        for acao in problema.acoes(folha.estado):
            expandido = No.novoNoFilho(problema, folha, acao)
            if limitado != 0:
                if expandido.calcularProfundidade() == limitado:
                    return None
            borda.append(expandido)

def busca_arvore_dfs_iterativo(problema):
    borda = [ No(problema.estado_inicial()) ]
    while True:
        limitado = input('Até qual altura você deseja percorrer sua busca?  ')
        if int(limitado):
            break

    while borda:
        folha = borda.pop()
        if problema.teste_objetivo(folha.estado):
            return folha
        
        for acao in problema.acoes(folha.estado):
            expandido = No.novoNoFilho(problema, folha, acao)
            if expandido.calcularProfundidade() == int(limitado):
                while True:
                    resp = input('1- Deseja continuar buscando? '+"\n"+
                                 '2- Não, estou satisfeito.'+"\n"
                                )
                    if resp == '1':
                        while True:
                            limitado = input('Até qual altura você deseja percorrer sua busca?  ')
                            if int(limitado):
                                break
                        break
                    elif resp == '2':
                        return None

            borda.append(expandido)

def busca_gulosa(problema):
    from agentes.buscas.heuristica import heuristica
    borda = [ No(problema.estado_inicial()) ]
    
    fn = []
    bordaAux = []
    while borda:        
        fn = []
        bordaAux = []
        i=0
        for i in range(0,len(borda)):
            bordaAux.append(borda[i])
            fn.append(heuristica(bordaAux[i]))
            
        auxMenorHeuristica = 0
        
        auxPosMenorHeuristica = 0
        for j in range(0,len(fn)):
            if j == 0:
                auxMenorHeuristica = fn[j]
            else:
                if fn[j] < auxMenorHeuristica:
                    auxPosMenorHeuristica = j
                    auxMenorHeuristica = fn[j]

        if problema.teste_objetivo(bordaAux[auxPosMenorHeuristica].estado):
            return bordaAux[auxPosMenorHeuristica]
        
        for acao in problema.acoes(bordaAux[auxPosMenorHeuristica].estado):
            expandido = No.novoNoFilho(problema, bordaAux[auxPosMenorHeuristica], acao)
            if expandido is not None:
                borda.append(expandido)
        
        fn.pop(auxPosMenorHeuristica)
        bordaAux.pop(auxPosMenorHeuristica)
        borda.pop(auxPosMenorHeuristica)

def busca_a_estrela(problema):
    from agentes.buscas.heuristica import heuristica
    borda = [ No(problema.estado_inicial()) ]
    
    fn = []
    bordaAux = []
    while borda:        
        fn = []
        bordaAux = []
        i=0
        for i in range(0,len(borda)):
            bordaAux.append(borda[i])
            fn.append(heuristica(bordaAux[i]))
        auxMenorHeuristica = 0
        auxPosMenorHeuristica = 0
        for j in range(0,len(fn)):
            if j == 0:
                auxMenorHeuristica = fn[j]
            else:
                if fn[j] < auxMenorHeuristica:
                    auxPosMenorHeuristica = j
                    auxMenorHeuristica = fn[j]
        
        auxMenorHeuristica = auxMenorHeuristica+(bordaAux[auxPosMenorHeuristica].gn)
        


        if problema.teste_objetivo(bordaAux[auxPosMenorHeuristica].estado):
            
            return bordaAux[auxPosMenorHeuristica]
        
        for acao in problema.acoes(bordaAux[auxPosMenorHeuristica].estado):
            expandido = No.novoNoFilho(problema, bordaAux[auxPosMenorHeuristica], acao)
            if expandido is not None:
                borda.append(expandido)
        fn.pop(auxPosMenorHeuristica)
        bordaAux.pop(auxPosMenorHeuristica)
        borda.pop(auxPosMenorHeuristica)
