from customtkinter import *

# =========================================================
# COLORES
# =========================================================
COLOR_FONDO = "#f0f2f5"
COLOR_AZUL = "#0053a1"
COLOR_AMARILLO = "#fdb827"
COLOR_BLANCO = "#ffffff"
COLOR_ROJO = "#ea4f4f"
COLOR_VERDE = "#2ce429"
TRANSPARENTE = "transparent"
ALTURA_ESTANDAR_CAMPO = 35
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


def decrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    if cantidad_actual > 0:
        cantidad_boletos.set(cantidad_actual - 1)


def incrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    cantidad_boletos.set(cantidad_actual + 1)


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

campo_pelicula = CTkOptionMenu(
    master=frame_central,
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

campo_horario = CTkOptionMenu(
    master=frame_central,
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

campo_tipo = CTkSegmentedButton(
    master=frame_central,
    values=["NIÑO", "NORMAL", "VIP"],
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

campo_precio = CTkEntry(
    master=frame_central,
    state="readonly",
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

campo_total = CTkEntry(
    master=frame_central,
    state="readonly",
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
