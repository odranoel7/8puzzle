from enum import Enum, auto
class AgentesOrdenador(Enum):
    JOGADOR_PADRAO = auto()


from regras_jogo.regras_abstratas import AbstractRegrasJogo
from regras_jogo.personagens import Personagens
from random import randint
class Puzzle(AbstractRegrasJogo):
    
    def __init__(self):        
        #self.elementos = [randint(0, 8) for _ in range(8)]
        
        
        
        self.elementos = []
        while len(self.elementos) < 9:
            aux = randint(0,8)
            if aux not in self.elementos:
                self.elementos.append(aux)
        
        self.pontuacao = 0
        #print('tamanho'+str(len(self.elementos)))

    def registrarAgentePersonagem(self, personagem=Personagens.O_JOGADOR):
        """ Só há um agente, o jogador, então não preciso de lógica.
        """
        return 1
    
    def isFim(self):
        """ Se a lista estiver ordenada, fim de jogo.
        """
        from agentes.tipos import TiposAgentes
        
        auxLista = []
        fim = False
        for j in range(len(self.elementos)):
            if self.elementos[j] != 0:
                auxLista.append(self.elementos[j])
        
        fim = all(auxLista[i] <= auxLista[i+1]
            for i, _ in enumerate(auxLista[:-1]))                

        if fim:
            if not ((self.elementos[len(self.elementos)-1] == 0) or (self.elementos[0] == 0)):
                fim = False
        

        #print('Esse é o valor que quer saber -> '+str(auxLista[3:6]))

        


        if (((self.elementos[0:3]==[1,2,3]) or (self.elementos[0:3]==[0,1,2]))
         or ((self.elementos[3:6]==[4,5,6]) or (self.elementos[3:6]==[3,4,5])) 
         or ((self.elementos[6:9]==[6,7,8]) or (self.elementos[6:9]==[7,8,0]))):     
            aux = ''
            i=0
            for i in range(len(self.elementos)):
                if self.elementos[i] != 0: 
                    aux = aux+' '+str(self.elementos[i])
                else:
                    aux = aux+' '+' '
                if ((i == 2) or (i == 5) or (i == (len(self.elementos)-1))):                
                    print(aux+'\n')
                    aux = ''        
        
        return fim

    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        from percepcoes import PercepcoesJogador
        return PercepcoesJogador(tuple(self.elementos))

        #return elementos

    def registrarProximaAcao(self, id_agente, acao):
        """ Como só há um agente atuando no mundo, o próprio jogador, não é
        necessário nenhum mecanismo para guardar ações associadas por agentes
        distintos.
        """
        self.acao_jogador = acao
    
    def atualizarEstado(self, diferencial_tempo):
        """ Não preciso me preocupar com a passagem do tempo, pois só uma
        jogada é feita por vez, e o jogo não muda seu estado sem jogadas.

        Verifico a ação última registrada e atualizado o estado do jogo
        computando-a.
        """
        #OBS: I é onde o 0 está, e o J é para onde ele vai depois da permuta!
        from acoes import AcoesJogador
        auxI = 0
        auxJ = 0
        auxVlrI = 0
        auxVlrJ = 0
        if self.acao_jogador.tipo == AcoesJogador.permutar:
            for i in range(len(self.elementos)):
                if self.elementos[i] == 0:
                    pos0 = i
                    break
            if (self.acao_jogador.parametros) == 'C':
                if pos0 <= 2:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI-3
                

            elif self.acao_jogador.parametros == 'B':
                if pos0 >= 6:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI+3


            elif self.acao_jogador.parametros == 'E':
                if pos0 in [0,3,6]:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI-1
                

            elif self.acao_jogador.parametros == 'D':
                if pos0 in [2,5,8]:
                    print('Ação invalida')
                else:
                    auxI = pos0
                    auxJ = auxI+1

            auxVlrI = self.elementos[auxI]
            auxVlrJ = self.elementos[auxJ]
            self.elementos[auxI] = auxVlrJ
            self.elementos[auxJ] = auxVlrI
            
            #self.elementos[i], self.elementos[j] = self.elementos[j], self.elementos[i]
        else:
            raise TypeError

        self.pontuacao += 1

    def registrarAgenteJogador(self, elem_agente=AgentesOrdenador.JOGADOR_PADRAO):
        """ Só há um agente, o jogador, então não preciso de lógica.
        """
        return 1
    
    def terminarJogo(self):
        print(f'Fim de jogo! Sua pontuação foi de {self.pontuacao}.')
