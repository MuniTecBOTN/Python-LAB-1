from customtkinter import *


COLOR_PRIMARIO = "#2a00ac"
COLOR_SECUNDARIO  = "#81dc00"
COLOR_VERDE = "#10B981"
COLOR_ROJO = "#EF4444"
COLOR_BLANCO = "#FFFFFF"
COLOR_FONDO ="#e3e5f3"
COLOR_BORDE ="#e3e5f3"
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


ventana.mainloop()