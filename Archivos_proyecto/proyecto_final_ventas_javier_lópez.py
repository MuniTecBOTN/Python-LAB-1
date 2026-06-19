from customtkinter import *
from PIL import Image

set_default_color_theme("dark-blue")

#=================================================
#COLORES
#=================================================

color_fondo = "#f0f2f5"
color_azul = "#0053a1"
color_amarillo = "#fdb827"
color_blanco = "#ffffff"
color_rojo = "#ea4f4f"
color_verde = "#2ce429"
transparente = "transparent"

altura_estandar_campo = 35

tamaño_letra_normal = 18

# =========================================================
# CARGAR IMAGEN
# =========================================================

ruta_script = os.path.dirname(os.path.abspath(__file__))



#=================================================
# FUNCIONES
#=================================================

def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    etiqueta_titulo.configure(text=nombre_pestaña)
    
    
def decrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    if cantidad_actual > 0:
        cantidad_boletos.set(cantidad_actual - 1)
    

def incrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    cantidad_boletos.set(cantidad_actual + 1)
    

 

# =========================================================
# ESTILOS
# =========================================================
estilo_etiqueta_titulo = {
    "width": 120,
    "height": altura_estandar_campo,
    "font": ("Montserrat", 28),
    "text_color": color_blanco,
    "fg_color": color_azul,
}

estilo_etiqueta_normal = {
    "width": 120,
    "height": altura_estandar_campo,
    "font": ("Montserrat", tamaño_letra_normal),
    "text_color": color_blanco,
    "fg_color": color_amarillo,
}
estilo_etiqueta_normal_scr = {
    "height": altura_estandar_campo,
    "font": ("Montserrat", tamaño_letra_normal),
    "text_color": color_blanco,
    "fg_color": color_amarillo,
}
estilo_etiqueta_adicional = {
    "width": 120,
    "height": altura_estandar_campo,
    "font": ("Montserrat", tamaño_letra_normal),
    "text_color": color_blanco,
    "fg_color": color_azul,
}

estilo_etiqueta_adicional_scr = {
    "width": 120,
    "height": altura_estandar_campo,
    "font": ("Montserrat", tamaño_letra_normal),
    "text_color": color_blanco,
    "fg_color": color_azul,
}


estilo_campo = {
    "width": 200,
    "height": altura_estandar_campo,
    "fg_color": color_blanco,
    "border_color": color_blanco,
    "text_color": color_azul,
    "justify": "center",
    "corner_radius": 0,
    "placeholder_text": "...",
    "font": ("Montserrat", tamaño_letra_normal),
}

estilo_lista = {
    "width": 200,
    "height": altura_estandar_campo,
    "fg_color": color_blanco,
    "text_color": color_azul,
    "button_color": color_amarillo,
    "dropdown_fg_color": color_azul,
    "dropdown_text_color": color_blanco,
    "dropdown_font": ("Montserrat", tamaño_letra_normal),
    "anchor": "center",
    "corner_radius": 0,
    "dynamic_resizing": False,
    "font": ("Montserrat", tamaño_letra_normal),
}

estilo_boton = {
    "width": 120,
    "height": altura_estandar_campo,
    "fg_color": color_azul,
    "hover_color": color_amarillo,
    "text_color": color_blanco,
    "font": ("Montserrat", tamaño_letra_normal, "bold"),
    "corner_radius": 0,
}

estilo_boton_lipiar = {
    "width": 120,
    "height": altura_estandar_campo,
    "fg_color": color_azul,
    "hover_color": color_rojo,
    "text_color": color_blanco,
    "font": ("Montserrat", tamaño_letra_normal, "bold"),
    "corner_radius": 0,
}

estilo_boton_spinbox = {
    "height": altura_estandar_campo,
    "fg_color": color_azul,
    "hover_color": color_amarillo,
    "text_color": color_blanco,
    "font": ("Montserrat", tamaño_letra_normal, "bold"),
    "corner_radius": 0,
}

