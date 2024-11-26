import customtkinter as ctk
import sqlite3
from database import connect_db  # Importa a função do script de banco de dados
import utility.center as center
import cursos.cursos as cursos



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
        status_label.configure(text="Erro: Usuário já existe.", text_color="red")
    finally:
        conn.close()

def login():
    """Função para realizar o login de um usuário."""
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        status_label.configure(text="Preencha todos os campos!", text_color="red")
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
        status_label.configure(text="Login realizado com sucesso!", text_color="green")
        cursos.main()
        app.destroy()
    else:
        status_label.configure(text="Usuário ou senha incorretos.", text_color="red")

# Configuração principal da aplicação
app = ctk.CTk()
# Tamanho da janela e posicionamento no centro da tela
app.geometry(center.CenterWindowToDisplay(app, 400, 350))
# abrir posição da janela no centro da tela
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

# Botão para logar
login_button = ctk.CTkButton(app, text="Logar", command=login)
login_button.pack(pady=5)

# Label para exibir mensagens de status
status_label = ctk.CTkLabel(app, text="")
status_label.pack()

# Iniciar a aplicação
app.mainloop()
