from customtkinter import *

import string
import secrets
import random
    
set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("480x640")

# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)

# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           fg_color="#d6d6d6",
                           corner_radius=0)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0,weight=1)

frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_rowconfigure(1,weight=1)
frame_principal.grid_rowconfigure(2,weight=1)
frame_principal.grid_rowconfigure(3,weight=1)
frame_principal.grid_rowconfigure(4,weight=1)
frame_principal.grid_rowconfigure(5,weight=1)
frame_principal.grid_rowconfigure(6,weight=1)
frame_principal.grid_rowconfigure(7,weight=1)
frame_principal.grid_rowconfigure(8,weight=1)
frame_principal.grid_rowconfigure(9,weight=1)
frame_principal.grid_rowconfigure(10,weight=1)

#------------------------- FUNCIONES --------------------------
def copiar_portapapeles():
    
    ventana.clipboard_clear()
    ventana.clipboard_append(entry_resultado.get())


def generar_contraseña(): 
    longitud = int(valor_slider.get())

    caracteres = ""
    contraseña = ""
    
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
        contraseña += secrets.choice(string.ascii_lowercase)
        
    if var_mayusculas.get():
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
        entry_resultado.insert(0, contraseña) 
       
    if not caracteres:
        entry_resultado.delete(0, "end")
        entry_resultado.insert(0, "selecciona al menos una opción") 
        return

    for i in range(longitud - len (contraseña)):
        contraseña += secrets.choice(caracteres)
    
        contraseña = "".join(random.sample(contraseña, len(contraseña)))
    


#----------------- TEXTO SUPERIOR ------------------------

texto_superior = CTkLabel(
    master=frame_principal,
    width=300,
    height=80,
    text="🔐 GENERADOR DE CONTRASEÑAS",
    font=("Montserrat", 18,"bold"),
    text_color="#000000",
    fg_color="transparent"
    )

texto_superior.grid(row = 0, column = 0,columnspan=2, sticky="nsew")

#------------------ SLIDER -------------------------------

def actualizar_label_longitud(valor):
    etiqueta_longitud.configure(text=f"Longitud: {int(valor)}")

valor_slider = IntVar(value=0)
slider = CTkSlider(
    master=frame_principal,
    from_=4,
    to=32,
    number_of_steps=100,
    width=400,
    fg_color="#505050",
    progress_color="#b9b9b9",
    button_color="#223ac2",
    button_hover_color="#81dc00",
    command=actualizar_label_longitud,
)

slider.grid(row=1,column=0)    
    
#-------------------- ETIQUETA LONGITUD -----------------------

etiqueta_longitud= CTkLabel(
    master=frame_principal,
    width=300,
    height=80,
    text="Longitud:",
    font=("Montserrat", 16,"bold"),
    text_color="#000000",
    fg_color="transparent"
    
)
etiqueta_longitud.grid(row = 2, column = 0,columnspan=2, sticky="nsew")

#------------------ CHECK BOX -------------------------------

var_minusculas = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir minúsculas (a-z)")
checkbox = CTkCheckBox(
    master=frame_principal,
    checkbox_width=20,
    checkbox_height=20,
    corner_radius=0,
    border_width=3,
    fg_color="#81dc00",
    hover_color="#2a00ac",
    textvariable=texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=var_minusculas,
    font=("Montserrat", 16, "bold"),
)

checkbox.grid(row=3,column=0)

var_mayusculas = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir mayúsculas (A-Z)")
checkbox = CTkCheckBox(
    master=frame_principal,
    checkbox_width=20,
    checkbox_height=20,
    corner_radius=0,
    border_width=3,
    fg_color="#81dc00",
    hover_color="#2a00ac",
    textvariable=texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=var_mayusculas,
    font=("Montserrat", 16, "bold"),
)

checkbox.grid(row=4,column=0)

var_numeros = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir números (0-9)")
checkbox = CTkCheckBox(
    master=frame_principal,
    checkbox_width=20,
    checkbox_height=20,
    corner_radius=0,
    border_width=3,
    fg_color="#81dc00",
    hover_color="#2a00ac",
    textvariable=texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=var_numeros,
    font=("Montserrat", 16, "bold"),
)

checkbox.grid(row=5,column=0)


var_simbolos = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir símbolos (!@#...)")
checkbox = CTkCheckBox(
    master=frame_principal,
    checkbox_width=20,
    checkbox_height=20,
    corner_radius=0,
    border_width=3,
    fg_color="#81dc00",
    hover_color="#2a00ac",
    textvariable=texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=var_simbolos,
    font=("Montserrat", 16, "bold"),
)

checkbox.grid(row=6,column=0)

#---------------- CAMPO DE TEXTO ---------------

entry_resultado = CTkEntry(
    master=frame_principal,
    width=400,
    border_width=2,
    corner_radius=7,
    placeholder_text="......",
    justify="center",
    font=("Montserrat", 16, "bold"),
)
entry_resultado.grid(row=7,column=0,)

#--------------- CAMPO BOTONES -------------------

boton_generar = CTkButton(
    master=frame_principal,
    width=120,
    height=30,
    text="Generar",
    fg_color="#2a00ac",
    hover_color="#81dc00",
    text_color="#ffffff",
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    command=generar_contraseña
)

boton_generar.grid(row=8, column=0)

boton_copiar = CTkButton(
    master=frame_principal,
    width=120,
    height=30,
    text="Copiar al portapeles",
    fg_color="#2a00ac",
    hover_color="#81dc00",
    text_color="#ffffff",
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    command=copiar_portapapeles
)

boton_copiar.grid(row=9, column=0)

#----------------------- ETIQUETA DE MENSAJE ------------------

etiqueta_informacion= CTkLabel(
    master=frame_principal,
    width=300,
    height=80,
    text="Contraseña copiada al portapapeles",
    font=("Montserrat", 16,"bold"),
    text_color="#000000",
    fg_color="transparent"
    
)
etiqueta_informacion.grid(row = 10, column = 0,columnspan=2, sticky="nsew")


ventana.mainloop()