from customtkinter import *
import string
import secrets
import random

# =========================================================
# CONFIGURACIÓN GLOBAL
# =========================================================
set_appearance_mode("light")
set_default_color_theme("dark-blue")

# =========================================================
# COLORES
# =========================================================
COLOR_PRIMARIO = "#2a00ac"
COLOR_PRIMARIO_REALCE = "#4a16e6"
COLOR_SECUNDARIO = "#81dc00"
COLOR_VERDE = "#10B981"
COLOR_ROJO = "#EF4444"
COLOR_BLANCO = "#FFFFFF"
COLOR_FONDO = "#e3e5f3"
COLOR_BORDE = "#e3e5f3"
COLOR_SOMBRA = "#dcdfef"

COLOR_PRIMARIO_HOVER = "#3B0FD0"
COLOR_SECUNDARIO_HOVER = "#6FC000"
COLOR_VERDE_HOVER = "#0E9E6F"
COLOR_ROJO_HOVER = "#DC2626"
COLOR_BLANCO_HOVER = "#F5F5F5"
COLOR_FONDO_HOVER = "#D7DAEC"
COLOR_BORDE_HOVER = "#C8CEE8"

TRANSPARENTE = "transparent"
ALTURA_ESTANDAR_WIDGET = 30

TAMANO_LETRA_NORMAL = ALTURA_ESTANDAR_WIDGET*(2/5)
TAMANO_LETRA_TITULO = ALTURA_ESTANDAR_WIDGET/2

ESTILO_DE_LETRA_NORMAL = ("Montserrat", TAMANO_LETRA_NORMAL)
ESTILO_DE_LETRA_TITULO = ("Montserrat", TAMANO_LETRA_TITULO)





ESTILO_ENTRY = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "border_width": 1,
    "border_color": COLOR_BLANCO,
    "fg_color": COLOR_BLANCO,
    "text_color": COLOR_PRIMARIO,
    "placeholder_text_color": COLOR_SOMBRA,
    "justify": "center",
    "font": ESTILO_DE_LETRA_NORMAL,
    "state": "normal",
}


ESTILO_TEXTBOX = {
    "corner_radius": 0,
    "border_width": 0,
    "border_spacing": 3,
    "border_color": COLOR_FONDO,
    "fg_color": COLOR_BLANCO,
    "text_color": COLOR_PRIMARIO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "scrollbar_button_color": COLOR_PRIMARIO,
    "scrollbar_button_hover_color": COLOR_SECUNDARIO,
    "activate_scrollbars": True,
    "wrap": "word",
}


ESTILO_CHECKBOX = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "checkbox_width": (ALTURA_ESTANDAR_WIDGET*(2/3)),
    "checkbox_height": (ALTURA_ESTANDAR_WIDGET*(2/3)),
    "corner_radius": 0,
    "border_width": 2,
    "fg_color": COLOR_SECUNDARIO,
    "border_color": COLOR_PRIMARIO,
    "hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_PRIMARIO,
    "text_color_disabled": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "hover": True,
    "state": "normal",
}


ESTILO_RADIOBUTTON = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "radiobutton_width": (ALTURA_ESTANDAR_WIDGET/3),
    "radiobutton_height": (ALTURA_ESTANDAR_WIDGET/3),
    "corner_radius": 100,
    "border_width_unchecked": 2,
    "border_width_checked": 4,
    "fg_color": COLOR_SECUNDARIO,
    "border_color": COLOR_PRIMARIO,
    "hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_PRIMARIO,
    "text_color_disabled": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "hover": True,
    "state": "normal",
}


ESTILO_SWITCH = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "switch_width": ALTURA_ESTANDAR_WIDGET,
    "switch_height": (ALTURA_ESTANDAR_WIDGET/3),
    "border_width": 0,
    "fg_color": COLOR_SOMBRA,
    "border_color": COLOR_PRIMARIO,
    "progress_color": COLOR_SECUNDARIO,
    "button_color": COLOR_PRIMARIO,
    "button_hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_PRIMARIO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "state": "normal",
}


ESTILO_BOTON = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "border_width": 0,
    "border_spacing": 2,
    "fg_color": COLOR_PRIMARIO,
    "hover_color": COLOR_SECUNDARIO,
    "border_color": COLOR_PRIMARIO,
    "text_color": COLOR_BLANCO,
    "text_color_disabled": COLOR_FONDO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "state": "normal",
}


ESTILO_SEGMENTED_BUTTON = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "fg_color": COLOR_BLANCO,
    "selected_color": COLOR_SECUNDARIO,
    "selected_hover_color": COLOR_FONDO,
    "unselected_color": COLOR_PRIMARIO,
    "unselected_hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_BLANCO,
    "text_color_disabled": COLOR_BLANCO,
    "corner_radius": 0,
    "border_width": 2,
    "font": ESTILO_DE_LETRA_NORMAL,
    "dynamic_resizing": False,
    "state": "normal",
}