estilo_boton_segmentado = {
    "height": altura_estandar_campo,
    "fg_color": color_blanco,
    "selected_color": color_amarillo,
    "selected_hover_color": color_amarillo,
    "unselected_color": color_azul,
    "unselected_hover_color": color_azul,
    "text_color": color_blanco,
    "text_color_disabled": color_blanco,
    "corner_radius": 0,
    "border_width": 2,
    "font": ("Montserrat", tamaño_letra_normal),
    "dynamic_resizing": False,
}

#=================================================
# DICCIONARIOS
#=================================================

productos = {
    "Xiaomi Redmi 15 C": {"codigo": "X001", "precio": 15000, "stock": 100, "ruta": "xiaomi_redmi_15c.jpg"},
    "Samsung Galaxy S25 ULTRA": {"codigo": "S001", "precio": 20000, "stock": 50, "ruta": "samsung_galaxy_s25_ultra.jpg"},
    "Apple iPhone 15 Pro Max": {"codigo": "A001", "precio": 15000, "stock": 75, "ruta": "apple_iphone_15_pro_max.jpg"},
    "Huawei P60 Pro": {"codigo": "H001", "precio": 12000, "stock": 80, "ruta": "huawei_p60_pro.jpg"},
    "Laptop Asus ROG Strix G16": {"codigo": "L001", "precio": 25000, "stock": 30, "ruta": "asus_rog_strix_g16.jpg"},
    "Tablet Samsung Galaxy Tab S8": {"codigo": "T001", "precio": 8000, "stock": 60, "ruta": "samsung_galaxy_tab_s8.jpg"},
    "Apple Watch series 9": {"codigo": "W001", "precio": 5000, "stock": 40, "ruta": "apple_watch_series_9.jpg"},
    "Audífonos Sony WH-1000XM4": {"codigo": "A002", "precio": 3000, "stock": 90, "ruta": "sony_wh-1000xm4.jpg"},
    "Sony xperia 1 V": {"codigo": "S002", "precio": 18000, "stock": 70, "ruta": "sony_xperia_1_v.jpg"},
}

carrito = []  

#=================================================
# VENTANA
#=================================================

ventana = CTk()
ventana.title("SIDEBAR")
ventana.geometry("1000x800")

ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)

#=================================================
# FRAME PRINCIPAL
#=================================================

frame_principal = CTkFrame(
    master=ventana,
    fg_color=color_fondo,
    corner_radius=0)

frame_principal.grid(
    row=0,
    column=0,
    sticky="snew",
    padx=10,
    pady=10
    )

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=20)

frame_principal.grid_rowconfigure(0,weight=1)

#=================================================
# FRAME SIDEBAR
#=================================================

frame_sidebar = CTkFrame(
    master=frame_principal,
    fg_color=color_azul,
    corner_radius=0)

frame_sidebar.grid(
    row=0,
    column=0,
    sticky="nsew"
    )

frame_sidebar.grid_columnconfigure(0,weight=1)

frame_sidebar.grid_rowconfigure([0,8],weight=1)

frame_sidebar.grid_propagate(False)


titulo = CTkLabel(
    frame_sidebar,
    text="MENU",
    **estilo_etiqueta_titulo
)

titulo.grid(row=0, column=0)


#BOTONES

boton_inicio = CTkButton(
    master=frame_sidebar,
    text="INICIO",
    **estilo_boton,
    command=lambda: ir_a_pestaña("INICIO")
    )

boton_inicio.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

boton_marcket = CTkButton(
    master=frame_sidebar,
    text="MARCKET",
    **estilo_boton,
    command=lambda: ir_a_pestaña("MARCKET")
    )

boton_marcket.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

boton_productos = CTkButton(
    master=frame_sidebar,
    text="PRODUCTOS",
    **estilo_boton,
    command=lambda: ir_a_pestaña("PRODUCTOS")
    )

boton_productos.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

boton_clientes = CTkButton(
    master=frame_sidebar,
    text="CLIENTES",
    **estilo_boton,
    command=lambda: ir_a_pestaña("CLIENTES")
    )

