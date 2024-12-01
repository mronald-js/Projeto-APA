import customtkinter as ctk
import tkinter
import os
import sys
sys.path.insert(1, os.getcwd())
from banco.database import connect_db
import utility.center as center

class FaculdadeControle(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry(center.CenterWindowToDisplay(self, 800, 600))
        self.title("Modificar Faculdades")
        self.create_widgets()
        self.create_button()
        self.create_button_containerOut()


    def create_widgets(self):
        # Título Principal
        ctk.CTkLabel(self, text="Modificar Faculdades", font=("Arial Bold", 24)).pack(pady=20)

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        headers = ["ID", "Nome"]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM colleges")
        colleges = cursor.fetchall()
        conn.close()
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                master=table_frame, text=header, font=("Arial Bold", 16), anchor="center"
            ).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
        for row, college in enumerate(colleges, start=1):
            for col, content in enumerate(college):
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
        for row in range(len(colleges) + 1):
            table_frame.rowconfigure(row, weight=1)
        
    def create_button(self):

        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, fill="y", side="top", expand=True)

        ctk.CTkButton(master=button_container, text="Adicionar Faculdade", command=self.add_college).pack(pady=5, padx=10, side="left")
        ctk.CTkButton(master=button_container, text="Remover Faculdade", command=self.remove_college).pack(pady=5, padx=10, side="left")
        ctk.CTkButton(master=button_container, text="Atualizar Faculdade", command=self.update_college).pack(pady=5, padx=10, side="left")

    def create_button_containerOut(self):
        """Cria o container para botões de ação."""
        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, fill="y", side="bottom", expand=True)

        ctk.CTkButton(
        master=button_container, text="Sair", command=self.quit_app
        ).pack(pady=20, padx=10, side="left")

        ctk.CTkButton(
        master=button_container, text="Voltar", command=self.retornar
        ).pack(pady=20, padx=10, side="left")

    def add_college(self):
        add_college_window = ctk.CTk()
        add_college_window.geometry(center.CenterWindowToDisplay(add_college_window, 400, 300))
        add_college_window.title("Adicionar Faculdade")
        #Id da faculdade
        ctk.CTkLabel(add_college_window, text="ID da Faculdade", font=("Arial", 12)).pack(pady=10)
        college_id = ctk.CTkEntry(add_college_window)
        college_id.pack(pady=10)
        ctk.CTkLabel(add_college_window, text="Nome da Faculdade", font=("Arial", 12)).pack(pady=10)
        college_name = ctk.CTkEntry(add_college_window)
        college_name.pack(pady=10)
        ctk.CTkButton(add_college_window, text="Adicionar", command=lambda: self.add_college_db(add_college_window, college_name, college_id)).pack(pady=10)
        add_college_window.mainloop()

    def add_college_db(self, add_college_window, college_name, college_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO colleges (faculdade_id, faculdade_name) VALUES (?, ?)", (college_id.get(), college_name.get()))
        conn.commit()
        conn.close()
        add_college_window.destroy()
        FaculdadeControle()
    
    def remove_college(self):
        remove_college_window = ctk.CTk()
        remove_college_window.geometry(center.CenterWindowToDisplay(remove_college_window, 400, 300))
        remove_college_window.title("Remover Faculdade")
        ctk.CTkLabel(remove_college_window, text="ID da Faculdade", font=("Arial", 12)).pack(pady=10)
        college_id = ctk.CTkEntry(remove_college_window)
        college_id.pack(pady=10)
        ctk.CTkButton(remove_college_window, text="Remover", command=lambda: self.remove_college_db(remove_college_window, college_id)).pack(pady=10)
        remove_college_window.mainloop()
    
    def remove_college_db(self, remove_college_window, college_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM colleges WHERE faculade_id=?", (college_id.get(),))
        conn.commit()
        conn.close()
        remove_college_window.destroy()
        FaculdadeControle()

    def update_college(self):
        update_college_window = ctk.CTk()
        update_college_window.geometry(center.CenterWindowToDisplay(update_college_window, 400, 300))
        update_college_window.title("Atualizar Faculdade")
        ctk.CTkLabel(update_college_window, text="ID da Faculdade", font=("Arial", 12)).pack(pady=10)
        college_id = ctk.CTkEntry(update_college_window)
        college_id.pack(pady=10)
        ctk.CTkLabel(update_college_window, text="Nome da Faculdade", font=("Arial", 12)).pack(pady=10)
        college_name = ctk.CTkEntry(update_college_window)
        college_name.pack(pady=10)
        ctk.CTkButton(update_college_window, text="Atualizar", command=lambda: self.update_college_db(update_college_window, college_name, college_id)).pack(pady=10)
        update_college_window.mainloop()

    def update_college_db(self, update_college_window, college_name, college_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE colleges SET faculdade_name=? WHERE faculdade_id=?", (college_name.get(), college_id.get()))
        conn.commit()
        conn.close()
        update_college_window.destroy()
        FaculdadeControle()

    def quit_app(self):
        """Fecha a aplicação."""
        self.destroy()

    def retornar(self):
        """Retorna para a tela principal."""
        # Evita import circular
        self.destroy()
        from admin.admin import AdminPanel  # Importa a classe AdminPanel do arquivo admin
        admin_panel = AdminPanel()  # Cria a instância da classe AdminPanel
        admin_panel.mainloop()
