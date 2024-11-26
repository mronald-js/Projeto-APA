import customtkinter as ctk
import sqlite3
from database import connect_db  # Importa a função do script de banco de dados
import utility.center as center


def main():
    app = ctk.CTk()
    app.geometry(center.CenterWindowToDisplay(app, 400, 350))

    app.title("Cursos")
    ctk.CTkLabel(app, text="Seja Bem Vindo ao painel de Cursos!", font=("Arial", 14)).pack(pady=80);

    app.mainloop()