boton_clientes.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

boton_reportes = CTkButton(
    master=frame_sidebar,
    text="REPORTES",
    **estilo_boton,
    command=lambda: ir_a_pestaña("REPORTES")
    )

boton_reportes.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

boton_salir = CTkButton(
    master=frame_sidebar,
    text="SALIR",
    **estilo_boton_lipiar,
    )

boton_salir.grid(row=8, column=0, padx=10, pady=10, sticky="sew")

#=================================================
# FRAME PANEL
#=================================================

frame_panel = CTkFrame(
    master=frame_principal,
    fg_color=color_fondo,
    corner_radius=0
    )

frame_panel.grid(row=0, column=1, sticky="snew")

frame_panel.grid_columnconfigure(0,weight=1)

frame_panel.grid_rowconfigure(0,weight=1)
frame_panel.grid_rowconfigure(1,weight=10)

frame_panel.grid_propagate(False)

#ETIQETA

etiqueta_titulo= CTkLabel(
    master=frame_panel,
    text="INICIO",
    **estilo_etiqueta_titulo
    
)
etiqueta_titulo.grid(row = 0, column = 0, sticky="nsew")

#=================================================
# PESTAÑAS
#=================================================

pestañas = CTkTabview(
    master=frame_panel,
    corner_radius=0,
    fg_color=color_fondo,
    segmented_button_fg_color=color_azul,
    segmented_button_selected_color=color_azul,
    segmented_button_selected_hover_color=color_amarillo,
    segmented_button_unselected_color=color_azul,
    segmented_button_unselected_hover_color=color_amarillo,
    text_color=color_blanco,
    
)

pestañas.grid(
    row=1,
    column=0,
    sticky="nsew",
    
)

pestaña_inicio = pestañas.add("INICIO")
pestaña_marcket = pestañas.add("MARCKET")
pestaña_productos = pestañas.add("PRODUCTOS")
pestaña_clientes = pestañas.add("CLIENTES")
pestaña_reportes = pestañas.add("REPORTES")

#=================================================
# FRAME INICIO
#=================================================
pestaña_inicio.configure(fg_color=color_fondo)

pestaña_inicio.grid_columnconfigure(0,weight=1)
pestaña_inicio.grid_rowconfigure([0,1,2], weight=1)


#=================================================
# FRAME SUPERIOR INICIO
#=================================================

frame_superior_inicio = CTkFrame(
    master=pestaña_inicio,
    fg_color=color_blanco,
    corner_radius=0,
    
)

frame_superior_inicio.grid_columnconfigure([0,1,2],weight=1)

frame_superior_inicio.grid_rowconfigure(0, weight=1)

frame_superior_inicio.grid(row=0, column=0, sticky="nsew")


#=================================================
# FRAME VENTAS INICIO
#=================================================

frame_ventas_inicio = CTkFrame(
    master=frame_superior_inicio,
    corner_radius=0,
    fg_color=color_azul,
)

frame_ventas_inicio.grid_columnconfigure(0, weight=1)

frame_ventas_inicio.grid_rowconfigure(0, weight=1)
frame_ventas_inicio.grid_rowconfigure(1, weight=1)

frame_ventas_inicio.grid(row=0, column=0,sticky="nsew", padx=10, pady=10)



ventas_inicio = CTkLabel(
    master=frame_ventas_inicio,
    text="VENTAS TOTAL",
    width= 150,
    height= altura_estandar_campo,
    font= ("Montserrat", 22),
    text_color= color_blanco,
    fg_color= transparente
    )

ventas_inicio.grid(row=0,column=0,sticky="s")

total_ventas_inicio = CTkLabel(
    master=frame_ventas_inicio,
    text="Q--",
    width= 150,
    height= altura_estandar_campo,
    font= ("Montserrat", 22),
    text_color= color_blanco,
    fg_color= transparente
    )

total_ventas_inicio.grid(row=1,column=0,sticky="n")


