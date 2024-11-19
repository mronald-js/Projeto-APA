import customtkinter as ctk

# Configuração principal da aplicação
app = ctk.CTk()
app.geometry("500x400")  # Dimensão da janela
app.title("Timetable - APA")

# Definir cores (fundo e botões)
app.configure(bg="black")

# Título
title_label = ctk.CTkLabel(
    app, 
    text="TIMETABLE - APA", 
    font=("Arial", 20, "bold"), 
    text_color="white"
)
title_label.pack(pady=20)  # Espaçamento superior

title_label = ctk.CTkLabel(
    app, 
    text="Selecione o seu perfil", 
    font=("Arial", 15), 
    text_color="white"
)
title_label.pack(pady=10)  # Espaçamento superior

# Botão Estudante
student_button = ctk.CTkButton(
    app, 
    text="Estudante", 
    width=200, 
    height=50, 
    fg_color="gray",  # Cor do botão
    text_color="white",  # Cor do texto
    corner_radius=8  # Arredondamento
)
student_button.pack(pady=10)  # Espaçamento entre elementos

# Botão Administrador
admin_button = ctk.CTkButton(
    app, 
    text="Administrador", 
    width=200, 
    height=50, 
    fg_color="gray", 
    text_color="white", 
    corner_radius=8
)
admin_button.pack(pady=10)

# Iniciar a aplicação
app.mainloop()