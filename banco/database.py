import sqlite3
from contextlib import closing  # Gerenciar conexões com segurança

DB_PATH = "./banco/timetable.db"  # Caminho do banco de dados

def connect_db():
    """Estabelece a conexão com o banco de dados e cria a tabela, se não existir."""
    try:

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Criação da tabela de usuários, se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                profile_type TEXT NOT NULL
            )
        """)


        # Criação da tabela de semestres, se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS semesters (
                semestre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                semestre_year INTEGER NOT NULL,
                semsetre_startOrEnd BOOLEAN NOT NULL
            )
        """)

        # Criação da tabela de faculdades, se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS colleges (
                faculdade_id INTEGER PRIMARY KEY AUTOINCREMENT,
                faculdade_name TEXT NOT NULL UNIQUE,
                faculdade_semesters INTEGER NOT NULL,
                FOREIGN KEY (faculdade_semesters) REFERENCES semesters(semestre_id)
            )
        """)

        # Criação da tabela de matérias, se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                materia_id INTEGER PRIMARY KEY AUTOINCREMENT,
                materia_name TEXT NOT NULL UNIQUE,
                materia_cargaHoraria INTEGER NOT NULL,
                FOREIGN KEY (materia_id) REFERENCES colleges(faculdade_id)
            )
        """)

        # Criação da tabela de estudantes, se não existir, estudante tem como chave estrangeira a faculdade, users e semestre
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                student_college INTEGER NOT NULL,
                student_semester INTEGER NOT NULL,
                FOREIGN KEY (student_college) REFERENCES colleges(faculdade_id),
                FOREIGN KEY (student_semester) REFERENCES semesters(semestre_id),
                FOREIGN KEY (student_matricula) REFERENCES users(user_id)
            )
        """)

        conn.commit()
        return conn
    
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def close_db(conn):
    """Fecha a conexão com o banco de dados."""
    try:
        if conn:
            conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao fechar a conexão: {e}")
