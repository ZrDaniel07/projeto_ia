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
                item['enunciado'] = remover_bloco_final(item.get('enunciado', ''))
                item['area'] = item.get('area', '')

            # Salva o resultado tratado
            with open(caminho_absoluto_saida, 'w', encoding='utf-8') as saida:
                json.dump(dados, saida, ensure_ascii=False, indent=2)

            print(f"JSON tratado salvo em: {caminho_saida}")

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_entrada}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")


def remover_bloco_final(texto):
    padrao_com_ano = re.compile(
        r'\s*\d{4}\s*\n?.*?Caderno.*?Página\s*\d+\s*[\n]*$', 
        re.IGNORECASE | re.DOTALL
    )

    padrao_sem_ano_com_codigo = re.compile(
        r'\s*.*?Caderno.*?Página\s*\d+\s*\n\*.*?\*\s*$',
        re.IGNORECASE | re.DOTALL
    )


    while True:
        texto_novo = re.sub(padrao_com_ano, '', texto)
        texto_novo = re.sub(padrao_sem_ano_com_codigo, '', texto_novo)

        if texto_novo == texto:
            break

        texto = texto_novo

    return texto.strip()



# Exemplo de uso
if __name__ == "__main__":
    entrada = '../nao_tratado/enem_questoes.json'
    saida = '../tratado/enem_questoes_s_pag.json'
    carregar_tratar_e_salvar_json(entrada, saida)
