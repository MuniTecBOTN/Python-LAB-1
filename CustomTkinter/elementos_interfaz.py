from customtkinter import *

set_default_color_theme("green")

ventana = CTk()
ventana.title("Elementos de una GUI")
ventana.geometry("800x600")

#   Configuramos 3 columnas
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

#   También configuramos 3 filas
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(3, weight=1)


#   Botón - CTkButton
def funcion_boton_1():
    print(f"Has presionado el Botón 1")


boton_1 = CTkButton(
    master=ventana,
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
    master=ventana,
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
    master=ventana,
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
    master=ventana,
    text="Opción 1",
    command=funcion_grupo_1_radios,
    value=1,
    variable=valor_grupo_1_radios,
    font=("Montserrat", 16),
)
radiobutton_2 = CTkRadioButton(
    master=ventana,
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
def funcion_menu_opciones(choice):
    print(f"Has seleccionado {choice} del menu de opciones")


lista_opciones = ["ATITLAN", "ACATENANGO", "TIKAL","ROSTRO MAYA"]
valor_menu_opciones = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=ventana,
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
def funcion_combobox(choice):
    print(f"Has selecionado {choice} en el combobox")
    valor_combobox.get()


valor_combobox = StringVar(value="Selecione una Opción")
combobox = CTkComboBox(
    master=ventana,
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
    master=ventana,
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
    master=ventana,
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
    master=ventana,
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
    master=ventana,
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
    master=ventana,
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
    master=ventana,
    orientation="horizontal",
)
barra_progreso.grid(
    row=3,
    column=2,
)
barra_progreso.start()
ventana.mainloop()