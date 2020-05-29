from agentes.humano import AgentePrepostoESHumano
class AgenteGulosa(AgentePrepostoESHumano):
    
    def __init__(self):
        # Uma sequencia de acoes, inicialmente vazia
        self.seq = []
    
    def formularProblema(self):
        ''' Formula um novo problema a ser resolvido, com base no objetivo
            atual.
            
            Ao final, self.problema deve estar preenchido.
        '''
        from agentes.modelagem.classificador import ProblemaClassificador
        self.problema = ProblemaClassificador(self.percepcao_mundo)

    def adquirirPercepcao(self, percepcao_mundo):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        super().adquirirPercepcao(percepcao_mundo)
        
        self.percepcao_mundo = percepcao_mundo.disposicao_elementos

    
    def escolherProximaAcao(self):
        # Se seq estiver vazia
        from agentes.buscas.buscas import busca_gulosa
        if not self.seq:
            self.formularProblema()

            no_solucao = busca_gulosa(self.problema)
            if no_solucao is None:
                return None
            else:
                self.seq = no_solucao.extrairSolucao()
                acao = self.seq.pop(0)
                return acao