#=================================================
# FRAME PRODUCTOS INICIO
#=================================================

frame_productos_inicio = CTkFrame(
    master=frame_superior_inicio,
    corner_radius=0,
    fg_color=color_amarillo
)

frame_productos_inicio.grid_columnconfigure(0, weight=1)
frame_productos_inicio.grid_rowconfigure(0, weight=1)
frame_productos_inicio.grid_rowconfigure(1, weight=1)

frame_productos_inicio.grid(row=0, column=1,sticky="nsew", padx=10, pady=10)

productos_inicio = CTkLabel(
    master=frame_productos_inicio,
    text="TOTAL PRODUCTOS",
    width= 150,
    height= altura_estandar_campo,
    font= ("Montserrat", 22),
    text_color= color_blanco,
    fg_color= transparente
    )

productos_inicio.grid(row=0,column=0,sticky="s")

total_productos_inicio = CTkLabel(
    master=frame_productos_inicio,
    text="--",
    width= 150,
    height= altura_estandar_campo,
    font= ("Montserrat", 22),
    text_color= color_blanco,
    fg_color= transparente
    )

total_productos_inicio.grid(row=1,column=0,sticky="n")

#=================================================
# FRAME CLIENTES INICIO
#=================================================

frame_clientes_inicio = CTkFrame(
    master=frame_superior_inicio,
    corner_radius=0,
    fg_color=color_azul
)

frame_clientes_inicio.grid_columnconfigure(0, weight=1)
frame_clientes_inicio.grid_rowconfigure(0, weight=1)
frame_clientes_inicio.grid_rowconfigure(1, weight=1)

frame_clientes_inicio.grid(row=0, column=2,sticky="nsew", padx=10, pady=10)

frame_clientes_inicio.grid_propagate(False)

clientes_inicio = CTkLabel(
    master=frame_clientes_inicio,
    text="TOTAL CLIENTES",
    width= 150,
    height= altura_estandar_campo,
    font= ("Montserrat", 22),
    text_color= color_blanco,
    fg_color= transparente
    )

clientes_inicio.grid(row=0,column=0,sticky="s")

total_clientes_inicio = CTkLabel(
    master=frame_clientes_inicio,
    text="--",
    width= 150,
    height= altura_estandar_campo,
    font= ("Montserrat", 22),
    text_color= color_blanco,
    fg_color= transparente
    )

total_clientes_inicio.grid(row=1,column=0,sticky="n")

#=================================================
# FRAME CENTRAL INICIO
#=================================================

frame_central_inicio = CTkFrame(
    master=pestaña_inicio,
    corner_radius=0,
    fg_color=color_blanco
)

frame_central_inicio.grid(row=1, column=0, sticky="nsew",pady=10)

#=================================================
# FRAME INFERIOR INICIO
#=================================================

frame_inferior_inicio = CTkFrame(
    master=pestaña_inicio,
    corner_radius=0,
    fg_color=color_blanco
)

frame_inferior_inicio.grid(row=2, column=0, sticky="nsew", pady=10)

#=================================================
# FRAME MARCKET
#=================================================

pestaña_marcket.configure(fg_color=color_blanco)

pestaña_marcket.grid_columnconfigure(0,weight=1)

pestaña_marcket.grid_rowconfigure(0, weight=2)
pestaña_marcket.grid_rowconfigure(1, weight=1)
pestaña_marcket.grid_rowconfigure(2, weight=5)
pestaña_marcket.grid_rowconfigure(3, weight=1)

#=================================================
# FRAME SUPERIOR MARCKET
#=================================================

frame_superior_marcket = CTkFrame(
    master=pestaña_marcket,
    fg_color=color_blanco,
    corner_radius=0
)

frame_superior_marcket.grid(row=0, column=0, sticky="snew")

frame_superior_marcket.grid_columnconfigure(0,weight=1)
frame_superior_marcket.grid_columnconfigure(1,weight=1)

