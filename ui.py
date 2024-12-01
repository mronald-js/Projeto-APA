import customtkinter as ctk
import tkinter
import sqlite3
from banco.database import *
import utility.center as center

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(center.CenterWindowToDisplay(self, 800, 600))
        self.title("Cadastro de Usuário")
        
        # Componentes da interface
        self.username_entry = ctk.CTkEntry(self, width=300)
        self.password_entry = ctk.CTkEntry(self, width=300, show="*")
        self.profile_combobox = ctk.CTkComboBox(self, values=["admin", "student"], width=300)
        self.status_label = ctk.CTkLabel(self, text="")
        
        self.create_ui()
    
    def create_ui(self):
        ctk.CTkLabel(self, text="Nome de Usuário:").pack(pady=(120, 0))
        self.username_entry.pack(pady=5)
        
        ctk.CTkLabel(self, text="Senha:").pack(pady=(10, 0))
        self.password_entry.pack(pady=5)
        
        show_button = ctk.CTkButton(master=self.password_entry, command=self.show_password, width=60, text="Mostrar")
        show_button.place(relx=1, rely=0.5, anchor=tkinter.E)
        
        ctk.CTkLabel(self, text="Tipo de Perfil:").pack(pady=(10, 0))
        self.profile_combobox.set("Selecione...")
        self.profile_combobox.pack(pady=5)
        
        create_button = ctk.CTkButton(self, text="Criar Usuário", command=self.create_user)
        create_button.pack(pady=20)
        
        login_button = ctk.CTkButton(self, text="Logar", command=self.login)
        login_button.pack(pady=5)
        
        self.status_label.pack()
    
    def show_password(self):
        hide_button = ctk.CTkButton(master=self.password_entry, command=self.hide_password, width=60, text="Esconder")
        hide_button.place(relx=1, rely=0.5, anchor=tkinter.E)
        self.password_entry.configure(show="")
    
    def hide_password(self):
        show_button = ctk.CTkButton(master=self.password_entry, command=self.show_password, width=60, text="Mostrar")
        show_button.place(relx=1, rely=0.5, anchor=tkinter.E)
        self.password_entry.configure(show="*")
    
    def create_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        profile_type = self.profile_combobox.get()
        
        if not username or not password or profile_type == "Selecione...":
            self.status_label.configure(text="Preencha todos os campos!", text_color="red")
            return
        
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, profile_type) VALUES (?, ?, ?)",
                (username, password, profile_type)
            )
            conn.commit()
            self.status_label.configure(text="Usuário criado com sucesso!", text_color="green")
        except sqlite3.IntegrityError:
            self.status_label.configure(text="Erro: Usuário já existe.", text_color="red")
        finally:
            conn.close()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            self.status_label.configure(text="Preencha todos os campos!", text_color="red")
            return
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()
        
        if user:
            self.status_label.configure(text="Login realizado com sucesso!", text_color="green")
            
            if self.profile_combobox.get() == "admin":
                from admin.admin import AdminPanel  # Importa a classe AdminPanel do arquivo admin
                self.destroy()  # Fecha a janela atual
                admin_panel = AdminPanel()  # Cria a instância da classe AdminPanel
                admin_panel.mainloop()     # Inicia o loop principal do painel admin
            else:
                from cronograma.cronograma import Cronograma  # Importa a classe Cronograma do arquivo cronograma
                self.destroy()
                cronograma = Cronograma(user='student')  # Chama a lógica do módulo de cronograma
                cronograma.mainloop()  # Inicia o loop principal do cronograma
        else:
            self.status_label.configure(text="Usuário Inexistente ou dados incorretos.", text_color="red")
