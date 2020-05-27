from abc import ABC, abstractmethod
class AgenteAbstrato(ABC):
    '''
    Classe abstrata de agentes artificiais racionais.
    '''

    @abstractmethod
    def adquirirPercepcao(self, percepcao_mundo):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        return
    
    @abstractmethod
    def escolherProximaAcao(self):
        ''' Escolhe proxima acao, com base em seu entendimento do mundo, a partir
        das percepções anteriores.
        '''
        return

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    #FAZER UM MÉTODO QUE ESCOLHE O JOGADOR!
    
    #HUMANO
    #from agentes.tipos import TiposAgentes
    #from agentes.humano import AgentePrepostoESHumano
    #from agentes.agente_bfs import AgenteBFS

    #if args[0] == TiposAgentes.PREPOSTO_HUMANO:
    #    return AgentePrepostoESHumano()    
    #else:
    #    raise NotImplementedError()

    #BFS
    from agentes.humano import AgentePrepostoESHumano
    from agentes.agente_bfs import AgenteBFS
    from agentes.agente_dfs import AgenteDFS
    #return AgentePrepostoESHumano()
    #return AgenteBFS()
    
    return AgenteDFS()