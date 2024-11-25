import customtkinter as ctk
import sqlite3
from database import connect_db  # Importa a função do script de banco de dados

def create_user():
    """Função para criar um usuário no banco de dados."""
    username = username_entry.get()
    password = password_entry.get()
    profile_type = profile_combobox.get()

    if not username or not password or not profile_type:
        status_label.configure(text="Preencha todos os campos!", text_color="red")
        return

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, profile_type) VALUES (?, ?, ?)",
            (username, password, profile_type)
        )
        conn.commit()
        status_label.configure(text="Usuário criado com sucesso!", text_color="green")
    except sqlite3.IntegrityError:
        status_label.configure(text="Erro: Nome de usuário já existe.", text_color="red")
    finally:
        conn.close()

# Configuração principal da aplicação
app = ctk.CTk()
app.geometry("400x350")
app.title("Cadastro de Usuário")

# Campo para nome de usuário
ctk.CTkLabel(app, text="Nome de Usuário:").pack(pady=(10, 0))
username_entry = ctk.CTkEntry(app, width=300)
username_entry.pack(pady=5)

# Campo para senha
ctk.CTkLabel(app, text="Senha:").pack(pady=(10, 0))
password_entry = ctk.CTkEntry(app, width=300, show="*")
password_entry.pack(pady=5)

# Dropdown (Combobox) para selecionar o tipo de usuário
ctk.CTkLabel(app, text="Tipo de Perfil:").pack(pady=(10, 0))
profile_combobox = ctk.CTkComboBox(
    app, values=["admin", "student"], width=300
)
profile_combobox.set("Selecione...")  # Texto padrão
profile_combobox.pack(pady=5)

# Botão para criar o usuário
create_button = ctk.CTkButton(app, text="Criar Usuário", command=create_user)
create_button.pack(pady=20)

# Label para exibir mensagens de status
status_label = ctk.CTkLabel(app, text="")
status_label.pack()

# Iniciar a aplicação
app.mainloop()
