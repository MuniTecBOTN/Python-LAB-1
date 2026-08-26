from customtkinter import *

# =========================================================
# COLORES
# =========================================================
COLOR_FONDO = "#f0f2f5"
COLOR_AZUL = "#0053a1"
COLOR_AMARILLO = "#fdb827"
COLOR_BLANCO = "#ffffff"
COLOR_ROJO = "#ee4c4c"
COLOR_VERDE = "#2ce429"
TRANSPARENTE = "transparent"
ALTURA_ESTANDAR_CAMPO = 40
TAMAÑO_LETRA_NORMAL = 18

# =========================================================
# ESTILOS
# =========================================================
estilo_etiqueta_titulo = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", 28),
    "text_color": COLOR_BLANCO,
    "fg_color": TRANSPARENTE,
}

estilo_etiqueta_normal = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "text_color": COLOR_BLANCO,
    "fg_color": COLOR_AMARILLO,
}

estilo_campo = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "border_color": COLOR_BLANCO,
    "text_color": COLOR_AZUL,
    "justify": "center",
    "corner_radius": 0,
    "placeholder_text": "...",
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
}

estilo_lista = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "text_color": COLOR_AZUL,
    "button_color": COLOR_AMARILLO,
    "dropdown_fg_color": COLOR_AZUL,
    "dropdown_text_color": COLOR_BLANCO,
    "dropdown_font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "anchor": "center",
    "corner_radius": 0,
    "dynamic_resizing": False,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
}

estilo_boton = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_AZUL,
    "hover_color": COLOR_AMARILLO,
    "text_color": COLOR_BLANCO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL, "bold"),
    "corner_radius": 0,
}

estilo_boton_spinbox = {
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_AZUL,
    "hover_color": COLOR_AMARILLO,
    "text_color": COLOR_BLANCO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL, "bold"),
    "corner_radius": 0,
}

estilo_boton_segmentado = {
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "selected_color": COLOR_AMARILLO,
    "selected_hover_color": COLOR_AMARILLO,
    "unselected_color": COLOR_AZUL,
    "unselected_hover_color": COLOR_AMARILLO,
    "text_color": COLOR_BLANCO,
    "text_color_disabled": COLOR_BLANCO,
    "corner_radius": 0,
    "border_width": 2,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "dynamic_resizing": False,
}


def calcular_total():
    total = cantidad_boletos.get() * precio_boleto.get()
    total_en_boletos.set(total)


def decrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    if cantidad_actual > 0:
        cantidad_boletos.set(cantidad_actual - 1)
    calcular_total()


def incrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    cantidad_boletos.set(cantidad_actual + 1)
    calcular_total()


def pelicula_seleccionada(nombre_pelicula):
    horarios = peliculas.get(nombre_pelicula, [])
    campo_horario.configure(values=horarios)
    campo_horario.set("SELECCIONE UN HORARIO")
    calcular_total()


def calcular_precio_unitario(tipo_boleto):
    precio_boleto.set(boleto_precio.get(tipo_boleto, 0))
    calcular_total()


def click_boton_limpiar():
    campo_horario.configure(values=["SELECCIONE UN HORARIO"])
    campo_pelicula.set(value="SELECCIONE UNA PELÍCULA")
    opcion_seleccionada_menu_horario.set("SELECCIONE UN HORARIO")
    opcion_seleccionada_menu_pelicula.set("SELECCIONE UNA PELÍCULA")
    campo_tipo.set(None)
    cantidad_boletos.set(0)
    precio_boleto.set(0)
    total_en_boletos.set(0)


def marcar_error(widget, color_fondo=COLOR_BLANCO, color_texto=COLOR_AZUL):

    widget.configure(fg_color=COLOR_ROJO, text_color=COLOR_BLANCO)

    ventana.after(
        800, lambda: widget.configure(fg_color=color_fondo, text_color=color_texto)
    )


