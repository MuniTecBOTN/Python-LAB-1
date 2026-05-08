from customtkinter import *

# =========================================================
# CONFIGURACIÓN GLOBAL
# =========================================================
set_appearance_mode("light")
set_default_color_theme("dark-blue")

# =========================================================
# APP PRINCIPAL
# =========================================================
app = CTk()

app.title("Sistema de Registro")
app.geometry("1000x700")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# =========================================================
# COLORES
# =========================================================
COLOR_FONDO = "#e3e5f3"
COLOR_AZUL = "#2a00ac"
COLOR_VERDE = "#81dc00"
COLOR_BLANCO = "#ffffff"

# =========================================================
# MENÚ LATERAL
# =========================================================
menu_lateral = CTkFrame(
    app,
    width=200,
    fg_color=COLOR_AZUL,
    corner_radius=0
)

menu_lateral.grid(
    row=0,
    column=0,
    sticky="ns"
)

menu_lateral.grid_columnconfigure(0, weight=1)

# =========================================================
# ÁREA PRINCIPAL
# =========================================================
area_principal = CTkFrame(
    master=app,
    fg_color=COLOR_FONDO,
    corner_radius=0
)

area_principal.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=10,
    pady=10
)

area_principal.grid_rowconfigure(1, weight=1)
area_principal.grid_columnconfigure(0, weight=1)

# =========================================================
# LABEL MENÚ
# =========================================================
etiqueta_menu = CTkLabel(
    menu_lateral,
    text="MENÚ",
    font=("Montserrat", 22, "bold"),
    text_color=COLOR_BLANCO
)

etiqueta_menu.grid(
    row=0,
    column=0,
    pady=30
)

# =========================================================
# FUNCIONES MENÚ
# =========================================================
def funcion_boton_ir_registrar():
    pestañas.set("Formulario")


def funcion_boton_ver_registro():
    pestañas.set("Registro")


def funcion_boton_acerca_de():
    etiqueta_informacion.configure(
        text="Sistema desarrollado con CustomTkinter",
        text_color=COLOR_AZUL
    )

# =========================================================
# ESTILO BOTONES
# =========================================================
estilo_botones = {
    "width": 150,
    "height": 35,
    "corner_radius": 0,
    "fg_color": COLOR_BLANCO,
    "hover_color": COLOR_VERDE,
    "text_color": COLOR_AZUL,
    "font": ("Montserrat", 16, "bold"),
    "border_width": 0
}

# =========================================================
# BOTONES MENÚ
# =========================================================
boton_ir_registrar = CTkButton(
    menu_lateral,
    text="Agregar Usuario",
    command=funcion_boton_ir_registrar,
    **estilo_botones
)

boton_ir_registrar.grid(
    row=1,
    column=0,
    padx=20,
    pady=10
)

boton_ver_registro = CTkButton(
    menu_lateral,
    text="Ver Registro",
    command=funcion_boton_ver_registro,
    **estilo_botones
)

boton_ver_registro.grid(
    row=2,
    column=0,
    padx=20,
    pady=10
)

boton_acerca_de = CTkButton(
    menu_lateral,
    text="Acerca de",
    command=funcion_boton_acerca_de,
    **estilo_botones
)

boton_acerca_de.grid(
    row=3,
    column=0,
    padx=20,
    pady=10
)

# =========================================================
# TABVIEW
# =========================================================
pestañas = CTkTabview(
    master=area_principal,
    corner_radius=0,
    fg_color=COLOR_FONDO,
    segmented_button_fg_color=COLOR_BLANCO,
    segmented_button_selected_color=COLOR_AZUL,
    segmented_button_selected_hover_color=COLOR_VERDE,
    text_color=COLOR_AZUL
)

pestañas.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10
)

# =========================================================
# PESTAÑAS
# =========================================================
formulario = pestañas.add("Formulario")
registro = pestañas.add("Registro")

formulario.configure(fg_color=COLOR_FONDO)
registro.configure(fg_color=COLOR_FONDO)

# =========================================================
# CONFIGURACIÓN FORMULARIO
# =========================================================
formulario.grid_columnconfigure(0, weight=1)
formulario.grid_rowconfigure(0, weight=1)

