from customtkinter import *

def decrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    if cantidad_actual > 0:
        cantidad_boletos.set(cantidad_actual - 1)
    

def incrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    cantidad_boletos.set(cantidad_actual + 1)
    
productos = {
    "Xiaomi Redmi 15 C": {"precio": 15000, "stock": 100},
    "Samsung Galaxy S25 ULTRA": {"precio": 20000, "stock": 50},
    "Apple iPhone 15 Pro Max": {"precio": 15000, "stock": 75},
}
    
# =========================================================
# COLORES
# =========================================================
COLOR_FONDO = "#f0f2f5"
COLOR_AZUL = "#143a81"
COLOR_AMARILLO = "#ffcf03"
COLOR_BLANCO = "#ffffff"
COLOR_ROJO = "#ee4c4c"
COLOR_VERDE = "#2ce429"
TRANSPARENTE = "transparent"
ALTURA_ESTANDAR_CAMPO = 50
TAMAÑO_LETRA_NORMAL = 18
TAMAÑO_LETRA_TITULO = 28 
# =========================================================
# ESTILOS
# =========================================================
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

# =========================================================
# FUNCIONES
# =========================================================
def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    etiqueta_titulo_ventana.configure(text=nombre_pestaña)


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
ventana.geometry("1600x920")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# =========================================================
# DECLARACIÓN DE FRAMES
# =========================================================

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

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=10)
frame_principal.grid_propagate(False)


# =========================================================
# SIDEBAR
# =========================================================

frame_sidebar = CTkFrame(
    master=frame_principal,
    fg_color=COLOR_AZUL,
    corner_radius=0
)
frame_sidebar.grid(
    row=0,
    column=0,
    sticky="wnse",
)
frame_sidebar.rowconfigure(0,weight=1)
frame_sidebar.rowconfigure(1,weight=8)
frame_sidebar.grid_columnconfigure(0, weight=1)

frame_logo = CTkFrame(
    master=frame_sidebar,
    height=80,
    fg_color=COLOR_AZUL,
    corner_radius=0
)

frame_logo.grid(
    row=0,
    column=0,
    sticky="news",
)
frame_logo.rowconfigure(0,weight=1)
frame_logo.columnconfigure(0,weight=1)

etiqueta_logo = CTkLabel(
    master=frame_logo,
    text="MENU",
    **estilo_etiqueta_titulo,
)

etiqueta_logo.grid(
    row=0,
    column=0,
    sticky="nsew",
)
# =========================================================
# BOTONES DE NAVEGACIÓN
# =========================================================
frame_botones_navegacion= CTkFrame(
    master=frame_sidebar,
    fg_color="transparent",
    corner_radius=0
)
frame_botones_navegacion.grid(
    row=1,
    column=0,
    sticky="nsew",
    pady = 35
)

frame_botones_navegacion.rowconfigure([0,1,2,3,4,5,6],weight=1)
frame_botones_navegacion.columnconfigure(0,weight=1)

inicio_boton = CTkButton(
    master=frame_botones_navegacion,
    text="INICIO",
    command=lambda: ir_a_pestaña("INICIO"),
    **estilo_boton,
)
inicio_boton.grid(
    row=0,
    column=0,
    sticky="ew",
)

boton_ventas = CTkButton(
    master=frame_botones_navegacion,
    text="VENTAS",
    command=lambda: ir_a_pestaña("VENTAS"),
    **estilo_boton,
)
boton_ventas.grid(
    row=1,
    column=0,
    sticky="ew",
)

boton_productos = CTkButton(
    master=frame_botones_navegacion,
    text="PRODUCTOS",
    command=lambda: ir_a_pestaña("PRODUCTOS"),
    **estilo_boton,
)
boton_productos.grid(
    row=2,
    column=0,
    sticky="ew",
)

boton_inventario = CTkButton(
    master=frame_botones_navegacion,
    text="INVENTARIO",
    command=lambda: ir_a_pestaña("INVENTARIO"),
    **estilo_boton,
)
boton_inventario.grid(
    row=3,
    column=0,
    sticky="ew",
)

boton_clientes = CTkButton(
    master=frame_botones_navegacion,
    text="CLIENTES",
    command=lambda: ir_a_pestaña("CLIENTES"),
    **estilo_boton,
)
boton_clientes.grid(
    row=4,
    column=0,
    sticky="ew",
)

boton_reportes = CTkButton(
    master=frame_botones_navegacion,
    text="REPORTES",
    command=lambda: ir_a_pestaña("REPORTES"),
    **estilo_boton,
)
boton_reportes.grid(
    row=5,
    column=0,
    sticky="ew",
)

boton_salir = CTkButton(
    master=frame_botones_navegacion,
    text="SALIR",
    command=ventana.destroy,
    **estilo_boton,
)
boton_salir.grid(
    row=6,
    column=0,
    sticky="ew",
)
# =========================================================
# TABVIEW
# =========================================================

frame_tabview = CTkFrame(
    master=frame_principal,
    fg_color=COLOR_FONDO,
    corner_radius=0
)

frame_tabview.grid(
    row=0,
    column=1,
    sticky="nsew",
)
frame_tabview.rowconfigure(0,weight=1)
frame_tabview.rowconfigure(1,weight=8,minsize=620)
frame_tabview.columnconfigure(0,weight=1)
frame_tabview.grid_propagate(False)