def validar_campos():

    valido = True

    # Validar película
    if opcion_seleccionada_menu_pelicula.get() == "SELECCIONE UNA PELÍCULA":
        marcar_error(campo_pelicula)
        valido = False

    # Validar horario
    if opcion_seleccionada_menu_horario.get() == "SELECCIONE UN HORARIO":
        marcar_error(campo_horario)
        valido = False

    # Validar tipo de boleto
    if campo_tipo.get() not in boleto_precio:
        marcar_error(campo_tipo, color_texto=COLOR_BLANCO)
        valido = False

    # Validar cantidad
    if cantidad_boletos.get() <= 0:
        marcar_error(campo_cantidad)
        valido = False

    return valido


peliculas = {
    "El Origen": ["13:30-16:00", "17:30-20:00", "21:30-00:00"],
    "Matrix": ["14:00-16:30", "18:00-20:30", "21:30-00:00"],
    "Interstellar": ["15:00-17:30", "18:30-21:00", "22:00-00:30"],
    "Michael Jackson: This Is It": ["14:30-17:00", "18:00-20:30", "21:30-00:00"],
    "Mario Bros.": ["13:00-15:30", "16:30-19:00", "20:00-22:30"],
    "El Conjuro": ["15:00-17:30", "18:00-20:30", "21:00-23:30"],
}

boleto_precio = {
    "NIÑO": 35,
    "NORMAL": 45,
    "VIP": 90,
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
ventana.geometry("800x580")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# =========================================================
# DECLARACIÓN DE FRAMES
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
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=8)
frame_principal.grid_rowconfigure(2, weight=1)

frame_superior = CTkFrame(
    master=frame_principal,
    height=80,
    fg_color=COLOR_AZUL,
    corner_radius=0,
)
frame_superior.grid(
    row=0,
    column=0,
    sticky="nsew",
)
frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)

frame_central = CTkFrame(
    master=frame_principal,
    fg_color=COLOR_FONDO,
    corner_radius=0,
)
frame_central.grid(
    row=1,
    column=0,
    sticky="nsew",
)
frame_central.grid_columnconfigure(0, weight=1)
frame_central.grid_columnconfigure(1, weight=1)
frame_central.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)


frame_inferior = CTkFrame(
    master=frame_principal,
    fg_color=TRANSPARENTE,
    corner_radius=0,
)
frame_inferior.grid(
    row=2,
    column=0,
    sticky="snew",
)

