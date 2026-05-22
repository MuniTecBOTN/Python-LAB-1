from customtkinter import *
# =========================================================
# COLORES
# =========================================================
COLOR_FONDO = "#e3e5f3"
COLOR_AZUL = "#143a81"
COLOR_AMARILLO = "#ffcf03"
COLOR_BLANCO = "#ffffff"
COLOR_ROJO = "#ea4f4f"
COLOR_VERDE = "#2ce429"
TRANSPARENTE = "transparent"

# =========================================================
# ESTILOS
# =========================================================
estilo_etiqueta_titulo = {
    "width":120,
    "height":30,
    "font":("Montserrat", 28),
    "text_color":COLOR_BLANCO,
    "fg_color":TRANSPARENTE,
}

estilo_etiqueta_normal = {
    "width":120,
    "height":30,
    "font":("Montserrat", 16),
    "text_color":COLOR_BLANCO,
    "fg_color":COLOR_AMARILLO,
}

estilo_campo={
    "width":200,
    "height":30,
    "fg_color":COLOR_BLANCO,
    "border_color":COLOR_BLANCO,
    "text_color":COLOR_AZUL,
    "justify":"center",
    "corner_radius":0,
    "placeholder_text":"...",
    "font":("Montserrat", 16),
}

estilo_lista = {
    "width":200,
    "height":30,
    "fg_color":COLOR_BLANCO,
    "text_color":COLOR_AZUL,
    "button_color":COLOR_AMARILLO,
    "dropdown_fg_color":COLOR_AZUL,
    "dropdown_text_color":COLOR_BLANCO,
    "dropdown_font":("Montserrat", 16),
    "anchor":"center",
    "corner_radius":0,
    "dynamic_resizing":False,
    "font":("Montserrat", 16),
}

estilo_boton={
    "width":120,
    "height":30,
    "fg_color":COLOR_AZUL,
    "hover_color":COLOR_AMARILLO,
    "text_color":COLOR_BLANCO,
    "font":("Montserrat", 16, "bold"),
    "corner_radius":0,
}
# =========================================================
# CONFIGURACIÓN GLOBAL
# =========================================================
set_appearance_mode("light")
set_default_color_theme("dark-blue")

# =========================================================
# APP PRINCIPAL
# =========================================================
ventana = CTk()

ventana.title("Sistema de Registro")
ventana.geometry("800x640")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# =========================================================
# DECLARACIÓN DE FRAMES
# =========================================================
frame_principal = CTkFrame(
    master=ventana,
    fg_color=COLOR_FONDO,
    corner_radius=0
)
frame_principal.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10
)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)

frame_superior = CTkFrame(
    master=frame_principal,
    fg_color=COLOR_AZUL,
    corner_radius=0
)
frame_superior.grid(
    row=0,
    column=0,
    sticky="nsew",
)
frame_superior.grid_columnconfigure(0,weight=1)
frame_superior.grid_rowconfigure(0,weight=1)

frame_central = CTkFrame(
    master=frame_principal,
    fg_color=COLOR_FONDO,
    corner_radius=0
)
frame_central.grid(
    row=1,
    column=0,
    sticky="nsew",
)
frame_central.grid_columnconfigure(0,weight=1)
frame_central.grid_columnconfigure(1,weight=1)
frame_central.grid_rowconfigure([0,1,2,3,4,5,6],weight=1)


frame_inferior = CTkFrame(
    master=frame_principal,
    fg_color=COLOR_AZUL,
    corner_radius=0
)
frame_inferior.grid(
    row=2,
    column=0,
    sticky="nsew",
)
frame_inferior.grid_columnconfigure(0,weight=1)
frame_inferior.grid_rowconfigure(0,weight=1)

frame_inferior_interno = CTkFrame(
    master=frame_inferior,
    fg_color=TRANSPARENTE,
    corner_radius=0
)
frame_inferior_interno.grid(
    row=0,
    column=0,
    sticky="nsew",
)
frame_inferior_interno.grid_columnconfigure([0,1],weight=1)
frame_inferior_interno.grid_rowconfigure(0,weight=1)
# =========================================================
# ELEMENTOS FRAME SUPERIROR
# =========================================================
etiqueta_titulo = CTkLabel(
    master=frame_superior,
    text="🎬 CINE PYTHON",
    **estilo_etiqueta_titulo
    )

etiqueta_titulo.grid(
    row=0,
    column=0
    )
# =========================================================
# ELEMENTOS FRAME CENTRAL
# =========================================================
etiqueta_pelicula = CTkLabel(
    master=frame_central,
    text="PELÍCULA: ",
    **estilo_etiqueta_normal
    )

etiqueta_pelicula.grid(
    row=0,
    column=0,
    sticky = "ew"
    )

campo_pelicula = CTkOptionMenu(
    master=frame_central,
    **estilo_lista
)

campo_pelicula.grid(
    row=0,
    column=1,
    sticky="ew"
)

etiqueta_horario = CTkLabel(
    master=frame_central,
    text="HORARIO: ",
    **estilo_etiqueta_normal
    )

etiqueta_horario.grid(
    row=1,
    column=0,
    sticky = "ew"
    )

campo_horario = CTkOptionMenu(
    master=frame_central,
    **estilo_lista
)

campo_horario.grid(
    row=1,
    column=1,
    sticky="ew"
)

etiqueta_tipo = CTkLabel(
    master=frame_central,
    text="PELÍCULA: ",
    **estilo_etiqueta_normal
    )

etiqueta_tipo.grid(
    row=0,
    column=0,
    sticky = "ew"
    )

campo_tipo = CTkOptionMenu(
    master=frame_central,
    **estilo_lista
)

campo_tipo.grid(
    row=0,
    column=1,
    sticky="ew"
)

# =========================================================
# MAIN LOOP
# =========================================================
ventana.mainloop()