import itertools

def imetabling_forca_bruta(professores):
    # Inicializar a matriz de 10 linhas x 5 colunas
    matriz = [[None for _ in range(5)] for _ in range(10)]

    def pode_alocar(professor, linha, coluna):
        # Verificar se o professor já está na mesma linha (mesmo período)
        if professor in matriz[linha]:
            return False
        return True

    def alocar_aulas(permutacao_aulas):
        # Tentar alocar as aulas da permutação
        for index, (professor, _) in enumerate(permutacao_aulas):
            for linha in range(10):
                for coluna in range(5):
                    if matriz[linha][coluna] is None and pode_alocar(professor, linha, coluna):
                        matriz[linha][coluna] = professor
                        break
                else:
                    continue
                break
            else:
                return False  # Se não conseguiu alocar essa aula, falha na permutação
        return True

    # Gerar todas as aulas a partir da carga horária dos professores
    aulas = []
    for professor, carga in professores.items():
        aulas.extend([(professor, i) for i in range(carga)])

    # Gerar todas as permutações das aulas
    permutacoes = itertools.permutations(aulas)

    # Tentar todas as permutações
    for permutacao in permutacoes:
        # Resetar a matriz a cada tentativa
        matriz = [[None for _ in range(5)] for _ in range(10)]

        if alocar_aulas(permutacao):
            return matriz  # Se encontrar uma alocação válida, retorna a matriz

    return None  # Se nenhuma permutação for válida

def imprimir_matriz(matriz):
    dias_semana = ["2ª feira", "3ª feira", "4ª feira", "5ª feira", "6ª feira"]
    periodos = ["Período 1", "Período 2"]
    
    print("Seguindo as especificações apresentadas e conforme carga horária para cada professor indicada.")
    print()
    
    for dia_index in range(5): # 5 dias
        print(f"{dias_semana[dia_index]}:")
        
        for periodo_index in range(2):  # 2 períodos por dia
            linha = dia_index * 2 + periodo_index
            print(f"  {periodos[periodo_index]}: ", end="")  # Exibe o período
            print(" | ".join(str(prof) if prof is not None else "-" for prof in matriz[linha]))
        print()

# Dados iniciais
professores = {
    1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 1, 7: 4, 8: 2, 9: 1, 10: 1,
    11: 2, 12: 2, 13: 2, 14: 2, 15: 4, 16: 2, 17: 4, 18: 5, 19: 4, 20: 4
}

solucao = imetabling_forca_bruta(professores)

if solucao:
    imprimir_matriz(solucao)
else:
    print("Nenhuma solução válida foi encontrada.")
