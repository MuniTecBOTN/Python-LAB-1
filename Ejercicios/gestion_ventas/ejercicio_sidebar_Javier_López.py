from customtkinter import *

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

#=================================================
# FUNCIONES
#=================================================

def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    etiqueta_titulo.configure(text=nombre_pestaña)

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
# VENTANA
#=================================================

ventana = CTk()
ventana.title("SIDEBAR")
ventana.geometry("800x600")

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
frame_principal.grid_columnconfigure(1, weight=10)

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
    text="SIDEBAR",
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

boton_ventas = CTkButton(
    master=frame_sidebar,
    text="VENTAS",
    **estilo_boton,
    command=lambda: ir_a_pestaña("VENTAS")
    )

boton_ventas.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

boton_productos = CTkButton(
    master=frame_sidebar,
    text="PRODUCTOS",
    **estilo_boton,
    command=lambda: ir_a_pestaña("PRODUCTOS")
    )

boton_productos.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

boton_inventario = CTkButton(
    master=frame_sidebar,
    text="INVENTARIO",
    **estilo_boton,
    command=lambda: ir_a_pestaña("INVENTARIO")
    )

boton_inventario.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

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
    **estilo_boton,
    )

boton_salir.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

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
pestaña_ventas = pestañas.add("VENTAS")
pestaña_productos = pestañas.add("PRODUCTOS")
pestaña_inventario = pestañas.add("INVENTARIO")
pestaña_clientes = pestañas.add("CLIENTES")
pestaña_reportes = pestañas.add("REPORTES")

pestaña_inicio.configure(fg_color=color_fondo)
pestaña_inicio.grid_columnconfigure(0,weight=1)
pestaña_inicio.grid_rowconfigure(0,weight=1)

#=================================================
# FRAME VENTAS
#=================================================

pestaña_ventas.configure(fg_color=color_fondo)
pestaña_ventas.grid_columnconfigure(0,weight=1)
pestaña_ventas.grid_rowconfigure([0,1,2], weight=1)

#=================================================
frame_superior_ventas = CTkFrame(
    master=pestaña_ventas,
    fg_color=color_fondo,
    corner_radius=0
)

frame_superior_ventas.grid(row=0, column=0, sticky="snew")

frame_superior_ventas.grid_columnconfigure(0,weight=1)
frame_superior_ventas.grid_columnconfigure(1,weight=1)

frame_superior_ventas.grid_rowconfigure(0,weight=1)
frame_superior_ventas.grid_rowconfigure(1,weight=1)

# ITEMS etiqueta y menu de opciones

etiqueta_items = CTkLabel(
    master=frame_superior_ventas,
    text="ITEMS:",
    **estilo_etiqueta_normal
    )

etiqueta_items.grid(
    row=0,
    column=0,
    sticky="e"
    )

menu_items =CTkOptionMenu(
    master=frame_superior_ventas,
    **estilo_lista
)

menu_items.grid(row=0,column=1,sticky="ew")

# CANTIDAD etiqueta y cuadro de SPINBOX

etiqueta_cantidad = CTkLabel(
    master=frame_superior_ventas,
    text="CANTIDAD:",
    **estilo_etiqueta_normal)

etiqueta_cantidad.grid(row=2, column=0, sticky="ew")

#frame spinbox

frame_spinbox = CTkFrame(
    master=frame_superior_ventas,
    fg_color="transparent",
    corner_radius=0
)

frame_spinbox.grid(
    row=2,
    column=1,
    sticky= "ew"
    )

frame_spinbox.grid_columnconfigure([0,1,2], weight=1)
frame_spinbox.grid_rowconfigure(0, weight=1)

# boton de restar spinbox

boton_restar = CTkButton(
    master=frame_spinbox,
    text="-",
    **estilo_boton_spinbox,
    )

boton_restar.grid(
    row=0,
    column=0,
    )

#texto spinbox

cantidad_items = IntVar(value=0)

campo_cantidad = CTkEntry(
    master=frame_spinbox,
    state="readonly",
    width= 180,
    corner_radius= 0,
    fg_color= color_blanco,
    justify= "center",
    border_color= color_blanco,
    textvariable=cantidad_items,
    font= ("Montserrat", 16, "bold")
    )

campo_cantidad.grid(
    row=0, 
    column=1,
    padx=1
    )

# boton de sumar spinbox

boton_sumar = CTkButton(
    master=frame_spinbox,
    text="+",
    **estilo_boton_spinbox,
    )

boton_sumar.grid(
    row=0,
    column=2,
    )


#=================================================

fram_central_ventas = CTkScrollableFrame(
    master=pestaña_ventas,
    fg_color=color_azul,
    corner_radius=0,
    scrollbar_button_color=color_verde,
    scrollbar_button_hover_color=color_amarillo
)

fram_central_ventas.grid(row=1, column=0, sticky="snew", padx=10,pady=10)

fram_central_ventas.grid_columnconfigure(0,weight=1)

fram_central_ventas.grid_rowconfigure(0,weight=1)

#=================================================

fram_inferior_ventas = CTkFrame(
    master=pestaña_ventas,
    fg_color=color_verde,
    corner_radius=0
)

fram_inferior_ventas.grid(row=2, column=0, sticky="snew")

fram_inferior_ventas.grid_columnconfigure(0,weight=1)

fram_inferior_ventas.grid_rowconfigure(0,weight=1)


#=================================================

pestaña_productos.configure(fg_color=color_fondo)
pestaña_productos.grid_columnconfigure(0,weight=1)
pestaña_productos.grid_rowconfigure(0,weight=1)

pestaña_inventario.configure(fg_color=color_fondo)
pestaña_inventario.grid_columnconfigure(0,weight=1)
pestaña_inventario.grid_rowconfigure(0,weight=1)

pestañas._segmented_button.grid_forget()





ventana.mainloop()

