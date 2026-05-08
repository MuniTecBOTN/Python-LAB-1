from customtkinter import *

import string
import secrets

def actualizar_label_longitud(valor):
    etiqueta_longitud.configure(text=f"longitud:{int(valor)}")
    
set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("700x600")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------

# ------------------ FRAME PRINCIPAL ------------------
frame_principal = CTkFrame(master=ventana, fg_color="#B2B4BD", corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)
frame_principal.grid_rowconfigure(3, weight=1)
frame_principal.grid_rowconfigure(4, weight=1)
frame_principal.grid_rowconfigure(5, weight=1)
frame_principal.grid_rowconfigure(6, weight=1)
frame_principal.grid_rowconfigure(7, weight=1)
frame_principal.grid_rowconfigure(8, weight=1)
frame_principal.grid_rowconfigure(9, weight=1)
frame_principal.grid_rowconfigure(10, weight=1)


# ------------------ FRAME TÍTULO ------------------
frame_titulo = CTkFrame(master=frame_principal, height=80, fg_color="#246997", corner_radius=0)
frame_titulo.grid(row=1, column=0, sticky="new")

frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(1, weight=1)

# ------------------- FRAME SUPERIOR ------------------
frame_superior = CTkFrame(master=frame_principal,width=420, height=80, fg_color="transparent", corner_radius=0)
frame_superior.grid(row=2, column=0, sticky="s")

frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)
frame_superior.grid_propagate(False)


def generar_contraseña():
    longtud = int(actualizar_label_longitud.get())
    
    caracteres = ""
    contraseña = ""

    if var_minusculas.get():
        caracteres += string.ascii_lowercase
        contraseña += secrets.choice(string.ascii_lowercase)
        
    if var_mayuscula.get():
        caracteres += string.ascii_uppercase
        contraseña += secrets.choice(string.ascii_uppercase)
    
    if var_numeros.get():
        caracteres += string.digits
        contraseña += secrets.choice(string.digits)
        
    if var_simbolos.get():
        caracteres += string.punctuation
        contraseña += secrets.choice(string.punctuation)
        
    if not caracteres:
        
        entry_resultado.delete(0, "end")
        
        entry_resultado.insert(0,"selecciona al menos una opción")
        
        return
        
    for i in range(actualizar_label_longitud - len(contraseña)):
        contraseña += secrets.choice(caracteres)
        
    contraseña = "". join(random.sample(contraseña, len(contraseña)))
    
    entry_resultado.delete(0, "end")
    entry_resultado.insert(0,)
        

    def copiar_portapapeles()
    
        ventana.clipboard_clear()
        ventana.clipboard_append(entry_resultado.get())
        
        
        
# ------------------ LABELS ------------------
etiqueta_superior = CTkLabel(
    master=frame_principal,
    width=300,
    height=80,
    text="GENERADOR DE CONTRASEÑAS",
    font=("Montserrat", 30, "bold"),
    text_color="#080808",
    fg_color="transparent",
)
etiqueta_superior.grid(row=0, column=0, columnspan=2, sticky="nsew")

valor_slider = IntVar(value=0)
slider = CTkSlider(
    master=frame_principal,
    from_=4,
    to=32,
    command=actualizar_label_longitud,
    variable=valor_slider,
    number_of_steps=100,
    fg_color="#18e07c",
)
slider.grid(
    row=1,
    column=0,
)
    
etiqueta_longitud = CTkLabel(
    master=frame_principal,
    width=300,
    height=80,
    text="LONGITUD: 12",
    font=("Montserrat", 15, "bold"),
    text_color="#080808",
    fg_color="transparent",
)
etiqueta_longitud.grid(row=2, column=0, columnspan=3, sticky="nsew")


var_minusculas = BooleanVar(value=False)
checkbox_minusculas = CTkCheckBox(
    master=frame_principal,
    checkbox_width=40,
    checkbox_height=40,
    corner_radius=100,
    border_width=1,
    text="¿Incluir minusculas (a-z)?",
    onvalue=True,
    offvalue=False,
    variable=var_minusculas,
    font=("Montserrat", 16),
)

checkbox_minusculas.grid(
    row=3,
    column=0,
)

var_mayuscula = BooleanVar(value=False)
checkbox_mayuscula= CTkCheckBox(
    master=frame_principal,
    checkbox_width=40,
    checkbox_height=40,
    corner_radius=100,
    border_width=1,
    text="¿Incluir mayúculas (A-Z)?",
    onvalue=True,
    offvalue=False,
    variable=var_mayuscula,
    font=("Montserrat", 16),
)

checkbox_mayuscula.grid(
    row=4,
    column=0,
)

var_numeros = BooleanVar(value=False)
checkbox_numeros = CTkCheckBox(
    master=frame_principal,
    checkbox_width=40,
    checkbox_height=40,
    corner_radius=100,
    border_width=1,
    text="¿Incluir números (0-9)?",
    onvalue=True,
    offvalue=False,
    variable=var_numeros,
    font=("Montserrat", 16),
)

checkbox_numeros.grid(
    row=5,
    column=0,
)

var_simbolos = BooleanVar(value=False)
checkbox_simbolos = CTkCheckBox(
    master=frame_principal,
    checkbox_width=40,
    checkbox_height=40,
    corner_radius=100,
    border_width=1,
    text="¿Incluir simbolos (!Q#...)?",
    onvalue=True,
    offvalue=False,
    variable=var_simbolos,
    font=("Montserrat", 16),
)

checkbox_simbolos.grid(
    row=6,
    column=0,
)

#   Caja de texto - CTkTextBox
caja_texto = CTkTextbox(
    master=frame_principal,
    width=500,
    height=40,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_texto.grid(
    row=7,
    column=0, pady=5
)

#   Botón - CTkButton
def funcion_boton_1():
    print(f"Has presionado el Botón 1")


boton_1 = CTkButton(
    master=frame_principal,
    width=100,
    height=30,
    corner_radius=0,
    text="   Generar   ",
    anchor="center",
    font=("Montserrat", 16),
    fg_color="#246997",
    command=funcion_boton_1,
)

boton_1.grid(
    row=8,
    column=0,pady=10
)

#   Botón - CTkButton
def funcion_boton_1():
    print(f"Has presionado el Botón 2")

boton_2 = CTkButton(
    master=frame_principal,
    width=100,
    height=30,
    corner_radius=0,
    text="Copiar al portapapeles",
    anchor="center",
    font=("Montserrat", 16),
    fg_color="#246997",
    command=funcion_boton_1,
)

boton_2.grid(
    row=9,
    column=0, pady=10
)

etiqueta_superior = CTkLabel(
    master=frame_principal,
    width=300,
    height=80,
    text="contraseña copiada al portapapeles",
    font=("Montserrat", 10, "bold"),
    text_color="#080808",
    fg_color="transparent",
)
etiqueta_superior.grid(row=10, column=0, columnspan=2, sticky="nsew")
ventana.mainloop()
