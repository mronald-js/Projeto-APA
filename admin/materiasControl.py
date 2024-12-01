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
        # Vai abrir uma nova janela para adicionar uma matéria, com basicamente 4 campos: ID, Nome, Carga horária e Id do curso vinculado
        add_subject_window = ctk.CTk()
        add_subject_window.geometry(center.CenterWindowToDisplay(add_subject_window, 400, 400))
        add_subject_window.title("Adicionar Matéria")
        ctk.CTkLabel(add_subject_window, text="Adicionar Matéria", font=("Arial Bold", 24)).pack(pady=20)
        ctk.CTkLabel(add_subject_window, text="ID:").pack(pady=5)
        id_entry = ctk.CTkEntry(add_subject_window)
        id_entry.pack(pady=5)
        ctk.CTkLabel(add_subject_window, text="Nome:").pack(pady=5)
        name_entry = ctk.CTkEntry(add_subject_window)
        name_entry.pack(pady=5)
        ctk.CTkLabel(add_subject_window, text="Carga Horária:").pack(pady=5)
        cargaHoraria_entry = ctk.CTkEntry(add_subject_window)
        cargaHoraria_entry.pack(pady=5)

        ctk.CTkLabel(add_subject_window, text="ID do Curso:").pack(pady=5)
        idCurso_entry = ctk.CTkEntry(add_subject_window)
        idCurso_entry.pack(pady=5)
        ctk.CTkButton(add_subject_window, text="Adicionar", command=lambda: self.add_subject_to_db(
            id_entry.get(), name_entry.get(), cargaHoraria_entry.get(), idCurso_entry.get()
        )).pack(pady=5)

        add_subject_window.mainloop()
    
    def remove_subject(self):
        # Vai abrir uma nova janela para remover uma matéria, com basicamente 1 campo: ID
        remove_subject_window = ctk.CTk()
        remove_subject_window.geometry(center.CenterWindowToDisplay(remove_subject_window, 400, 400))
        remove_subject_window.title("Remover Matéria")
        ctk.CTkLabel(remove_subject_window, text="Remover Matéria", font=("Arial Bold", 24)).pack(pady=20)
        ctk.CTkLabel(remove_subject_window, text="ID:").pack(pady=5)
        id_entry = ctk.CTkEntry(remove_subject_window)
        id_entry.pack(pady=5)
        ctk.CTkButton(remove_subject_window, text="Remover", command=lambda: self.remove_subject_from_db(
            id_entry.get()
        )).pack(pady=5)            

        remove_subject_window.mainloop()

    def update_subject(self):
        # Vai abrir uma nova janela para atualizar uma matéria, com basicamente 4 campos: ID, Nome, Carga horária e Id do curso vinculado
        update_subject_window = ctk.CTk()
        update_subject_window.geometry(center.CenterWindowToDisplay(update_subject_window, 400, 400))
        update_subject_window.title("Atualizar Matéria")
        ctk.CTkLabel(update_subject_window, text="Atualizar Matéria", font=("Arial Bold", 24)).pack(pady=20)
        ctk.CTkLabel(update_subject_window, text="ID:").pack(pady=5)
        id_entry = ctk.CTkEntry(update_subject_window)
        id_entry.pack(pady=5)
        ctk.CTkLabel(update_subject_window, text="Nome:").pack(pady=5)
        name_entry = ctk.CTkEntry(update_subject_window)
        name_entry.pack(pady=5)
        ctk.CTkLabel(update_subject_window, text="Carga Horária:").pack(pady=5)
        cargaHoraria_entry = ctk.CTkEntry(update_subject_window)
        cargaHoraria_entry.pack(pady=5)
        ctk.CTkLabel(update_subject_window, text="ID do Curso:").pack(pady=5)
        idCurso_entry = ctk.CTkEntry(update_subject_window)
        idCurso_entry.pack(pady=5)
        ctk.CTkButton(update_subject_window, text="Atualizar", command=lambda: self.update_subject_from_db(
            id_entry.get(), name_entry.get(), cargaHoraria_entry.get(), idCurso_entry.get()
        )).pack(pady=5)

        update_subject_window.mainloop()

    def add_subject_to_db(self, id, name, cargaHoraria, idCurso):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subjects (materia_id, materia_name, materia_cargaHoraria, materia_curso) VALUES (?, ?, ?, ?)", (id, name, cargaHoraria, idCurso))
        conn.commit()
        conn.close()
        self.destroy()
        materiasControle().mainloop()
    
    def remove_subject_from_db(self, id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM subjects WHERE materia_id=?", (id,))
        conn.commit()
        conn.close()
        self.destroy()
        materiasControle().mainloop()
    
    def update_subject_from_db(self, id, name, cargaHoraria, idCurso):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE subjects SET materia_name=?, materia_cargaHoraria=?, materia_curso=? WHERE materia_id=?", (name, cargaHoraria, idCurso, id))
        conn.commit()
        conn.close()
        self.destroy()
        materiasControle().mainloop()

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
