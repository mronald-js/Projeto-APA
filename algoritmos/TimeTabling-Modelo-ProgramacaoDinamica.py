def timetabling_dp(professores, salas, periodos, dias_semana):
    # Inicializar tabela de alocação
    alocacao_por_dia = {dia: {periodo: {sala: None for sala in salas} for periodo in periodos} for dia in dias_semana}
    
    # Resolver o problema iterativamente
    for professor, carga in professores.items():
        for dia in dias_semana:
            for periodo in periodos:
                for sala in salas:
                    if carga > 0 and alocacao_por_dia[dia][periodo][sala] is None:
                        alocacao_por_dia[dia][periodo][sala] = professor
                        carga -= 1
                    if carga == 0:
                        break
                if carga == 0:
                    break
            if carga == 0:
                break
    
    return alocacao_por_dia


def imprimir_grade(dias_semana, periodos, salas, alocacao_por_dia):
    print("Tabela 6.1: Exemplo de grade horária gerada (cinco salas concomitantes)")
    print("Seguindo as especificações apresentadas e conforme carga horária para cada professor indicada.")
    print()

    for dia in dias_semana:
        print(f"{dia}:")
        
        for periodo in periodos:
            print(f"  {periodo}: ", end="")
            
            tabela = []
            for sala in salas:
                professor = alocacao_por_dia[dia][periodo][sala]
                tabela.append(str(professor) if professor is not None else "-")
            
            # Imprimindo a linha da tabela
            print(" | ".join(tabela))
        print()


# Dados iniciais
professores = {
    1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 1, 7: 4, 8: 2, 9: 1, 10: 1,
    11: 2, 12: 2, 13: 2, 14: 2, 15: 4, 16: 2, 17: 4, 18: 5, 19: 4, 20: 4
}

salas = [1, 2, 3, 4, 5]  # 5 salas disponíveis
dias_semana = ["2ª feira", "3ª feira", "4ª feira", "5ª feira", "6ª feira"]  # 5 dias da semana
periodos = ["Período 1", "Período 2"]  # 2 períodos por dia

# Resolver o problema de timetabling usando Programação Dinâmica
alocacao_por_dia = timetabling_dp(professores, salas, periodos, dias_semana)

# Exibir a grade
imprimir_grade(dias_semana, periodos, salas, alocacao_por_dia)