frame_titulo = CTkFrame(
    master=frame_tabview,
    height=80,
    fg_color=COLOR_AZUL,
    corner_radius=0
)

frame_titulo.grid(
    row=0,
    column=0,
    sticky="news",
)

frame_titulo.rowconfigure(0,weight=1)
frame_titulo.columnconfigure(0,weight=1)

etiqueta_titulo_ventana = CTkLabel(
        master=frame_titulo,
        text="INICIO",
        **estilo_etiqueta_titulo,
    )
etiqueta_titulo_ventana.grid(
    row=0,
    column=0,
    sticky="nsew",
)
# =========================================================
# PESTAÑAS DEL TABVIEW
# =========================================================
pestañas = CTkTabview(
    master=frame_tabview,
    corner_radius=0,
    fg_color=COLOR_FONDO,
    segmented_button_fg_color=COLOR_AZUL,
    segmented_button_selected_color=COLOR_VERDE,
    segmented_button_selected_hover_color=COLOR_VERDE,
    segmented_button_unselected_color = COLOR_AZUL,	
    segmented_button_unselected_hover_color = COLOR_VERDE,
    text_color=COLOR_BLANCO
)

pestañas.grid(
    row=1,
    column=0,
    sticky="nsew",
)
# =========================================================
# PESTAÑAS
# =========================================================
tab_inicio = pestañas.add("INICIO")
tab_ventas = pestañas.add("VENTAS")
tab_productos = pestañas.add("PRODUCTOS")
tab_inventario = pestañas.add("INVENTARIO")
tab_clientes = pestañas.add("CLIENTES")
tab_reportes = pestañas.add("REPORTES")

tab_inicio.configure(fg_color=COLOR_BLANCO)
tab_inicio.grid_columnconfigure(0,weight=1)
tab_inicio.grid_rowconfigure(0,weight=1)

tab_productos.configure(fg_color=COLOR_BLANCO)
tab_productos.grid_columnconfigure(0,weight=1)
tab_productos.grid_rowconfigure(0,weight=1)

tab_inventario.configure(fg_color=COLOR_BLANCO)
tab_inventario.grid_columnconfigure(0,weight=1)
tab_inventario.grid_rowconfigure(0,weight=1)

tab_clientes.configure(fg_color=COLOR_BLANCO)
tab_clientes.grid_columnconfigure(0,weight=1)
tab_clientes.grid_rowconfigure(0,weight=1)

tab_reportes.configure(fg_color=COLOR_BLANCO)
tab_reportes.grid_columnconfigure(0,weight=1)
tab_reportes.grid_rowconfigure(0,weight=1)

pestañas._segmented_button.grid_forget()

# =========================================================
# TAB VENTAS
# =========================================================
tab_ventas.configure(fg_color=COLOR_BLANCO)
tab_ventas.grid_columnconfigure(0,weight=1)
tab_ventas.grid_rowconfigure([0,1],weight=1)

frame_producto = CTkFrame(
    master=tab_ventas,
    fg_color=COLOR_FONDO,
    corner_radius=0
)

frame_producto.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=20,
    pady=20
)

frame_producto.grid_columnconfigure(0,weight=2)
frame_producto.grid_columnconfigure(1,weight=4)
frame_producto.grid_columnconfigure(2,weight=1)
frame_producto.grid_rowconfigure([0,1],weight=1)

etiqueta_producto = CTkLabel(
    master=frame_producto,
    text="ITEM:",
    **estilo_etiqueta_normal,
)

etiqueta_producto.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=10,
    pady=10
)   

lista_productos = list(productos.keys())
opcion_seleccionada_menu_producto = StringVar(value="SELECCIONE UN PRODUCTO")

campo_producto = CTkOptionMenu(
    master=frame_producto,
    #command=producto_seleccionado,
    values=lista_productos,
    variable=opcion_seleccionada_menu_producto,
    **estilo_lista,
)
campo_producto.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=10,
    pady=10,
    columnspan=2
)

etiqueta_cantidad = CTkLabel(
    master=frame_producto,
    text="CANTIDAD:",
    **estilo_etiqueta_normal,
)
etiqueta_cantidad.grid( 
    row=1,
    column=0,
    sticky="ew",
    padx=10,
    pady=10
)

# =========================================================
# SPINBOX
# =========================================================
frame_spinbox = CTkFrame(
    master=frame_producto,
    height=ALTURA_ESTANDAR_CAMPO,
    fg_color=TRANSPARENTE,
    corner_radius=0,
)
frame_spinbox.grid(
    row=1,
    column=1,
    sticky="ew",
    padx=10,
    pady=10,
    columnspan=2,
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

boton_agregar = CTkButton(
    master=frame_producto,
    text="AGREGAR",
    **estilo_boton,
) 
boton_agregar.grid(
    row=2,
    column=2,
    sticky="ew",
    padx=10,
    pady=10
)   

frame_escroleable = CTkScrollableFrame(
    master=tab_ventas,
    fg_color=COLOR_FONDO,
    corner_radius=0,
    scrollbar_button_color=COLOR_AZUL,
    scrollbar_button_hover_color=COLOR_AZUL,
)   
frame_escroleable.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=20,
    pady=20
)

# =========================================================
# MAIN LOOP
# =========================================================
ventana.mainloop()