frame_superior_marcket.grid_rowconfigure(0,weight=1)
frame_superior_marcket.grid_rowconfigure(1,weight=1)
frame_superior_marcket.grid_rowconfigure(2,weight=1)

# ITEMS etiqueta y menu de opciones

etiqueta_items = CTkLabel(
    master=frame_superior_marcket,
    text="ITEMS:",
    **estilo_etiqueta_normal
    )

etiqueta_items.grid(
    row=0,
    column=0,
    )


menu_items =CTkOptionMenu(
    master=frame_superior_marcket,
    **estilo_lista
)

menu_items.grid(row=0,column=1,sticky="ew",padx=10)

# CANTIDAD etiqueta y cuadro de SPINBOX


etiqueta_cantidad = CTkLabel(
    master=frame_superior_marcket,
    text="CANTIDAD:",
    **estilo_etiqueta_normal)

etiqueta_cantidad.grid(row=2, column=0,)

#frame spinbox

frame_spinbox = CTkFrame(
    master=frame_superior_marcket,
    fg_color="transparent",
    corner_radius=0
)

frame_spinbox.grid(
    row=2,
    column=1,
    sticky= "ew",
    padx=10
    )

frame_spinbox.grid_columnconfigure([0,1,2], weight=1)
frame_spinbox.grid_rowconfigure(0, weight=1)

# boton de restar spinbox

boton_restar = CTkButton(
    master=frame_spinbox,
    text="-",
    **estilo_boton_spinbox,
    command= decrementar_boletos,
    )

boton_restar.grid(
    row=0,
    column=0,
    sticky="ew"
    )

#texto spinbox


cantidad_boletos = IntVar(value=0)

campo_cantidad = CTkEntry(
    master=frame_spinbox,
    state="readonly",
    textvariable=cantidad_boletos,
    **estilo_campo
    )

campo_cantidad.grid(
    row=0, 
    column=1,
    padx=1,
    sticky="ew"
    )

# boton de sumar spinbox

boton_sumar = CTkButton(
    master=frame_spinbox,
    text="+",
    **estilo_boton_spinbox,
    command=incrementar_boletos,
    )

boton_sumar.grid(
    row=0,
    column=2,
    sticky="ew"
    )

#boton agregar

boton_agregar = CTkButton(
    master=frame_superior_marcket,
    text="AGREGAR",
    **estilo_boton,
    )

boton_agregar.grid(row=3, column=1, sticky="e", padx=10, pady=10)

#=================================================
# FRAME TITULOS MARCKET
#=================================================

frame_titulos_marcket = CTkFrame(
    master=pestaña_marcket,
    fg_color="transparent",
    corner_radius=0
)

frame_titulos_marcket.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=10
)

frame_titulos_marcket.grid_columnconfigure(0, weight=2)
frame_titulos_marcket.grid_columnconfigure(1, weight=8)
frame_titulos_marcket.grid_columnconfigure(2, weight=1)
frame_titulos_marcket.grid_columnconfigure(3, weight=2)
frame_titulos_marcket.grid_columnconfigure(4, weight=2)

frame_titulos_marcket.grid_rowconfigure(0, weight=1)

etiqueta_codigo_scroll = CTkLabel(
    master=frame_titulos_marcket,
    text="CODIGO",
    **estilo_etiqueta_normal_scr
)

etiqueta_codigo_scroll.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=5
)

etiqueta_item_scroll = CTkLabel(
    master=frame_titulos_marcket,
    text="ITEM",
    **estilo_etiqueta_adicional_scr
)

etiqueta_item_scroll.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=5
)

etiqueta_cantidad_scroll = CTkLabel(
    master=frame_titulos_marcket,
    text="CANTIDAD",
    **estilo_etiqueta_normal_scr
)

etiqueta_cantidad_scroll.grid(
    row=0,
    column=2,
    sticky="ew",
    padx=5
)

etiqueta_precio_scroll = CTkLabel(
    master=frame_titulos_marcket,
    text="PRECIO",
    **estilo_etiqueta_normal_scr
)

