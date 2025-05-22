
from typing import Dict, List
from pydantic import BaseModel

class HistoricoQuestao(BaseModel):
    id_questao: str
    tema: str
    subtema: str
    acertos: int
    erros: int

class FlashcardQuestao(BaseModel):
    id_questao: str
    subtema: str
    total_erros: int

class AgenteFlashcard:
    def gerar_flashcards(self, historico: List[HistoricoQuestao], limite: int = 5) -> List[FlashcardQuestao]:
        # Ordenar por maior número de erros e retornar os mais críticos
        ordenadas = sorted(
            historico, key=lambda x: x.erros, reverse=True
        )
        selecionadas = ordenadas[:limite]

        return [
            FlashcardQuestao(
                id_questao=q.id_questao,
                subtema=q.subtema,
                total_erros=q.erros
            )
            for q in selecionadas if q.erros > 0
        ]
