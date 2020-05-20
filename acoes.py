from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    permutar = 'PERMUTAR'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def permutar(cls, escolhido):
        return cls(AcoesJogador.permutar, escolhido)