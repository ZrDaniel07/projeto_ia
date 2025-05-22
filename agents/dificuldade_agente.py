
from pydantic import BaseModel, Field
from projeto_ia.fuzzy_logic.dificuldade import calcular_dificuldade

class HistoricoQuestao(BaseModel):
    id_questao: str
    acertos: int = Field(ge=0)
    erros: int = Field(ge=0)

class ResultadoDificuldade(BaseModel):
    dificuldade_fuzzy: float
    classificacao: str

class DificuldadeAgente:
    def avaliar(self, historico: HistoricoQuestao) -> ResultadoDificuldade:
        total = historico.acertos + historico.erros
        taxa_erro = historico.erros / total if total > 0 else 0.0
        resultado = calcular_dificuldade(taxa_erro)
        return ResultadoDificuldade(
            dificuldade_fuzzy=resultado["valor_fuzzy"],
            classificacao=resultado["classificacao"]
        )