etiqueta_precio_scroll.grid(
    row=0,
    column=3,
    sticky="ew",
    padx=5
)

etiqueta_total_scroll = CTkLabel(
    master=frame_titulos_marcket,
    text="TOTAL",
    **estilo_etiqueta_adicional_scr
)

etiqueta_total_scroll.grid(
    row=0,
    column=4,
    sticky="ew",
    padx=5
)

#=================================================
# FRAME SCROLLABLE MARCKET
#=================================================

fram_scroll_marcket = CTkScrollableFrame(
    master=pestaña_marcket,
    fg_color=color_fondo,
    corner_radius=0,
    scrollbar_button_color=color_amarillo,
    scrollbar_button_hover_color=color_azul,
    border_color=color_blanco,
)

fram_scroll_marcket.grid(row=2, columnspan=5, sticky="snew",padx=10)

fram_scroll_marcket.grid_columnconfigure(0,weight=2)
fram_scroll_marcket.grid_columnconfigure(1,weight=8)
fram_scroll_marcket.grid_columnconfigure(2,weight=1)
fram_scroll_marcket.grid_columnconfigure(3,weight=2)
fram_scroll_marcket.grid_columnconfigure(4,weight=2)

fram_scroll_marcket.grid_rowconfigure(0,weight=1)

#=================================================
# FRAME INFERIOR MARCKET
#=================================================

frame_inferior_marcket = CTkFrame(
    master=pestaña_marcket,
    fg_color=color_blanco,
    corner_radius=0
)

frame_inferior_marcket.grid(row=3, column=0, sticky="snew")

frame_inferior_marcket.grid_columnconfigure(0,weight=1)

frame_inferior_marcket.grid_rowconfigure(0,weight=1)

#boton facturar

boton_facturar = CTkButton(
    master=frame_inferior_marcket,
    text="FACTURAR",
    **estilo_boton
)

boton_facturar.grid(row=3, column=1, sticky="e", padx=10, pady=10)

#=================================================
# FRAME PRINCIPAL PRODUCTOS
#=================================================

pestaña_productos.configure(fg_color=color_fondo)

pestaña_productos.grid_columnconfigure(0,weight=1)

pestaña_productos.grid_rowconfigure(0, weight=1)
pestaña_productos.grid_rowconfigure(1, weight=10)

#=================================================
# FRAME AGREGAR PRODUCTOS
#=================================================

frame_agregar_productos = CTkFrame(
    master=pestaña_productos,
    fg_color=color_blanco,
    corner_radius=0,
)

frame_agregar_productos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

frame_agregar_productos.grid_columnconfigure(0, weight=1)
frame_agregar_productos.grid_columnconfigure(1, weight=1)
frame_agregar_productos.grid_columnconfigure(2, weight=1)
frame_agregar_productos.grid_columnconfigure(3, weight=1)

frame_agregar_productos.grid_rowconfigure(0, weight=1)
frame_agregar_productos.grid_rowconfigure(1, weight=1)
frame_agregar_productos.grid_rowconfigure(2, weight=1)


etiqueta_agregar_productos = CTkLabel(
    master=frame_agregar_productos,
    text="PRODUCTO",
    **estilo_etiqueta_normal
)

etiqueta_agregar_productos.grid(row=0, column=0, padx=10, pady=10)

campo_agregar_productos = CTkEntry(
    master=frame_agregar_productos,
    **estilo_campo
)

campo_agregar_productos.grid(row=0, column=1, padx=10, pady=10)

etiqueta_agregar_marca = CTkLabel(
    master=frame_agregar_productos,
    text="MARCA",
    **estilo_etiqueta_normal
)

etiqueta_agregar_marca.grid(row=1, column=0, padx=10, pady=10)

campo_agregar_marca = CTkEntry(
    master=frame_agregar_productos,
    **estilo_campo
)

campo_agregar_marca.grid(row=1, column=1, padx=10, pady=10)

