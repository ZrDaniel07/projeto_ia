
from typing import List, Dict
from pydantic import BaseModel
from projeto_ia.fuzzy_logic.dificuldade import calcular_dificuldade
from projeto_ia.agents.dificuldade_agente import ResultadoDificuldade

class RespostaQuestao(BaseModel):
    id_questao: str
    correta: bool

class FeedbackQuestao(BaseModel):
    id_questao: str
    dificuldade_fuzzy: float
    classificacao: str
    total_erros: int
    total_acertos: int

class AgenteFeedback:
    def __init__(self, historico: Dict[str, Dict[str, int]]):
        self.historico = historico  # {"id_questao": {"acertos": int, "erros": int}}

    def processar_respostas(self, respostas: List[RespostaQuestao]) -> List[FeedbackQuestao]:
        feedbacks = []

        for resposta in respostas:
            stats = self.historico.get(resposta.id_questao, {"acertos": 0, "erros": 0})

            if resposta.correta:
                stats["acertos"] += 1
            else:
                stats["erros"] += 1

            self.historico[resposta.id_questao] = stats

            total = stats["acertos"] + stats["erros"]
            taxa_erro = stats["erros"] / total if total > 0 else 0.0
            fuzzy = calcular_dificuldade(taxa_erro)

            feedbacks.append(FeedbackQuestao(
                id_questao=resposta.id_questao,
                dificuldade_fuzzy=fuzzy["valor_fuzzy"],
                classificacao=fuzzy["classificacao"],
                total_erros=stats["erros"],
                total_acertos=stats["acertos"]
            ))

        return feedbacks
