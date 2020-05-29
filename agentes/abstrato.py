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
    from agentes.agente_dfs_limitado import AgenteDFS_limitado
    from agentes.agente_gulosa import AgenteGulosa
    from agentes.agente_a_estrela import AgenteAEstrela

    while True:
        resp = input('1 -> Agente humano.'+"\n"+'2 -> Agente BFS.'+"\n"+'3 -> Agente DFS.'+"\n"+'4 -> Agente DFS limitado.'+"\n"+'5 -> Busca gulosa.'+"\n"+'6 -> Busca A-Estrela'+"\n")
        if resp == '1':
            return AgentePrepostoESHumano()
        elif resp == '2':
            return AgenteBFS()
        elif resp == '3':
            return AgenteDFS()
        elif resp == '4':
            return AgenteDFS_limitado()
        elif resp == '5':
            return AgenteGulosa()
        elif resp == '6':
            return AgenteAEstrela()
        else:
            print("\n"+'Opção inválida, digite a opção correta!'+"\n")