frame_inferior.grid_columnconfigure([0, 1], weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
# =========================================================
# ELEMENTOS FRAME SUPERIROR
# =========================================================
etiqueta_titulo = CTkLabel(
    master=frame_superior,
    text="🎬 CINE PYTHON",
    **estilo_etiqueta_titulo,
)

etiqueta_titulo.grid(
    row=0,
    column=0,
)


# =========================================================
# ELEMENTOS FRAME CENTRAL
# =========================================================
etiqueta_pelicula = CTkLabel(
    master=frame_central,
    text="PELÍCULA: ",
    **estilo_etiqueta_normal,
)

etiqueta_pelicula.grid(
    row=0,
    column=0,
    sticky="ew",
)


lista_peliculas = list(peliculas.keys())
opcion_seleccionada_menu_pelicula = StringVar(value="SELECCIONE UNA PELÍCULA")

campo_pelicula = CTkOptionMenu(
    master=frame_central,
    command=pelicula_seleccionada,
    values=lista_peliculas,
    variable=opcion_seleccionada_menu_pelicula,
    **estilo_lista,
)


campo_pelicula.grid(
    row=0,
    column=1,
    sticky="ew",
)
etiqueta_horario = CTkLabel(
    master=frame_central,
    text="HORARIO: ",
    **estilo_etiqueta_normal,
)

etiqueta_horario.grid(
    row=1,
    column=0,
    sticky="ew",
)


opcion_seleccionada_menu_horario = StringVar(value="SELECCIONE UN HORARIO")

campo_horario = CTkOptionMenu(
    master=frame_central,
    values=["SELECCIONE UN HORARIO"],
    variable=opcion_seleccionada_menu_horario,
    **estilo_lista,
)


campo_horario.grid(
    row=1,
    column=1,
    sticky="ew",
)

etiqueta_tipo = CTkLabel(
    master=frame_central,
    text="TIPO DE BOLETO: ",
    **estilo_etiqueta_normal,
)

etiqueta_tipo.grid(
    row=2,
    column=0,
    sticky="ew",
)


tipos_de_boletos = list(boleto_precio.keys())

campo_tipo = CTkSegmentedButton(
    master=frame_central,
    values=tipos_de_boletos,
    command=calcular_precio_unitario,
    **estilo_boton_segmentado,
)
campo_tipo.set("NORMAL")

campo_tipo.grid(
    row=2,
    column=1,
    sticky="ew",
)


ventana.after(
    100,
    lambda: [boton.configure(width=100) for boton in campo_tipo._buttons_dict.values()],
)


etiqueta_cantidad = CTkLabel(
    master=frame_central,
    text="CANTIDAD: ",
    **estilo_etiqueta_normal,
)

etiqueta_cantidad.grid(
    row=3,
    column=0,
    sticky="ew",
)
# =========================================================
# SPINBOX
# =========================================================
frame_spinbox = CTkFrame(
    master=frame_central,
    height=ALTURA_ESTANDAR_CAMPO,
    fg_color=TRANSPARENTE,
    corner_radius=0,
)
frame_spinbox.grid(
    row=3,
    column=1,
    sticky="ew",
    padx=2,
)
frame_spinbox.grid_columnconfigure([0, 1, 2], weight=1)
frame_spinbox.grid_rowconfigure(0, weight=1)

boton_decrementar = CTkButton(
    master=frame_spinbox,
    command=decrementar_boletos,
    text="-",
    **estilo_boton_spinbox,
)
boton_decrementar.grid(
    row=0,
    column=0,
    sticky="news",
    padx=1,
)

cantidad_boletos = IntVar(value=0)
campo_cantidad = CTkEntry(
    master=frame_spinbox,
    state="readonly",
    height=ALTURA_ESTANDAR_CAMPO,
    fg_color=COLOR_BLANCO,
    border_color=COLOR_BLANCO,
    text_color=COLOR_AZUL,
    justify="center",
    corner_radius=0,
    textvariable=cantidad_boletos,
    font=("Montserrat", TAMAÑO_LETRA_NORMAL),
)
campo_cantidad.grid(
    row=0,
    column=1,
    sticky="news",
    padx=1,
)
boton_incrementar = CTkButton(
    master=frame_spinbox,
    command=incrementar_boletos,
    text="+",
    **estilo_boton_spinbox,
)
boton_incrementar.grid(
    row=0,
    column=2,
    sticky="news",
    padx=1,
)

etiqueta_precio = CTkLabel(
    master=frame_central,
    text="PRECIO UNITARIO: ",
    **estilo_etiqueta_normal,
)

etiqueta_precio.grid(
    row=4,
    column=0,
    sticky="ew",
)
precio_boleto = IntVar(value=0)
precio_boleto.set(boleto_precio.get("NORMAL", 0))

campo_precio = CTkEntry(
    master=frame_central,
    state="readonly",
    textvariable=precio_boleto,
    **estilo_campo,
)
campo_precio.grid(
    row=4,
    column=1,
    sticky="ew",
)

etiqueta_total = CTkLabel(
    master=frame_central,
    text="TOTAL: ",
    **estilo_etiqueta_normal,
)

etiqueta_total.grid(
    row=5,
    column=0,
    sticky="ew",
)
total_en_boletos = IntVar(value=0)
campo_total = CTkEntry(
    master=frame_central,
    state="readonly",
    textvariable=total_en_boletos,
    **estilo_campo,
)
campo_total.grid(
    row=5,
    column=1,
    sticky="ew",
)

# =========================================================
# ELEMENTOS FRAME INFERIOR
# =========================================================
boton_calcular = CTkButton(
    master=frame_inferior,
    text="CALCULAR",
    command=validar_campos,
    **estilo_boton,
)
boton_calcular.grid(
    row=0,
    column=0,
    sticky="snew",
)
boton_limpiar = CTkButton(
    master=frame_inferior,
    text="LIMPIAR",
    command=click_boton_limpiar,
    **estilo_boton,
)
boton_limpiar.grid(
    row=0,
    column=1,
    sticky="snew",
)

# =========================================================
# MAIN LOOP
# =========================================================
ventana.mainloop()
