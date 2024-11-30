import customtkinter as ctk
import utility.center as center


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

        # Cabeçalhos da tabela
        headers = ["SEG", "TER", "QUA", "QUI", "SEX"]
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                master=table_frame, text=header, font=("Arial Bold", 16), anchor="center"
            ).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        # Conteúdo do cronograma
        schedule = [
            ["Introdução à Programação\nSilva\n08:00-10:00\nCOMP101", "", 
            "Estruturas de Dados\nOliveira\n08:00-10:00\nCOMP201", "", 
            "Engenharia de Software\nSantos\n09:00-11:30\nCOMP301"],
            ["", "Banco de Dados\nPereira\n14:00-16:00\nCOMP302", 
            "", "Redes de Computadores\nFernandes\n16:30-18:30\nCOMP401", 
            "Banco de Dados\nPereira\n14:00-16:00\nCOMP302"],
            ["", "Algoritmos e Complexidade\nCosta\n10:00-12:00\nCOMP202", 
            "", "", ""],
        ]

        # Criando células da tabela
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