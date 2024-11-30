import customtkinter as ctk
import tkinter
import os
import sys
sys.path.insert(1, os.getcwd())
from banco.database import connect_db
import utility.center as center

class materiasControle(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry(center.CenterWindowToDisplay(self, 800, 600))
        self.title("Modificar Matérias")
        self.create_widgets()
        self.create_button()
        self.create_button_containerOut()

    def create_widgets(self):
        # Título Principal
        ctk.CTkLabel(self, text="Modificar Materias", font=("Arial Bold", 24)).pack(pady=20)

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        headers = ["ID", "Nome", "Carga Horária", "Faculdade"]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subjects")
        subjects = cursor.fetchall()
        conn.close()
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                master=table_frame, text=header, font=("Arial Bold", 16), anchor="center"
            ).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
        for row, subject in enumerate(subjects, start=1):
            for col, content in enumerate(subject):
                cell = ctk.CTkLabel(
                    master=table_frame,
                    text=content,
                    font=("Arial", 12),
                    anchor="center",
                    wraplength=150,
                    justify="center",
                    fg_color="#DCE4EE" if content else None,
                    text_color="black"
                )
                cell.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        for col in range(len(headers)):
            table_frame.columnconfigure(col, weight=1)
        for row in range(len(subjects) + 1):
            table_frame.rowconfigure(row, weight=1)

    def create_button(self):
        """Cria o container para os botões principais."""
        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, fill="y", side="top", expand=True)  # Posicionar no topo

        ctk.CTkButton(button_container, text="Adicionar Matéria", command=self.add_subject).pack(
            pady=5, padx=10, side="left"
        )
        ctk.CTkButton(button_container, text="Remover Matéria", command=self.remove_subject).pack(
            pady=5, padx=10, side="left"
        )
        ctk.CTkButton(button_container, text="Atualizar Matéria", command=self.update_subject).pack(
            pady=5, padx=10, side="left"
        )
    
    def add_subject(self):
        pass # Implementar
    
    def remove_subject(self):
        pass

    def update_subject(self):
        pass

    def create_button_containerOut(self):
        """Cria o container para botões de ação."""
        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, side="bottom", fill="y", expand=True)

        ctk.CTkButton(
        master=button_container, text="Sair", command=self.quit_app
        ).pack(pady=20, padx=10, side="left")

        ctk.CTkButton(
        master=button_container, text="Voltar", command=self.retornar
        ).pack(pady=20, padx=10, side="left")

    def quit_app(self):
        """Fecha a aplicação."""
        self.destroy()

    def retornar(self):
        """Retorna para a tela do admin."""
        # Evita import circular
        from admin.admin import AdminPanel  # Importa a classe AdminPanel do arquivo admin
        self.destroy()  # Fecha a janela atual
        admin_panel = AdminPanel()  # Cria a instância da classe AdminPanel
        admin_panel.mainloop()
