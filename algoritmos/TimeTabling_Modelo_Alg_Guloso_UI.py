import random  # Importando a biblioteca random
import os
import sys
sys.path.insert(1, os.getcwd())
import json
# Dados iniciais
professores = {
    1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 1, 7: 4, 8: 2, 9: 1, 10: 1,
    11: 2, 12: 2, 13: 2, 14: 2, 15: 4, 16: 2, 17: 4, 18: 5, 19: 4, 20: 4
}

salas = [1, 2, 3, 4, 5]  # 5 salas disponíveis
periodos = ["Período 1", "Período 2"]  # Dois períodos por dia
dias_semana = ["2ª feira", "3ª feira", "4ª feira", "5ª feira", "6ª feira"]  # 5 dias da semana

# Função para carregar os dados de alocação (a partir de um arquivo)
def carregar_dados():
    try:
        with open("alocacao_gulosa.json", "r") as file:
            dados = json.load(file)
            return dados
    except FileNotFoundError:
        print("Arquivo de dados não encontrado, utilizando dados iniciais.")
        return {}

# Função para salvar os dados atualizados
def salvar_guloso(alocacao_por_dia):
    with open("alocacao_gulosa.json", "w") as file:
        json.dump(alocacao_por_dia, file, indent=4)
    print("Dados salvos no arquivo alocacao_gulosa.json.")

# Função para alocar aulas de maneira gulosa
def alocar_aulas_guloso():
    alocacao_por_dia = carregar_dados()  # Carrega os dados, se existirem

    # Verifica a integridade dos dados após a remoção
    if not professores or not salas or not periodos or not dias_semana:
        print("Erro: dados ausentes após a remoção de um item.")
        return {}  # Retorna um dicionário vazio para evitar falhas

    # Caso não haja dados, aloca normalmente
    if not alocacao_por_dia:
        alocacao_por_dia = {
            dia: {periodo: {sala: None for sala in salas} for periodo in periodos}
            for dia in dias_semana
        }

        # Para cada professor, tentar alocar suas aulas
        for professor, carga_horaria in professores.items():
            aulas_restantes = carga_horaria

            for dia in dias_semana:
                for periodo in periodos:
                    if aulas_restantes > 0:
                        for sala in salas:
                            if alocacao_por_dia[dia][periodo][sala] is None:
                                # Aloca o professor
                                alocacao_por_dia[dia][periodo][sala] = professor
                                aulas_restantes -= 1
                                break

    return alocacao_por_dia

# Rodando o algoritmo guloso
alocacao = alocar_aulas_guloso()
# imprimir_grade(alocacao)
salvar_guloso(alocacao)  # Salva os dados após a alocação
