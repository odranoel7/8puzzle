from agentes.modelagem.problema import ProblemaAbstrato


class ProblemaClassificador(ProblemaAbstrato):

    def __init__(self, estado_inicial):
        super().__init__()
        self._estado_inicial = estado_inicial

    def estado_inicial(self):
        return self._estado_inicial

    def acoes(self, estado):
        """
        Por simplificação, estado já é uma tupla de valores, mas não é bonito.
        """
        from acoes import AcaoJogador

        #lista = []
        #aux = ""
        
        #return [ AcaoJogador.permutar(str(i))
        #    for i,_ in enumerate(estado)
        #        for j,_ in enumerate(estado) ]

        return [AcaoJogador.permutar('C'), AcaoJogador.permutar('B'), AcaoJogador.permutar('E'), AcaoJogador.permutar('D')]

    def resultado(self, estado, acao):
        from acoes import AcoesJogador

        estado_resultante = list(estado)
        if acao.tipo == AcoesJogador.permutar:
            auxI = 0
            auxJ = 0
            auxVlrI = 0
            auxVlrJ = 0
            
            for i in range(len(estado_resultante)):
                if estado_resultante[i] == 0:
                    pos0 = i
                    break
            if (acao.parametros) == 'C':
                if pos0 <= 2:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI-3

            elif acao.parametros == 'B':
                if pos0 >= 6:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI+3

            elif acao.parametros == 'E':
                if pos0 in [0, 3, 6]:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI-1

            elif acao.parametros == 'D':
                if pos0 in [2, 5, 8]:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI+1

            auxVlrI = estado_resultante[auxI]
            auxVlrJ = estado_resultante[auxJ]
            estado_resultante[auxI] = auxVlrJ
            estado_resultante[auxJ] = auxVlrI

            #i, j = acao.parametros
            #estado_resultante[i], estado_resultante[j] = estado_resultante[j], estado_resultante[i]
        else:
            raise TypeError

        return tuple(estado_resultante)

    def teste_objetivo(self, estado):
        auxLista = []
        for j in range(len(estado)):
            if estado[j] != 0:
                auxLista.append(estado[j])
        
        return all(auxLista[i] <= auxLista[i+1]
            for i, _ in enumerate(auxLista[:-1]))

        #return all(estado[i] <= estado[i+1]
        #           for i, _ in enumerate(estado[:-1]))

    def custo_transicao(self, estado, acao, estado_resultante):
        return 1
