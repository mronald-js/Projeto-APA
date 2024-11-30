
import customtkinter as ctk
import tkinter
from banco.database import connect_db
import utility.center as center



class AdminPanel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(center.CenterWindowToDisplay(self, 800, 600))
        self.title("Painel do Administrador")
        
        self.create_widgets()

    def create_widgets(self):
        # Título Principal
        ctk.CTkLabel(self, text="Administrador", font=("Arial bold", 24)).pack(pady=20)

        # Criação do frame container
        frame_container = ctk.CTkFrame(master=self)
        frame_container.pack(pady=20, fill="both", expand=True)

        # Adicionar frames e botões
        self.create_modificar_frame(frame_container)
        self.create_timetable_frame(frame_container)
        self.create_button_container()

    def create_modificar_frame(self, parent):
        """Cria o frame de modificação."""
        modificar_frame = ctk.CTkFrame(master=parent, width=200, height=200)
        modificar_frame.pack(side="left", padx=(80, 20), pady=20, fill="y")

        ctk.CTkLabel(
            master=modificar_frame, text="Modificar", fg_color="transparent"
        ).place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        ctk.CTkButton(
            master=modificar_frame, text="Matéria", command=self.renderMaterias
        ).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        ctk.CTkButton(
            master=modificar_frame, text="Faculdades",  command=self.renderFaculdades
        ).place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def create_timetable_frame(self, parent):
        """Cria o frame do cronograma de aulas."""
        timetable_frame = ctk.CTkFrame(master=parent, width=400, height=200)
        timetable_frame.pack(side="left", padx=40, pady=20, fill="y", expand=True)

        ctk.CTkLabel(
            master=timetable_frame, text="Cronograma de Aulas", fg_color="transparent"
        ).place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        ctk.CTkButton(
            master=timetable_frame, text="Cronograma de Aulas", command=self.renderCronograma
        ).place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


    def create_button_container(self):
        """Cria o container para botões de ação."""
        button_container = ctk.CTkFrame(master=self, fg_color="transparent")
        button_container.pack(pady=20, fill="y", expand=True)

        ctk.CTkButton(
            master=button_container, text="Sair", command=self.quit_app
        ).pack(pady=20, padx=10, side="left")

        ctk.CTkButton(
            master=button_container, text="Voltar", command=self.retornar
        ).pack(pady=20, padx=10, side="left")

    def renderCronograma(self):
        # Evita import circular
        import os
        import sys
        sys.path.insert(1, os.getcwd())
        self.destroy()
        import cronograma.cronograma as cronograma
        cronograma = cronograma.Cronograma(user='admin')
        cronograma.mainloop()
    
    def renderMaterias(self):
        # Evita import circular
        import os
        import sys
        sys.path.insert(1, os.getcwd())
        self.destroy()
        from admin import materiasControl
        materiais = materiasControl.materiasControle()
        materiais.mainloop()
    
    def renderFaculdades(self):
        # Evita import circular
        import os
        import sys
        sys.path.insert(1, os.getcwd())
        self.destroy()
        from admin import faculdadeControl
        faculdade = faculdadeControl.FaculdadeControle()
        faculdade.mainloop()

    def quit_app(self):
        """Fecha a aplicação."""
        self.destroy()

    def retornar(self):
        """Retorna para a tela principal."""
        # Evita import circular
        import os
        import sys
        sys.path.insert(1, os.getcwd())
        self.destroy()
        import ui
        app = ui.App()
        app.mainloop()
