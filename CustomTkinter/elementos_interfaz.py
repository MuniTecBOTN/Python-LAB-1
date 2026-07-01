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
frame_contenedor = CTkFrame(
    master=ventana,
    fg_color=COLOR_BORDE,
)
frame_contenedor.grid(
    row=0,
    column=0,
    sticky = "nsew",
)

frame_contenedor.grid_rowconfigure([0,1,2,3],weight=1)
frame_contenedor.grid_columnconfigure([0,1,2],weight=1)


#   Botón - CTkButton
def funcion_boton_1():
    print(f"Has presionado el Botón 1")


boton_1 = CTkButton(
    master=frame_contenedor,
    width=80,
    height=30,
    corner_radius=0,
    text="Haz Click",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_1,
)

boton_1.grid(
    row=0,
    column=1,
)

#   Otra forma de posicionarlo, Relx= 0 es el borde izquierdo de la pantalla y 1 el borde derecho
"""boton_1.place(
    relx=0.5,
    rely=0.15,
    anchor="center",
)"""


#   Botones Agrupados - CTkSegmentedButton
def funcion_botones_agrupados(value):
    print(f"Has selecionado {value}, de los botones agrupados")


valor_botones_agrupados = StringVar(value=None)

botones_agrupados = CTkSegmentedButton(
    master=frame_contenedor,
    values=["Opción 1", "Opción 2", "Opción 3"],
    variable=valor_botones_agrupados,
    command=funcion_botones_agrupados,
    font=("Montserrat", 16),
)

botones_agrupados.grid(
    row=1,
    column=1,
)


#   CheckBox - CTkCheckBox
def funcion_checkbox():
    print(f"Has cambiado el valor del checkbox a {valor_checkbox.get()}")


valor_checkbox = BooleanVar(value=False)
texto_checkbox = StringVar(value="¿Aceptas los términos")
checkbox = CTkCheckBox(
    master=frame_contenedor,
    checkbox_width=40,
    checkbox_height=40,
    corner_radius=100,
    border_width=1,
    text="¿Acepta los términos?",
    textvariable=texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=valor_checkbox,
    command=funcion_checkbox,
    font=("Montserrat", 16),
)

checkbox.grid(
    row=0,
    column=0,
)


#   Radio Botones - CTkRadioButton
def funcion_grupo_1_radios():
    print(
        f"Has seleccionado la opción {valor_grupo_1_radios.get()} del grupo 1 de radiobuttons"
    )


valor_grupo_1_radios = IntVar(value=0)
radiobutton_1 = CTkRadioButton(
    master=frame_contenedor,
    text="Opción 1",
    command=funcion_grupo_1_radios,
    value=1,
    variable=valor_grupo_1_radios,
    font=("Montserrat", 16),
)
radiobutton_2 = CTkRadioButton(
    master=frame_contenedor,
    text="Opción 2",
    command=funcion_grupo_1_radios,
    value=2,
    variable=valor_grupo_1_radios,
    font=("Montserrat", 16),
)

radiobutton_1.grid(
    row=0,
    column=2,
    pady=150,
    sticky="n",
)
radiobutton_2.grid(
    row=0,
    column=2,
    pady=150,
    sticky="s",
)


#   Menu de opciones 1 - CTkOptionMenu
def funcion_menu_opciones(seleccion):
    print(f"Has seleccionado {seleccion} del menu de opciones")


lista_opciones = ["ATITLAN", "ACATENANGO", "TIKAL", "ROSTRO MAYA"]
valor_menu_opciones = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_contenedor,
    width=180,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_opciones,
    variable=valor_menu_opciones,
    command=funcion_menu_opciones,
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=1,
    column=0,
)


#   ComboBox - CTkComboBox
def funcion_combobox(seleccion):
    print(f"Has selecionado {seleccion} en el combobox")
    valor_combobox.get()


valor_combobox = StringVar(value="Selecione una Opción")
combobox = CTkComboBox(
    master=frame_contenedor,
    width=180,
    corner_radius=0,
    values=lista_opciones,
    variable=valor_combobox,
    command=funcion_combobox,
    font=("Montserrat", 16),
)

combobox.grid(
    row=1,
    column=2,
)


#   Campo de texto - CTkEntry
def al_presionar_enter(event):
    print(f"Ha ingresado '{campo_texto.get()}' en el campo de texto")


campo_texto = CTkEntry(
    master=frame_contenedor,
    width=180,
    corner_radius=0,
    placeholder_text="Escriba su nombre...",
    font=("Montserrat", 16),
)
campo_texto.bind("<Return>", al_presionar_enter)
campo_texto.grid(
    row=2,
    column=0,
)

#   Caja de texto - CTkTextBox
caja_texto = CTkTextbox(
    master=frame_contenedor,
    width=200,
    height=100,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_texto.grid(
    row=2,
    column=1,
)

#   Etiqueta - CTkLabel
etiqueta_1 = CTkLabel(
    master=frame_contenedor,
    fg_color="transparent",
    text="Esta es una etiqueta",
    font=("Montserrat", 16),
)
etiqueta_1.grid(
    row=2,
    column=2,
)


#   Slider - CTkSlider
def funcion_slider(value):
    print(f"Has configuardo el slider a {value} %")


valor_slider = IntVar(value=0)
slider = CTkSlider(
    master=frame_contenedor,
    from_=0,
    to=100,
    variable=valor_slider,
    number_of_steps=100,
    command=funcion_slider,
)
slider.grid(
    row=3,
    column=0,
)


#   Switch - CTkSwitch
def funcion_switch():
    print(f"Has cambiado el estado del switch a {valor_switch.get()}")


valor_switch = StringVar(value="off")
switch = CTkSwitch(
    master=frame_contenedor,
    text="Texto Switch",
    command=funcion_switch,
    variable=valor_switch,
    onvalue="on",
    offvalue="off",
    font=("Montserrat", 16),
)
switch.grid(
    row=3,
    column=1,
)

#   Barra Progreso - CTkProgressBar
barra_progreso = CTkProgressBar(
    master=frame_contenedor,
    orientation="horizontal",
)
barra_progreso.grid(
    row=3,
    column=2,
)
barra_progreso.start()


ventana.mainloop()