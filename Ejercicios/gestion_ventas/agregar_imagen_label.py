import os
from customtkinter import *

# pip install Pillow
from PIL import Image


set_appearance_mode("light")
set_default_color_theme("dark-blue")

# =========================================================
# APP PRINCIPAL
# =========================================================
ventana = CTk()

ventana.title("Sistema de Registro")
ventana.geometry("1600x920")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# =========================================================
# FRAME PRINCIPAL
# =========================================================
frame_principal = CTkFrame(
    master=ventana,
    fg_color="transparent",
    corner_radius=0,
)
frame_principal.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10,
)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
# =========================================================
# CARGAR IMAGEN
# =========================================================

ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(ruta_script, "imagenes/dragon.webp")

# Cargar imagen
imagen_nave = CTkImage(
    light_image=Image.open(ruta_imagen),
    dark_image=Image.open(ruta_imagen),
    size=(800, 800)
)

etiqueta_imagen = CTkLabel(
        master=frame_principal,
        image=imagen_nave, 
        text="",
)
etiqueta_imagen.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=10,
        pady=10,
    )

ventana.mainloop()