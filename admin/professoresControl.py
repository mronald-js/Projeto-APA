import customtkinter as ctk
import tkinter
import os
import sys
from tkinter import simpledialog
sys.path.insert(1, os.getcwd())
from banco.database import connect_db
import utility.center as center
import random  # Importando a biblioteca random
import json

# Dados do "guloso"
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
            dados = file.read().strip()
            if dados:  # Verifica se o arquivo não está vazio
                return json.loads(dados)
            else:
                print("Arquivo vazio, utilizando dados padrão.")
                return {}  # Retorna um dicionário vazio se o arquivo estiver vazio
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar os dados: {e}")
        print("Utilizando dados padrão.")
        return {}  # Retorna um dicionário vazio em caso de erro

# Função para salvar os dados atualizados
def salvar_guloso(alocacao_por_dia):
    with open("alocacao_gulosa.json", "w") as file:
        json.dump(alocacao_por_dia, file, indent=4)
    print("Dados salvos no arquivo alocacao_gulosa.json.")

# Função para alocar aulas de maneira gulosa
def alocar_aulas_guloso():
    alocacao_por_dia = carregar_dados()  # Carrega os dados, se existirem

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

class ProfessoresControle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(center.CenterWindowToDisplay(self, 800, 600))
        self.title("Controle de Professores")
        self.create_widgets()
        self.create_button_container()
        self.create_button_containerOut()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Modificar Professores", font=("Arial Bold", 24)).pack(pady=20)

        # Criar um frame com rolagem
        scrollable_frame = ctk.CTkScrollableFrame(self)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        headers = ["ID", "Nome", "Carga Horária"]
        # Dados dos professores
        professors = list(professores.items())  # Lista dos professores

        # Cabeçalhos da tabela
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                master=scrollable_frame, text=header, font=("Arial Bold", 16), anchor="center"
            ).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        # Dados dos professores
        for row, (professor_id, carga_horaria) in enumerate(professors, start=1):
            ctk.CTkLabel(
                master=scrollable_frame, text=professor_id, font=("Arial", 12), anchor="center"
            ).grid(row=row, column=0, padx=5, pady=5, sticky="nsew")
            ctk.CTkLabel(
                master=scrollable_frame, text=f"Professor {professor_id}", font=("Arial", 12), anchor="center"
            ).grid(row=row, column=1, padx=5, pady=5, sticky="nsew")
            ctk.CTkLabel(
                master=scrollable_frame, text=carga_horaria, font=("Arial", 12), anchor="center"
            ).grid(row=row, column=2, padx=5, pady=5, sticky="nsew")

    def create_button_container(self):
        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, fill="y", side="top", expand=True)

        ctk.CTkButton(master=button_container, text="Adicionar Professor", command=self.add_professor).pack(pady=5, padx=10, side="left")
        ctk.CTkButton(master=button_container, text="Remover Professor", command=self.remove_professor).pack(pady=5, padx=10, side="left")
        ctk.CTkButton(master=button_container, text="Atualizar Professor", command=self.update_professor).pack(pady=5, padx=10, side="left")

    def add_professor(self):
        """Adicionar um novo professor (com o nome e carga horária)."""
        professor_name = simpledialog.askstring("Adicionar Professor", "Digite o nome do professor:")
        if professor_name:
            carga_horaria = simpledialog.askinteger("Adicionar Professor", f"Digite a carga horária de {professor_name}:")
            if carga_horaria:
                # Gerar um ID único, baseado no maior ID já presente
                new_professor_id = max(professores.keys(), default=0) + 1  # Garante um ID único
                professores[new_professor_id] = carga_horaria
                
                # Agora, atualiza a alocação de aulas
                alocacao_por_dia = alocar_aulas_guloso()
                
                # Salva os dados atualizados
                salvar_guloso(alocacao_por_dia)  # Atualiza o JSON
                self.create_widgets()  # Atualiza a interface

    def remove_professor(self):
        """Remover um professor pelo ID."""
        alocacao_por_dia = carregar_dados()
        professor_id = simpledialog.askinteger("Remover Professor", "Digite o ID do professor a ser removido:")
        if professor_id in professores:
            # Remover o professor das alocações
            for dia, alocacao_dia in alocacao_por_dia.items():
                for periodo, alocacao_periodo in alocacao_dia.items():
                    for sala, professor in alocacao_periodo.items():
                        if professor == professor_id:
                            alocacao_por_dia[dia][periodo][sala] = None  # Remover o professor da alocação

            # Agora, removemos o professor da lista de professores
            del professores[professor_id]

            self.salvar_guloso(alocacao_por_dia)  # Atualiza o JSON com as alocações e os dados dos professores
            alocar_aulas_guloso()  # Realoca as aulas
            self.create_widgets()  # Atualiza a tabela

    def update_professor(self):
        """Atualizar os dados de um professor."""
        professor_id = simpledialog.askinteger("Atualizar Professor", "Digite o ID do professor a ser atualizado:")
        if professor_id in professores:
            new_name = simpledialog.askstring("Atualizar Professor", f"Digite o novo nome para o professor {professor_id}:")
            if new_name:
                new_carga_horaria = simpledialog.askinteger("Atualizar Professor", f"Digite a nova carga horária de {new_name}:")
                if new_carga_horaria:
                    # Atualiza a carga horária do professor
                    professores[professor_id] = new_carga_horaria
                    
                    # Atualiza as alocações de aulas com a nova carga horária
                    alocacao_por_dia = alocar_aulas_guloso()
                    
                    # Salva os dados atualizados
                    salvar_guloso(alocacao_por_dia)  # Atualiza o JSON
                    self.create_widgets()  # Atualiza a interface

    def salvar_guloso(self, alocacao_por_dia):
        with open("alocacao_gulosa.json", "w") as file:
            json.dump(alocacao_por_dia, file, indent=4)
        print("Dados salvos no arquivo alocacao_gulosa.json.")

    def quit_app(self):
        """Fecha a aplicação."""
        self.destroy()

    def retornar(self):
        """Retorna para a tela principal."""
        self.destroy()
        from admin.admin import AdminPanel
        admin_panel = AdminPanel()
        admin_panel.mainloop()

    def create_button_containerOut(self):
        """Cria o container para botões de ação."""
        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, fill="y", expand=True)

        ctk.CTkButton(
            master=button_container, text="Sair", command=self.quit_app
        ).pack(pady=20, padx=10, side="left")

        ctk.CTkButton(
            master=button_container, text="Voltar", command=self.retornar
        ).pack(pady=20, padx=10, side="left")