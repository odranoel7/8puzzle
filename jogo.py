#!/usr/bin/env python3

import time
from regras_jogo.regras_abstratas import construir_jogo
from regras_jogo.personagens import Personagens
from agentes.abstrato import construir_agente
from agentes.tipos import TiposAgentes

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():
    
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    id_jogador, jogador = jogo.registrarAgenteJogador(), construir_agente()
    tempo_de_jogo = 0
    
    
    #jogo = construir_jogo()
    #personagem_jogador = jogo.registrarAgentePersonagem(Personagens.O_JOGADOR)
    #agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.O_JOGADOR)
    #agente_jogador = construir_agente(TiposAgentes.AUTO_BFS, Personagens.O_JOGADOR)
    
    tempo_de_jogo = 0
    while not jogo.isFim():
        ambiente_perceptivel = jogo.gerarCampoVisao(id_jogador)
        jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        acao = jogador.escolherProximaAcao()
        #if acao is None:
        #    print('Sem solução')
        #    break
        jogo.registrarProximaAcao(id_jogador, acao)

        # Atualizar jogo
        tempo_corrente = ler_tempo()
        jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
        tempo_de_jogo += tempo_corrente

        
        # Mostrar mundo ao jogador
        #ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        #agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        #acao = agente_jogador.escolherProximaAcao()
        #jogo.registrarProximaAcao(personagem_jogador, acao)

        # Atualizar jogo
        #tempo_corrente = ler_tempo()
        #jogo.atualizarEstado(tempo_corrente - tempo_de_jogo)
        #tempo_de_jogo += tempo_corrente
        
    jogo.terminarJogo()


if __name__ == '__main__':
    iniciar_jogo()