
from pydantic_ai import PydanticAI, OpenAIModel
from pydantic import BaseModel, Field

class QuestaoEntrada(BaseModel):
    enunciado: str = Field(..., description="Texto da questão do ENEM")

class ClassificacaoTema(BaseModel):
    tema: str = Field(..., description="Tema principal da questão, como: matemática, física, química, biologia, história, geografia, filosofia, sociologia, português")
    subtema: str = Field(..., description="Subtema específico, como: funções, genética, cinemática, gramática etc.")

class TemaAgente(PydanticAI):
    input_model = QuestaoEntrada
    output_model = ClassificacaoTema
    model = OpenAIModel(model="gpt-4")

    prompt_template = """Você é um agente que classifica o tema de uma questão do ENEM.
    Dado o enunciado a seguir, identifique o tema principal e o subtema mais específico.

    Enunciado:
    {enunciado}
    """
