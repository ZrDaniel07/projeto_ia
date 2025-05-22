import json
import os
import re

def carregar_tratar_e_salvar_json(caminho_entrada, caminho_saida):
    caminho_absoluto_entrada = os.path.join(os.path.dirname(__file__), caminho_entrada)
    caminho_absoluto_saida = os.path.join(os.path.dirname(__file__), caminho_saida)

    try:
        with open(caminho_absoluto_entrada, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            for item in dados:
                enunciado_original = item.get('enunciado', '')
                corpo, alternativas = extrair_alternativas(enunciado_original)

                if len(alternativas) < 5:
                    continue 

                item['enunciado_completo'] = enunciado_original.strip()
                item['enunciado'] = corpo.strip()
                item['alternativas'] = alternativas
                item['area'] = item.get('area', '')

            with open(caminho_absoluto_saida, 'w', encoding='utf-8') as saida:
                json.dump(dados, saida, ensure_ascii=False, indent=2)

            print(f"JSON com alternativas salvo em: {caminho_saida}")

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_entrada}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")

def extrair_alternativas(texto):
    linhas = [linha.strip() for linha in texto.strip().splitlines() if linha.strip()]

    if len(linhas) >= 5:
        alternativas = linhas[-5:]
        corpo = "\n".join(linhas[:-5])
    else:
        alternativas = linhas
        corpo = ""

    return corpo, alternativas

# Exemplo de uso
if __name__ == "__main__":
    entrada = '../tratado/enem_questoes_s_pag.json'
    saida = '../tratado/enem_questoes_c_op.json'
    carregar_tratar_e_salvar_json(entrada, saida)
