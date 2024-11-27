import os
import sys
sys.path.insert(1, os.getcwd())
from database import connect_db  # Importa a função do script de banco de dados
import customtkinter as ctk
import tkinter
import utility.center as center

app = ctk.CTk()

def quit():
    app.destroy()

def retornar():
    app.destroy()
    import main

app.geometry(center.CenterWindowToDisplay(app, 800, 600))

app.title("Painel do Administrador")

ctk.CTkLabel(app, text="Administrador", font=("Arial bold", 24)).pack(pady=20)

# Criação de um frame container para organizar os frames lado a lado
frame_container = ctk.CTkFrame(master=app)
frame_container.pack(pady=20, fill="both", expand=True)

# Frame Modificar
Modificar = ctk.CTkFrame(master=frame_container, width=200, height=200)
Modificar.pack(side="left", padx=(80,20), pady=20, fill="y")

ModificarTitulo = ctk.CTkLabel(master=Modificar, text="Modificar", fg_color="transparent")
ModificarTitulo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

btnMateria = ctk.CTkButton(master=Modificar, text="Matéria")
btnMateria.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

btnFaculdades = ctk.CTkButton(master=Modificar, text="Faculdades")
btnFaculdades.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

btnEstudantes = ctk.CTkButton(master=Modificar, text="Estudantes")
btnEstudantes.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# Frame Timetable
Timetable = ctk.CTkFrame(master=frame_container, width=400, height=200)
Timetable.pack(side="left", padx=40, pady=20, fill="y")

TimetableTiulo = ctk.CTkLabel(master=Timetable, text="Cronograma de Aulas", fg_color="transparent")
TimetableTiulo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

cronogramaAulas = ctk.CTkButton(master=Timetable, text="Cronograma de Aulas")
cronogramaAulas.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

btnViewBySection = ctk.CTkButton(master=Timetable, text="Ver por seção")
btnViewBySection.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

btnViewByFaculty = ctk.CTkButton(master=Timetable, text="Ver por Faculdades")
btnViewByFaculty.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# Botão Sair

button_container = ctk.CTkFrame(master=app, fg_color="transparent")
button_container.pack(pady=20, fill="y", expand=True )

btnSair = ctk.CTkButton(master=button_container, text="Sair", command=quit)
btnSair.pack(pady=20, padx=10, side="left")

btnVoltar = ctk.CTkButton(master=button_container, text="voltar", command=retornar)
btnVoltar.pack(pady=20, padx=10, side="left")

app.mainloop()