etiqueta_agregar_precio = CTkLabel(
    master=frame_agregar_productos,
    text="PRECIO",
    **estilo_etiqueta_normal
)

etiqueta_agregar_precio.grid(row=0, column=2, padx=10, pady=10)

campo_agregar_precio = CTkEntry(
    master=frame_agregar_productos,
    **estilo_campo
)

campo_agregar_precio.grid(row=0, column=3, padx=10, pady=10)

etiqueta_agregar_stock = CTkLabel(
    master=frame_agregar_productos,
    text="STOCK",
    **estilo_etiqueta_normal
)

etiqueta_agregar_stock.grid(row=1, column=2, padx=10, pady=10)

campo_agregar_stock = CTkEntry(
    master=frame_agregar_productos,
    **estilo_campo
)

campo_agregar_stock.grid(row=1, column=3, padx=10, pady=10)

#=================================================
#BOTON LIMPIAR PRODUCTOS

boton_limpiar_productos = CTkButton(
    master=frame_agregar_productos,
    text="LIMPIAR",
    **estilo_boton_lipiar,
)

boton_limpiar_productos.grid(row=2, column=1, sticky="e", padx=10, pady=10)

#=================================================
#BOTON AGREGAR PRODUCTOS

boton_agregar_productos = CTkButton(
    master=frame_agregar_productos,
    text="AGREGAR",
    **estilo_boton,
)

boton_agregar_productos.grid(row=2, column=2, sticky="w", padx=10, pady=10)


#=================================================
# FRAME PRODUCTOS
#=================================================

frame_principal_productos = CTkScrollableFrame(
    master=pestaña_productos,
    fg_color=color_blanco,
    corner_radius=0,
    scrollbar_button_color=color_amarillo,
    scrollbar_button_hover_color=color_azul,
    border_color=color_blanco,)

frame_principal_productos.grid(row=1, column=0, sticky="snew", padx=10, pady=10)

columna = 0
fila = 0

for producto in productos: 

    frame_principal_productos.grid_columnconfigure(columna, weight=1)
    frame_principal_productos.grid_rowconfigure(fila, weight=1)

    frame_producto = CTkFrame(
        master=frame_principal_productos,
        fg_color=color_blanco,
        corner_radius=0,
    )
    
    frame_producto.grid_rowconfigure(0, weight=10)
    frame_producto.grid_rowconfigure(1, weight=2)
    frame_producto.grid_rowconfigure(2, weight=2)
    
    frame_producto.grid_columnconfigure(0, weight=1)
    
    frame_producto.grid(
        row=fila,
        column=columna,
        sticky="ew",
        padx=10,
        pady=10,
    )
    ruta_imagen = os.path.join(ruta_script, f"imagenes/{productos[producto]['ruta']}")

    # Cargar imagen

    imagen_producto = CTkImage(
        light_image=Image.open(ruta_imagen),
        dark_image=Image.open(ruta_imagen),
        size=(100, 100)
    )

    etiqueta_imagen = CTkLabel(
        master=frame_producto,
        text="",
        **estilo_etiqueta_adicional_scr,
        image=imagen_producto,
    )
    etiqueta_imagen.grid(
        row=0,
        column=0,
        #sticky="nsew",
        padx=10,
        pady=10,
    )
    
    etiqueta_producto = CTkLabel(
        master=frame_producto,
        text=producto,
        **estilo_etiqueta_adicional
    )
    
    etiqueta_producto.grid(
        row=1,
        column=0,
        #sticky="nsew",
        padx=10,
        pady=10,
    )
    
    etiqueta_precio = CTkLabel(
        master=frame_producto,
        text=f"Q{productos[producto]['precio']}",
        **estilo_etiqueta_normal_scr
    )
    
    etiqueta_precio.grid(
        row=2,
        column=0,
        #sticky="nsew",
        padx=10,
        pady=10,
    )
    
    columna += 1
    if columna >=3:
        columna = 0
        fila += 1



#=================================================



pestañas._segmented_button.grid_forget()


ventana.mainloop()

