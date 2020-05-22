from agentes.buscas.no_busca import No

def busca_arvore(problema):
    ''' Monta uma nova sequencia de acoes para resolver o problema atual.
    
        Ao final, self.seq deve conter uma lista de acoes.
    '''
    borda = [ No(problema.estado_inicial()) ]
    while borda:
    
        folha = borda.pop(0)
        if problema.teste_objetivo(folha.estado):
            return folha
        
        for acao in problema.acoes(folha.estado):
            expandido = No.novoNoFilho(problema, folha, acao)
            borda.append(expandido)

    raise ProblemaSemSolucaoException()