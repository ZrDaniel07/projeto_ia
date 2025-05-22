
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variável de entrada: taxa de erro (0 a 1)
erro = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'erro')

# Variável de saída: dificuldade (0 a 1)
dificuldade = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'dificuldade')

# Conjuntos fuzzy para taxa de erro
erro['baixo'] = fuzz.trimf(erro.universe, [0.0, 0.0, 0.3])
erro['medio'] = fuzz.trimf(erro.universe, [0.2, 0.5, 0.8])
erro['alto']  = fuzz.trimf(erro.universe, [0.6, 1.0, 1.0])

# Conjuntos fuzzy para dificuldade
dificuldade['facil']   = fuzz.trimf(dificuldade.universe, [0.0, 0.0, 0.3])
dificuldade['media']   = fuzz.trimf(dificuldade.universe, [0.2, 0.5, 0.8])
dificuldade['dificil'] = fuzz.trimf(dificuldade.universe, [0.6, 1.0, 1.0])

# Regras fuzzy
rules = [
    ctrl.Rule(erro['baixo'], dificuldade['facil']),
    ctrl.Rule(erro['medio'], dificuldade['media']),
    ctrl.Rule(erro['alto'],  dificuldade['dificil'])
]

# Sistema de controle
dificuldade_ctrl = ctrl.ControlSystem(rules)
dificuldade_simulador = ctrl.ControlSystemSimulation(dificuldade_ctrl)

def calcular_dificuldade(taxa_erro: float) -> dict:
    """
    Retorna a dificuldade fuzzy para uma determinada taxa de erro (entre 0 e 1).
    """
    taxa_erro = min(max(taxa_erro, 0.0), 1.0)
    dificuldade_simulador.input['erro'] = taxa_erro
    dificuldade_simulador.compute()
    valor = dificuldade_simulador.output['dificuldade']

    if valor < 0.3:
        label = 'fácil'
    elif valor < 0.7:
        label = 'média'
    else:
        label = 'difícil'

    return {
        "valor_fuzzy": round(valor, 3),
        "classificacao": label
    }
