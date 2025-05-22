
from pydantic_ai import PydanticAI, OpenAIModel
from pydantic import BaseModel, Field

class FormularioEntrada(BaseModel):
    nome: str = Field(..., description="Nome completo do aluno")
    idade: int = Field(..., description="Idade do aluno")
    email: str = Field(..., description="E-mail do aluno")
    respostas: dict = Field(..., description="Respostas do aluno com IDs das questões como chaves")

class ResultadoProcessado(BaseModel):
    total_respondidas: int
    valido: bool
    mensagem: str

class FormularioAgente(PydanticAI):
    input_model = FormularioEntrada
    output_model = ResultadoProcessado
    model = OpenAIModel(model="gpt-4")

    prompt_template = """Você é um agente que valida o preenchimento de um formulário de aluno.
    Dado os dados abaixo:
    - Nome: {nome}
    - Idade: {idade}
    - E-mail: {email}
    - Respostas: {respostas}

    Valide se os dados estão completos. Retorne se está válido, o total de respostas e uma mensagem para o usuário."""