# =========================================================
# FRAME PRINCIPAL
# =========================================================
frame_principal = CTkFrame(
    master=formulario,
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

# =========================================================
# FRAME TÍTULO
# =========================================================
frame_titulo = CTkFrame(
    master=frame_principal,
    height=80,
    fg_color=COLOR_AZUL,
    corner_radius=0
)

frame_titulo.grid(
    row=0,
    column=0,
    sticky="ew"
)

frame_titulo.grid_columnconfigure(0, weight=1)

# =========================================================
# TÍTULO
# =========================================================
etiqueta_titulo = CTkLabel(
    master=frame_titulo,
    height=80,
    text="REGISTRO DE USUARIO",
    font=("Montserrat", 20, "bold"),
    text_color=COLOR_BLANCO,
    fg_color="transparent"
)

etiqueta_titulo.grid(
    row=0,
    column=0,
    sticky="nsew"
)

# =========================================================
# FRAME DATOS
# =========================================================
frame_datos = CTkFrame(
    master=frame_principal,
    width=500,
    height=450,
    fg_color="transparent",
    corner_radius=0
)

frame_datos.grid(
    row=1,
    column=0,
    sticky="ns",
    padx=10,
    pady=10
)

frame_datos.grid_propagate(False)

frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_columnconfigure(1, weight=1)

for i in range(7):
    frame_datos.grid_rowconfigure(i, weight=1, minsize=50)

# =========================================================
# FRAME INFERIOR
# =========================================================
frame_inferior = CTkFrame(
    master=frame_principal,
    width=420,
    height=80,
    fg_color="transparent",
    corner_radius=0
)

frame_inferior.grid(
    row=2,
    column=0,
    sticky="s"
)

frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
frame_inferior.grid_propagate(False)

# =========================================================
# FUNCIONES
# =========================================================
def capturar_datos():

    nombre = campo_nombre.get().strip().lower()
    correo = campo_correo.get().strip().lower()
    edad = campo_edad.get().strip()

    pais = pais_seleccionado.get().strip()
    profesion = profesion_seleccionada.get().strip()
    genero = genero_seleccionado.get()

    if (
        not nombre
        or not correo
        or not edad
        or pais == "SELECCIONA"
        or profesion == "SELECCIONA"
        or genero == 0
    ):

        etiqueta_informacion.configure(
            text="Por favor, completa todos los campos",
            text_color="red"
        )

        etiqueta_informacion.after(
            2000,
            lambda: etiqueta_informacion.configure(text="")
        )

        return

    if not nombre.replace(" ", "").isalpha():

        etiqueta_informacion.configure(
            text="El nombre no puede contener números",
            text_color="red"
        )

        return

    if len(nombre) < 3:

        etiqueta_informacion.configure(
            text="El nombre debe tener al menos 3 caracteres",
            text_color="red"
        )

        return

    if not edad.isdigit():

        etiqueta_informacion.configure(
            text="La edad debe ser un número",
            text_color="red"
        )

        return

    if int(edad) < 1 or int(edad) > 99:

        etiqueta_informacion.configure(
            text="Edad inválida",
            text_color="red"
        )

        return

    extensiones_validas = (
        "@gmail.com",
        "@hotmail.com",
        "@yahoo.com",
        "@outlook.com"
    )

    if not correo.endswith(extensiones_validas):

        etiqueta_informacion.configure(
            text="Ingrese un correo válido",
            text_color="red"
        )

        return

    etiqueta_informacion.configure(
        text="Usuario registrado correctamente",
        text_color=COLOR_AZUL
    )


def limpiar():

    campo_nombre.delete(0, "end")
    campo_correo.delete(0, "end")
    campo_edad.delete(0, "end")

    pais_seleccionado.set("SELECCIONA")
    profesion_seleccionada.set("SELECCIONA")
    genero_seleccionado.set(0)

    etiqueta_informacion.configure(text="")

# =========================================================
# LABELS
# =========================================================
labels = [
    "NOMBRE",
    "CORREO",
    "EDAD",
    "PAÍS",
    "PROFESIÓN",
    "GÉNERO"
]

for i, texto in enumerate(labels):

    label = CTkLabel(
        master=frame_datos,
        width=120,
        height=30,
        text=texto,
        font=("Montserrat", 16),
        text_color=COLOR_BLANCO,
        fg_color=COLOR_VERDE,
        corner_radius=0
    )

    label.grid(
        row=i,
        column=0,
        sticky="e",
        padx=10
    )

# =========================================================
# ESTILO ENTRADAS
# =========================================================
estilo_entry = {
    "width": 200,
    "height": 30,
    "border_color": COLOR_FONDO,
    "text_color": COLOR_AZUL,
    "justify": "center",
    "corner_radius": 0,
    "placeholder_text": "...",
    "font": ("Montserrat", 16)
}

# =========================================================
# ENTRADAS
# =========================================================
campo_nombre = CTkEntry(
    frame_datos,
    **estilo_entry
)

campo_nombre.grid(
    row=0,
    column=1,
    sticky="w"
)

campo_correo = CTkEntry(
    frame_datos,
    **estilo_entry
)

campo_correo.grid(
    row=1,
    column=1,
    sticky="w"
)

campo_edad = CTkEntry(
    frame_datos,
    **estilo_entry
)

campo_edad.grid(
    row=2,
    column=1,
    sticky="w"
)

# =========================================================
# OPTION MENUS
# =========================================================
lista_paises = [
    "GUATEMALA",
    "MEXICO",
    "COLOMBIA",
    "SALVADOR",
    "COSTA RICA",
    "PANAMA"
]

pais_seleccionado = StringVar(value="SELECCIONA")

estilo_optionmenu = {
    "width": 200,
    "height": 30,
    "fg_color": COLOR_BLANCO,
    "text_color": COLOR_AZUL,
    "button_color": COLOR_VERDE,
    "dropdown_fg_color": COLOR_AZUL,
    "dropdown_text_color": COLOR_BLANCO,
    "anchor": "center",
    "corner_radius": 0,
    "dynamic_resizing": False,
    "font": ("Montserrat", 16)
}

menu_pais = CTkOptionMenu(
    frame_datos,
    values=lista_paises,
    variable=pais_seleccionado,
    **estilo_optionmenu
)

menu_pais.grid(
    row=3,
    column=1,
    sticky="w"
)

lista_profesiones = [
    "INGENIERO",
    "DOCTOR",
    "ABOGADO",
    "ARTISTA",
    "TECNICO",
    "PROGRAMADOR"
]

profesion_seleccionada = StringVar(value="SELECCIONA")

menu_profesion = CTkOptionMenu(
    frame_datos,
    values=lista_profesiones,
    variable=profesion_seleccionada,
    **estilo_optionmenu
)

menu_profesion.grid(
    row=4,
    column=1,
    sticky="w"
)

# =========================================================
# RADIO BUTTONS
# =========================================================
frame_radios = CTkFrame(
    frame_datos,
    fg_color="transparent",
    corner_radius=0
)

frame_radios.grid(
    row=5,
    column=1,
    sticky="w"
)

frame_radios.grid_columnconfigure(0, weight=1)

for i in range(3):
    frame_radios.grid_rowconfigure(i, weight=1)

genero_seleccionado = IntVar(value=0)

estilo_radio = {
    "font": ("Montserrat", 16),
    "text_color": COLOR_AZUL,
    "border_color": COLOR_AZUL,
    "fg_color": COLOR_VERDE,
    "hover_color": COLOR_VERDE
}

radio_femenino = CTkRadioButton(
    frame_radios,
    text="FEMENINO",
    value=1,
    variable=genero_seleccionado,
    **estilo_radio
)

radio_femenino.grid(
    row=0,
    column=0,
    sticky="w",
    padx=10,
    pady=2
)

radio_masculino = CTkRadioButton(
    frame_radios,
    text="MASCULINO",
    value=2,
    variable=genero_seleccionado,
    **estilo_radio
)

radio_masculino.grid(
    row=1,
    column=0,
    sticky="w",
    padx=10,
    pady=2
)

radio_otro = CTkRadioButton(
    frame_radios,
    text="OTRO",
    value=3,
    variable=genero_seleccionado,
    **estilo_radio
)

radio_otro.grid(
    row=2,
    column=0,
    sticky="w",
    padx=10,
    pady=2
)

# =========================================================
# BOTONES FORMULARIO
# =========================================================
boton_enviar = CTkButton(
    frame_datos,
    width=120,
    height=30,
    text="ENVIAR",
    fg_color=COLOR_AZUL,
    hover_color=COLOR_VERDE,
    text_color=COLOR_BLANCO,
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    command=capturar_datos
)

boton_enviar.grid(
    row=6,
    column=0,
    sticky="w"
)

boton_limpiar = CTkButton(
    frame_datos,
    width=120,
    height=30,
    text="LIMPIAR",
    fg_color=COLOR_AZUL,
    hover_color=COLOR_VERDE,
    text_color=COLOR_BLANCO,
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    command=limpiar
)

boton_limpiar.grid(
    row=6,
    column=1,
    sticky="e"
)

# =========================================================
# LABEL INFORMACIÓN
# =========================================================
etiqueta_informacion = CTkLabel(
    master=frame_inferior,
    width=300,
    height=80,
    text="",
    font=("Montserrat", 12, "bold"),
    text_color="#223ac2",
    fg_color="transparent"
)

etiqueta_informacion.grid(
    row=0,
    column=0,
    sticky="nsew"
)

# =========================================================
# PESTAÑA REGISTRO
# =========================================================
registro.grid_columnconfigure(0, weight=1)

checkbox = CTkCheckBox(
    registro,
    text="Opción A",
    corner_radius=0
)

checkbox.grid(
    row=0,
    column=0,
    pady=20
)

slider = CTkSlider(
    registro,
    corner_radius=0,
    button_corner_radius=0
)

slider.grid(
    row=1,
    column=0,
    padx=40,
    pady=20,
    sticky="ew"
)

combobox = CTkComboBox(
    registro,
    values=["1", "2", "3"],
    corner_radius=0
)

combobox.grid(
    row=2,
    column=0,
    pady=20
)

# =========================================================
# MAIN LOOP
# =========================================================
app.mainloop()