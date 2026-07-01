from customtkinter import *

COLOR_PRIMARIO = "#2a00ac"
COLOR_SECUNDARIO = "#81dc00"
COLOR_VERDE = "#10B981"
COLOR_ROJO = "#EF4444"
COLOR_BLANCO = "#FFFFFF"
COLOR_FONDO = "#e3e5f3"
COLOR_BORDE = "#e3e5f3"
TRANSPARENTE = "transparent"


ALTURA_ESTANDAR_CAMPO = 50
TAMAÑO_LETRA_NORMAL = 18
TAMAÑO_LETRA_TITULO = 28


ESTILO_DE_LETRA_NORMAL = ("Montserrat", TAMAÑO_LETRA_NORMAL)
ESTILO_DE_LETRA_TITULO = ("Montserrat", TAMAÑO_LETRA_TITULO)

set_default_color_theme("dark-blue")


ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("800x600")


# acá se configuran las columnas, con el weight se le da un peso a cada columna,
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)


# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------


frame_principal = CTkFrame(
    master=ventana,
    fg_color="#d72b48",
    corner_radius=0,
)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)


frame_izquierdo = CTkFrame(
    master=frame_principal,
    fg_color="#ff790c",
    corner_radius=0,
)

frame_izquierdo.grid_columnconfigure(0, weight=1)
frame_izquierdo.grid_columnconfigure(1, weight=1)

frame_izquierdo.grid_rowconfigure(0, weight=1)
frame_izquierdo.grid_rowconfigure(1, weight=1)


frame_derecho = CTkFrame(
    master=frame_principal,
    fg_color="#31f281",
    corner_radius=0,
)

frame_derecho.grid_columnconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(1, weight=1)


frame_interno_izquierdo_0_0 = CTkFrame(
    master=frame_izquierdo,
    fg_color="#c03ab5",
    corner_radius=0,
)


frame_interno_izquierdo_1_1 = CTkFrame(
    master=frame_izquierdo,
    fg_color="#3c9492",
    corner_radius=0,
)


frame_interno_derecho_0_0 = CTkFrame(
    master=frame_derecho,
    fg_color="#3c944c",
    corner_radius=0,
)


frame_interno_derecho_1_0 = CTkFrame(
    master=frame_derecho,
    fg_color="#19109b",
    corner_radius=0,
)

frame_principal.grid(
    row=0,
    column=0,
    sticky="snew",
    padx=10,
    pady=10,
)
frame_derecho.grid(
    row=0,
    column=1,
    sticky="snew",
    padx=10,
    pady=10,
)
frame_izquierdo.grid(
    row=0,
    column=0,
    sticky="snew",
    padx=10,
    pady=10,
)
frame_interno_izquierdo_0_0.grid(
    row=0,
    column=0,
    sticky="snew",
    padx=10,
    pady=10,
)
frame_interno_izquierdo_1_1.grid(
    row=1,
    column=1,
    sticky="snew",
    padx=10,
    pady=10,
)
frame_interno_derecho_0_0.grid(
    row=0,
    column=0,
    sticky="snew",
    padx=10,
    pady=10,
)
frame_interno_derecho_1_0.grid(
    row=1,
    column=0,
    sticky="snew",
    padx=10,
    pady=10,
)


ventana.mainloop()
