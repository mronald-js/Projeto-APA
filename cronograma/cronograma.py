import customtkinter as ctk
import utility.center as center
import algoritmos.TimeTabling_Modelo_Alg_Guloso_UI as alg_guloso

class Cronograma(ctk.CTk):

    def __init__(self, user):
        super().__init__()
        self.geometry(center.CenterWindowToDisplay(self, 800, 600))
        self.title("Visualizar Timetabling")
        self.user = user

        # Ajustar a estrutura de alocação
        self.alocacao_ajustada = self.ajustar_alocacao()

        self.create_widgets()
        self.create_button_container()

    def ajustar_alocacao(self):
        """
        Ajusta a estrutura de alocação do algoritmo para o formato esperado pela interface.
        """
        # Obtém a alocação diretamente no formato esperado: {dia: {período: {sala: professor}}}
        try:
            alocacao = alg_guloso.alocar_aulas_guloso()
            return alocacao
        except Exception as e:
            print(f"Erro ao ajustar a alocação: {e}")
            return None  # Retorna None em caso de erro

    def create_widgets(self):
        # Título Principal
        titulo = ctk.CTkLabel(self, text="2024 Timetabling", font=("Arial Bold", 24), anchor="center", text_color="#333333")
        titulo.pack(pady=20)

        # Criação do frame container para a tabela
        table_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#F0F0F0")  # Cor de fundo clara para o frame
        table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Configuração de layout da tabela
        table_frame.grid_columnconfigure(0, weight=1)
        for i in range(len(alg_guloso.salas) + 1):
            table_frame.grid_columnconfigure(i, weight=1)

        # Cabeçalhos da tabela (em cor escura e fundo contrastante)
        headers = ["Dia/Sala"] + alg_guloso.salas
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                master=table_frame,
                text=header,
                font=("Arial Bold", 14),
                fg_color="#1F1F1F",  # Cor escura para o fundo do cabeçalho
                text_color="white",  # Cor clara para o texto
                corner_radius=5,
                padx=10,
                pady=5,
                anchor="center"
            ).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        # Exibir a grade horária
        row_index = 1
        for dia, alocacao_dia in self.alocacao_ajustada.items():
            for periodo, alocacao_periodo in alocacao_dia.items():
                # Exibe o dia e o período
                ctk.CTkLabel(
                    master=table_frame,
                    text=f"{dia} - {periodo}",
                    font=("Arial", 12, "bold"),
                    fg_color="#E0E0E0",  # Fundo claro para os títulos das linhas
                    text_color="#333333",  # Cor escura para o texto
                    corner_radius=5,
                    padx=10,
                    pady=5,
                    anchor="center"
                ).grid(row=row_index, column=0, padx=5, pady=5, sticky="nsew")

                # Preenche as salas com os professores alocados
                for col_index, sala in enumerate(alg_guloso.salas, start=1):
                    professor = alocacao_periodo.get(str(sala), None)  # Acesso correto
                    texto = f"Prof. {professor}" if professor is not None else "-"
                    ctk.CTkLabel(
                        master=table_frame,
                        text=texto,
                        font=("Arial", 12),
                        fg_color="#FFFFFF" if (row_index % 2 == 0) else "#F9F9F9",  # Linhas claras e escuras
                        text_color="#333333",  # Cor escura para o texto
                        corner_radius=5,
                        padx=10,
                        pady=5,
                        anchor="center"
                    ).grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

                row_index += 1

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
        self.destroy()
        if user == 'admin':
            from admin.admin import AdminPanel
            app = AdminPanel()
            app.mainloop()
        else:
            from ui import App
            app = App()
            app.mainloop()