ESTILO_OPTIONMENU = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "fg_color": COLOR_PRIMARIO,
    "corner_radius": 0,
    "button_color": COLOR_SECUNDARIO,
    "button_hover_color": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "text_color": COLOR_BLANCO,
    "text_color_disabled": COLOR_SOMBRA,
    "dropdown_text_color": COLOR_BLANCO,
    "dropdown_fg_color": COLOR_PRIMARIO,
    "dropdown_font": ESTILO_DE_LETRA_NORMAL,
    "dropdown_hover_color": COLOR_SECUNDARIO,
    "hover": True,
    "dynamic_resizing": False,
    "state": "normal",
}


ESTILO_COMBOBOX = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "border_width": 0,
    "fg_color": COLOR_PRIMARIO,
    "border_color": COLOR_SECUNDARIO,
    "button_color": COLOR_SECUNDARIO,
    "button_hover_color": COLOR_SOMBRA,
    "dropdown_fg_color": COLOR_PRIMARIO,
    "dropdown_hover_color": COLOR_SECUNDARIO,
    "dropdown_text_color": COLOR_BLANCO,
    "text_color": COLOR_BLANCO,
    "text_color_disabled": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "dropdown_font": ESTILO_DE_LETRA_NORMAL,
    "hover": True,
    "state": "normal",
    "justify": "center",
}


ESTILO_SLIDER = {
    "height": (ALTURA_ESTANDAR_WIDGET / 2),
    "fg_color": COLOR_SOMBRA,
    "progress_color": COLOR_PRIMARIO,
    "button_color": COLOR_SECUNDARIO,
    "button_hover_color": COLOR_SECUNDARIO_HOVER,
    "corner_radius": 1,
    "button_corner_radius": 20,
    "orientation": "horizontal",
    "hover": True,
    "state": "normal",
}


ESTILO_LABEL_NORMAL_VERDE = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": COLOR_SECUNDARIO,
    "text_color": COLOR_BLANCO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3),     
}


ESTILO_LABEL_NORMAL_TRANSPARENTE = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": TRANSPARENTE,
    "text_color": COLOR_PRIMARIO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3),     
}


ESTILO_LABEL_TITULO = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": COLOR_PRIMARIO,
    "text_color": COLOR_BLANCO,
    "font": ESTILO_DE_LETRA_TITULO,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3), 
    "pady": (ALTURA_ESTANDAR_WIDGET/3),     
}


ESTILO_IMAGELABEL = {
    "corner_radius": 0,
    "fg_color": TRANSPARENTE,
    "text_color": COLOR_PRIMARIO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "text": "",
    "compound": "center",
    "state": "normal",
    "anchor": "center",
    "justify": "center"
}


ESTILO_PROGRESSBAR = {
    "height": (ALTURA_ESTANDAR_WIDGET/3),
    "border_width": 0,
    "corner_radius": 0,
    "fg_color": COLOR_SOMBRA,
    "border_color":COLOR_SECUNDARIO,
    "progress_color": COLOR_PRIMARIO,
    "orientation": "horizontal",
    "mode": "determinate",
}



# =========================================================
# VENTANA
# =========================================================
ventana = CTk()

ventana.title("Generador de Contraseñas")
ventana.geometry("600x600")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

# =========================================================
# FRAME PRINCIPAL
# =========================================================
frame_principal = CTkFrame(
    master=ventana,
    fg_color=COLOR_FONDO,
    corner_radius=0,
)

frame_principal.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10,
)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0,weight=1)

# =========================================================
# FRAME TÍTULO
# =========================================================
frame_titulo = CTkFrame(
    master=frame_principal,
    height=80,
    fg_color=COLOR_PRIMARIO,
    corner_radius=0,
)

frame_titulo.grid(
    row=0,
    column=0,
    sticky="ew",
)

frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(0,weight=1)
# =========================================================
# TÍTULO
# =========================================================
titulo = CTkLabel(
    master=frame_titulo,
    text="GENERADOR DE CONTRASEÑAS",
    **ESTILO_LABEL_TITULO,
)

titulo.grid(
    row=0,
    column=0,
    pady=20,
)

# =========================================================
# FRAME CONTENIDO
# =========================================================
frame_contenido = CTkFrame(
    master=frame_principal,
    fg_color=TRANSPARENTE,
    corner_radius=0,
)

frame_contenido.grid(
    row=1,
    column=0,
    padx=50,
    pady=20,
    sticky="ew",
)

frame_contenido.grid_columnconfigure(0, weight=1)
frame_contenido.grid_rowconfigure([0,1,2,3,4,5,6],weight=1)

