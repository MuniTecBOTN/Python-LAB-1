COLOR_PRIMARIO = "#161D35"
COLOR_SECUNDARIO = "#F59E0B"
COLOR_VERDE = "#10B981"
COLOR_ROJO = "#EF4444"
COLOR_BLANCO = "#FFFFFF"
COLOR_FONDO = "#F8FAFC"
COLOR_BORDE = "#E2E8F0"
TRANSPARENTE = "transparent"

ALTURA_ESTANDAR_CAMPO = 50
TAMAÑO_LETRA_ETIQUETA = 18
TAMAÑO_LETRA_TITULO = 28

estilo_etiqueta_titulo = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_TITULO),
    "text_color": COLOR_BLANCO,
    "fg_color": TRANSPARENTE,
}

estilo_etiqueta_normal = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_ETIQUETA),
    "text_color": COLOR_BLANCO,
    "fg_color": COLOR_SECUNDARIO,
}

estilo_etiqueta_normal_blanco = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_ETIQUETA),
    "text_color": COLOR_PRIMARIO,
    "fg_color": COLOR_BLANCO,
}

estilo_etiqueta_normal_azul = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_ETIQUETA),
    "text_color": COLOR_BLANCO,
    "fg_color": COLOR_PRIMARIO,
}

estilo_campo = {
    "width": 400,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "border_color": COLOR_BLANCO,
    "text_color": COLOR_PRIMARIO,
    "justify": "center",
    "corner_radius": 0,
    "placeholder_text": "...",
    "font": ("Montserrat", TAMAÑO_LETRA_ETIQUETA),
}

estilo_lista = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "text_color": COLOR_PRIMARIO,
    "button_color": COLOR_SECUNDARIO,
    "dropdown_fg_color": COLOR_PRIMARIO,
    "dropdown_text_color": COLOR_BLANCO,
    "dropdown_font": ("Montserrat", TAMAÑO_LETRA_ETIQUETA),
    "anchor": "center",
    "corner_radius": 0,
    "dynamic_resizing": False,
    "font": ("Montserrat", TAMAÑO_LETRA_ETIQUETA),
}

estilo_boton = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_PRIMARIO,
    "hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_BLANCO,
    "font": ("Montserrat", TAMAÑO_LETRA_ETIQUETA, "bold"),
    "corner_radius": 0,
}