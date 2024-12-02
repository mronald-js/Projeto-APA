import random  # Importando a biblioteca random

# Dados iniciais
professores = {
    1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 1, 7: 4, 8: 2, 9: 1, 10: 1,
    11: 2, 12: 2, 13: 2, 14: 2, 15: 4, 16: 2, 17: 4, 18: 5, 19: 4, 20: 4
}

salas = [1, 2, 3, 4, 5]  # 5 salas disponíveis
periodos = ["Período 1", "Período 2"]  # Dois períodos por dia
dias_semana = ["2ª feira", "3ª feira", "4ª feira", "5ª feira", "6ª feira"]  # 5 dias da semana

# Estrutura de alocação
alocacao_por_dia = {dia: {periodo: {sala: None for sala in salas} for periodo in periodos} for dia in dias_semana}
professores_alocados = {professor: 0 for professor in professores}  # Contagem de aulas alocadas para cada professor

# Função para alocar aulas de maneira gulosa
def alocar_aulas_guloso():
    alocacao = {professor: [] for professor in professores.keys()}  # Alocação inicial vazia

    # Para cada professor, tentar alocar suas aulas
    for professor, carga_horaria in professores.items():
        aulas_restantes = carga_horaria  # O número de aulas que ainda precisa ministrar

        # Tentando alocar aulas até que o professor tenha completado sua carga horária
        for dia in dias_semana:
            for periodo in periodos:
                if aulas_restantes > 0:
                    # Tentando alocar o professor na primeira sala disponível para aquele dia e período
                    for sala in salas:
                        if alocacao_por_dia[dia][periodo][sala] is None:
                            alocacao[professor].append((f"Aula {random.randint(1, 100)}", periodo, sala))
                            alocacao_por_dia[dia][periodo][sala] = professor  # Marcar a sala como ocupada
                            professores_alocados[professor] += 1  # Incrementar a quantidade de aulas alocadas para o professor
                            aulas_restantes -= 1  # Decrementa a carga horária restante
                            break  # Passa para o próximo período ou dia

    return alocacao

# Função de impressão da grade horária no formato desejado
def imprimir_grade():
    print("Tabela 6.1: Exemplo de grade horária gerada (cinco salas concomitantes)")
    print("Seguindo as especificações apresentadas e conforme carga horária para cada professor indicada.")
    print()

    # Exibindo a alocação por dia e período
    for dia in dias_semana:
        print(f"{dia}:")
        
        for periodo in periodos:
            print(f"  {periodo}: ", end="")
            
            # Preparando os dados da tabela
            tabela = []
            for sala in salas:
                professor = alocacao_por_dia[dia][periodo][sala]
                tabela.append(str(professor) if professor is not None else "-")
            
            # Imprimindo a linha da tabela
            print(" | ".join(tabela))

# Rodando o algoritmo guloso
alocacao = alocar_aulas_guloso()
imprimir_grade()