# =========================================================
# FUNCIONES
# =========================================================
def generar_contrasena():
    longitud = int(slider_longitud.get())
    
    caracteres = ""
    contrasena = ""

    if var_minusculas.get():
        caracteres += string.ascii_lowercase
        contrasena += secrets.choice(string.ascii_lowercase)

    if var_mayusculas.get():
        caracteres += string.ascii_uppercase
        contrasena += secrets.choice(string.ascii_uppercase)

    if var_numeros.get():
        caracteres += string.digits
        contrasena += secrets.choice(string.digits)

    if var_simbolos.get():
        caracteres += string.punctuation
        contrasena += secrets.choice(string.punctuation)

    if not caracteres:
        entry_resultado.delete(0, "end")
        entry_resultado.insert(0,"Selecciona al menos una opción")
        return

    for i in range(longitud - len(contrasena)):
        contrasena += secrets.choice(caracteres)
        
    contrasena = "".join(random.sample(contrasena, len(contrasena)))
    
    entry_resultado.delete(0, "end")
    entry_resultado.insert(0, contrasena)


def copiar_portapapeles():

    ventana.clipboard_clear()
    ventana.clipboard_append(entry_resultado.get())

    label_estado.configure(
        text="Contraseña copiada al portapapeles"
    )


def actualizar_label_longitud(valor):

    label_longitud.configure(text=f"LONGITUD: {int(valor)}")

# =========================================================
# LABEL LONGITUD
# =========================================================
label_longitud = CTkLabel(
    frame_contenido,
    text="LONGITUD: 12",
    **ESTILO_LABEL_NORMAL_VERDE,
)

label_longitud.grid(
    row=0,
    column=0,
    sticky="ew",
)

# =========================================================
# SLIDER
# =========================================================
slider_longitud = CTkSlider(
    frame_contenido,
    from_=4,
    to=32, 
    command=actualizar_label_longitud,
    **ESTILO_SLIDER,
)

slider_longitud.set(12)

slider_longitud.grid(
    row=1,
    column=0,
    sticky="ew",
    pady=25,
)

frame_checkbox = CTkFrame(
    master=frame_contenido,
    fg_color=TRANSPARENTE,
    corner_radius=0,
)
frame_checkbox.grid(
    row=2,
    column=0,
    sticky="nsew",
)
frame_checkbox.grid_columnconfigure(0,weight=1)
frame_checkbox.grid_rowconfigure([0,1,2,3],weight=1)


# =========================================================
# VARIABLES
# =========================================================
var_minusculas = BooleanVar(value=True)
var_mayusculas = BooleanVar(value=True)
var_numeros = BooleanVar(value=True)
var_simbolos = BooleanVar(value=False)

# =========================================================
# CHECKBOXES
# =========================================================
check_minusculas = CTkCheckBox(
    frame_checkbox,
    text="INCLUIR MINÚSCULAS (a-z)",
    variable=var_minusculas,
    **ESTILO_CHECKBOX,
)

check_minusculas.grid(
    row=0,
    column=0,
    sticky="w",
    pady=5,
)

check_mayusculas = CTkCheckBox(
    frame_checkbox,
    text="INCLUIR MAYÚSCULAS (A-Z)",
    variable=var_mayusculas,
    **ESTILO_CHECKBOX,
)

check_mayusculas.grid(
    row=1,
    column=0,
    sticky="w",
    pady=5,
)

check_numeros = CTkCheckBox(
    frame_checkbox,
    text="INCLUIR NÚMEROS (0-9)",
    variable=var_numeros,
    **ESTILO_CHECKBOX,
)

check_numeros.grid(
    row=2,
    column=0,
    sticky="w",
    pady=5,
)

check_simbolos = CTkCheckBox(
    frame_checkbox,
    text="INCLUIR SÍMBOLOS (!@#...)",
    variable=var_simbolos,
    **ESTILO_CHECKBOX,
)

check_simbolos.grid(
    row=3,
    column=0,
    sticky="w",
    pady=5,
)

# =========================================================
# ENTRY RESULTADO
# =========================================================
entry_resultado = CTkEntry(
    frame_contenido,
    **ESTILO_ENTRY,
)

entry_resultado.grid(
    row=3,
    column=0,
    pady=30,
    sticky="ew",
)

# =========================================================
# BOTÓN GENERAR
# =========================================================
boton_generar = CTkButton(
    frame_contenido,
    text="GENERAR",
    command=generar_contrasena,
    **ESTILO_BOTON,
)

boton_generar.grid(
    row=4,
    column=0,
    sticky = "ew",
    pady=10,
)

# =========================================================
# BOTÓN COPIAR
# =========================================================
boton_copiar = CTkButton(
    frame_contenido,
    text="COPIAR AL PORTAPAPELES",
    command=copiar_portapapeles,
    **ESTILO_BOTON,
)

boton_copiar.grid(
    row=5,
    column=0,    
    sticky = "ew",
    pady=10,
)

# =========================================================
# LABEL ESTADO
# =========================================================
label_estado = CTkLabel(
    frame_contenido,
    text="",
    **ESTILO_LABEL_NORMAL_TRANSPARENTE,
)

label_estado.grid(
    row=6,
    column=0,
)

# =========================================================
# MAIN LOOP
# =========================================================
ventana.mainloop()