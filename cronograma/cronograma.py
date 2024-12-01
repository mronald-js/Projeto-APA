import customtkinter as ctk
import utility.center as center
from banco.database import connect_db

class schedule:
    def __init__(self, nome, horario):
        self.nome = nome
        self.horario = horario

class Cronograma(ctk.CTk):

    def __init__(self, user):
        super().__init__()
        self.geometry(center.CenterWindowToDisplay(self, 800, 600))
        self.title("Visualizar Cronograma")
        self.create_widgets()
        self.create_button_container()
        self.user = user

    def create_widgets(self):
        # Título Principal
        ctk.CTkLabel(self, text="Primeiro Semestre 2024 Cronograma", font=("Arial Bold", 24)).pack(pady=20)

        # Criação do frame container para a tabela
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        conn = connect_db()
        cursor = conn.cursor()

        # # Cabeçalhos da tabela
        # headers = ["SEG", "TER", "QUA", "QUI", "SEX"]
        # for col, header in enumerate(headers):
        #     ctk.CTkLabel(
        #         master=table_frame, text=header, font=("Arial Bold", 16), anchor="center"
        #     ).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        # Cabeçalhos da tabela a partir do banco de dados
        cursor.execute("SELECT * FROM days")
        days = cursor.fetchall()
        headers = []
        for day in days:
            headers.append(day[1])
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                master=table_frame, text=header, font=("Arial Bold", 16), anchor="center"
            ).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        cursor.execute("SELECT * FROM subjects")
        subjects = cursor.fetchall()

        schedule = []
        #se não estiver vazio
        if subjects:
            for subject in subjects:
                print(subject)
                schedule.append([f"{subject[1]}\n{subject[2]}", "", "", "", ""])
        else:
            schedule = [
                ["", "", "", "", ""],
                ["", "", "", "", ""],
                ["", "", "", "", ""],
            ]

        # Conteúdo do cronograma
        # schedule = [
        #     ["Introdução à Programação\n08:00-10:00", "", 
        #     "Estruturas de Dados\n08:00-10:00", "", 
        #     "Engenharia de Software\n09:00-11:30"],
        #     ["", "Banco de Dados\n14:00-16:00", 
        #     "", "Redes de Computadores\n16:30-18:30", 
        #     "Banco de Dados\n14:00-16:00"],
        #     ["", "Algoritmos e Complexidade\n10:00-12:00", 
        #     "", "", ""],
        # ]

        # Criando células da tabela a partir do schedule e separando em conjunto com os dias
        for row, day_schedule in enumerate(schedule, start=1):
            for col, content in enumerate(day_schedule):
                cell = ctk.CTkLabel(
                    master=table_frame,
                    text=content,  # Texto de cada célula
                    font=("Arial", 12),
                    anchor="center",
                    wraplength=150,  # Ajusta textos longos
                    justify="center",  # Centraliza o texto
                    fg_color="#DCE4EE" if content else None,  # Cor de fundo
                    text_color="black"  # Cor do texto
                )
                cell.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Ajuste das proporções das colunas e linhas
        for col in range(len(headers)):
            table_frame.columnconfigure(col, weight=1)
        for row in range(len(schedule) + 1):  # Incluindo os cabeçalhos
            table_frame.rowconfigure(row, weight=1)

    def create_button_container(self):
        """Cria o container para botões de ação."""
        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, fill="y", expand=True)

        ctk.CTkButton(
        master=button_container, text="Sair", command=self.quit_app
        ).pack(pady=20, padx=10, side="left")

        ctk.CTkButton(
        master=button_container, text="Voltar", command=lambda: self.retornar(user=self.user)
        ).pack(pady=20, padx=10, side="left")

    def quit_app(self):
        """Fecha a aplicação."""
        self.destroy()

    def retornar(self, user):
        """Retorna para a tela principal."""
        # Evita import circular
        self.destroy()
        if(user == 'admin'):
            from admin.admin import AdminPanel
            app = AdminPanel()
            app.mainloop()
        else:
            from ui import App
            app = App()
            app.mainloop()