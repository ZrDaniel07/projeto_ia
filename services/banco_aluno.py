
import json
from typing import Dict

class BancoAluno:
    def __init__(self):
        # Estrutura: { aluno_id: { questao_id: {"acertos": int, "erros": int} } }
        self.historico: Dict[str, Dict[str, Dict[str, int]]] = {}

    def registrar_resposta(self, aluno_id: str, questao_id: str, correta: bool):
        if aluno_id not in self.historico:
            self.historico[aluno_id] = {}
        if questao_id not in self.historico[aluno_id]:
            self.historico[aluno_id][questao_id] = {"acertos": 0, "erros": 0}

        if correta:
            self.historico[aluno_id][questao_id]["acertos"] += 1
        else:
            self.historico[aluno_id][questao_id]["erros"] += 1

    def obter_historico(self, aluno_id: str) -> Dict[str, Dict[str, int]]:
        return self.historico.get(aluno_id, {})

    def salvar_em_arquivo(self, caminho: str):
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(self.historico, f, ensure_ascii=False, indent=2)

    def carregar_de_arquivo(self, caminho: str):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                self.historico = json.load(f)
        except FileNotFoundError:
            self.historico = {}
