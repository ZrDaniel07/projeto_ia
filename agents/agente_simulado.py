
import random
from typing import List
from pydantic import BaseModel, Field

# Mock de uma questão
class Questao(BaseModel):
    id: str
    enunciado: str
    tema: str
    subtema: str
    dificuldade_fuzzy: float  # 0.0 a 1.0

class ConfigSimulado(BaseModel):
    quantidade: int
    temas: List[str] = Field(default_factory=list)
    dificuldade_min: float = 0.0
    dificuldade_max: float = 1.0

class AgenteSimulado:
    def __init__(self, banco_questoes: List[Questao]):
        self.banco_questoes = banco_questoes

    def gerar_simulado(self, config: ConfigSimulado) -> List[Questao]:
        # Filtro por dificuldade e tema
        filtradas = [
            q for q in self.banco_questoes
            if config.dificuldade_min <= q.dificuldade_fuzzy <= config.dificuldade_max
            and (not config.temas or q.tema in config.temas)
        ]

        random.shuffle(filtradas)
        return filtradas[:config.quantidade]
