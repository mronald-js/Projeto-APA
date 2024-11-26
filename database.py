import sqlite3

def connect_db():
    """Estabelece a conexão com o banco de dados e cria a tabela, se não existir."""

    conn = sqlite3.connect("./banco/timetable.db")
    cursor = conn.cursor()
    
    # Criação da tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            profile_type TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

def close_db(conn):
    """Fecha a conexão com o banco de dados."""
    if conn:
        conn.close()
