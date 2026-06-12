from customtkinter import *
set_default_color_theme("green")
set_appearance_mode("dark")
COLOR_FONDO = "#f0f2f5"
COLOR_AZUL = "#143a81"
COLOR_AMARILLO = "#ffcf03"
COLOR_BLANCO = "#ffffff"
COLOR_ROJO = "#ee4c4c"
COLOR_VERDE = "#2ce429"
TRANSPARENTE = "transparent"
ALTURA_ESTANDAR_CAMPO = 30
TAMAÑO_LETRA_NORMAL = 16
TAMAÑO_LETRA_TITULO = 28 
# =========================================================
# ESTILOS
# =========================================================
estilo_etiqueta_titulo = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_TITULO),
    "text_color": COLOR_BLANCO,
    "fg_color": COLOR_AZUL,
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
def agregar():
    producto=menuItem.get()
    precioUn=productos[producto]
    quanty=cantidad.get()
    precioTotal=precioUn*quanty
    print(f"Producto: {producto}, precioUnitario: {precioUn}, cantidad: {quanty}, precioTotal: {precioTotal}")
    
    return

def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    labelTitulo.configure(text=nombre_pestaña.upper())
    return
def aumentarCantidad():
    cantidad.set(cantidad.get()+1)
    return

def restarCantidad():
    cantidad.set(cantidad.get()-1)
    if cantidad.get()<0:
        cantidad.set(0)
    return

ventana=CTk()
cantidad=IntVar(value=0)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=2)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=2)
ventana.geometry("900x600")
sidebar=CTkFrame(master=ventana,
                 fg_color=COLOR_AZUL,
                 corner_radius=0)


labelTitulo=CTkLabel(master=ventana,
                         text="INICIO",
                         **estilo_etiqueta_titulo,
                         
)
labelTituloSide=CTkLabel(master=ventana,
                         text="Menu",
                         **estilo_etiqueta_titulo,
)

labelTitulo.grid(row=0, column=1, sticky="snew")
labelTituloSide.grid(row=0, column=0, sticky="snew")
btnsLabels=["Inicio", 
      "Ventas",
      "Productos",
      "Inventario",
      "Clientes",
      "Reportes",
      "Salir"
      ]
btns=[]
pestañasframes=[]
sidebar.grid_columnconfigure(0, weight=1)
pestañas=CTkTabview(
    master=ventana,
    corner_radius=0,
    fg_color=COLOR_FONDO
)
pestañas.propagate(False)
for i, btn in enumerate(btnsLabels):
    pestañasframes.append(pestañas.add(btn))
    sidebar.grid_rowconfigure(i, weight=1)
    if btn=="Salir":
        boton=CTkButton(master=sidebar,
                    text=btn,
                    **estilo_boton,
                    command=lambda: ventana.destroy()
                    )
    else:
        boton=CTkButton(master=sidebar,
                        text=btn,
                        **estilo_boton,
                        command=lambda x=btn: ir_a_pestaña(x)
                        )
    btns.append(boton)
    btns[i].grid(row=i, column=0, sticky="ew", padx=30)    
    
sidebar.grid(row=1, column=0, sticky="snew")
pestañas._segmented_button.grid_forget()
pestañas.set("Ventas")
pestañas.grid(row=1, column=1, sticky="snew")
pestañas.grid_propagate(False)

pestañasframes[1].grid_rowconfigure(0, weight=1)
pestañasframes[1].grid_rowconfigure(1, weight=1)
pestañasframes[1].grid_rowconfigure(2, weight=1)
pestañasframes[1].grid_rowconfigure(3, weight=1)
pestañasframes[1].grid_rowconfigure(4, weight=1)
pestañasframes[1].grid_columnconfigure(0, weight=1)
pestañasframes[1].grid_columnconfigure(1, weight=1)
pestañasframes[1].grid_columnconfigure(2, weight=1)
pestañasframes[1].grid_columnconfigure(3, weight=1)

productos={"Laptop 1": 1500, "Telefono 1":500}

labelItem=CTkLabel(
    master=pestañasframes[1],
    text="ITEM",
    **estilo_etiqueta_normal
)
labelItem.grid(row=0, column=1, sticky="e", padx=5)
menuItem=CTkOptionMenu(master=pestañasframes[1],
                       values=list(productos.keys()),
                       **estilo_lista
                       )
menuItem.grid(row=0, column=2, sticky="we", padx=5, columnspan=2)
labelCantidad=CTkLabel(
    master=pestañasframes[1],
    text="CANTIDAD",
    **estilo_etiqueta_normal
)
labelCantidad.grid(row=1, column=1, sticky="e", padx=5)
frameCantidad=CTkFrame(master=pestañasframes[1],
                       fg_color=COLOR_FONDO,
                       corner_radius=0)
frameCantidad.grid_rowconfigure(0, weight=1)
frameCantidad.grid_columnconfigure(0, weight=1)
frameCantidad.grid_columnconfigure(1, weight=1)
frameCantidad.grid_columnconfigure(2, weight=1)

btnmas=CTkButton(master=frameCantidad,
                 text="+",
                 **estilo_boton,
                 command=aumentarCantidad)

btnmenos=CTkButton(master=frameCantidad,  
                 text="-",
                 **estilo_boton,
                 command=restarCantidad)

entrycantidad=CTkEntry(master=frameCantidad,
                       state="readonly",
                       textvariable=cantidad,
                       **estilo_campo,
                       )

entrycantidad.grid(row=0, column=1, sticky="w", padx=5)
btnmas.grid(row=0, column=2, sticky="w", padx=5)
btnmenos.grid(row=0, column=0, sticky="w", padx=5)
frameCantidad.grid(row=1, column=2, sticky="w", padx=5)

buttonAgregar=CTkButton(master=pestañasframes[1],
                        text="Agregar",
                        command=agregar,
                        **estilo_boton)
buttonAgregar.grid(row=2, column=2)
frameTabla=CTkFrame(master=pestañasframes[1],
                    fg_color=COLOR_FONDO,
                    corner_radius=0)

frameTabla.grid_columnconfigure(0, weight=1)
frameTabla.grid_columnconfigure(1, weight=1)
frameTabla.grid_columnconfigure(2, weight=1)
frameTabla.grid_columnconfigure(3, weight=1)
frameTabla.grid_rowconfigure(0, weight=1)
frameTabla.grid_rowconfigure(1, weight=1)

frameEncabezados=CTkFrame(master=frameTabla,
                          fg_color=COLOR_FONDO,
                          corner_radius=0)

frameEncabezados.grid_columnconfigure(0, weight=1)
frameEncabezados.grid_columnconfigure(1, weight=1)
frameEncabezados.grid_columnconfigure(2, weight=1)
frameEncabezados.grid_columnconfigure(3, weight=1)
frameEncabezados.grid_rowconfigure(0, weight=1)

labelCodigoTabla=CTkLabel(master=frameEncabezados,
                     text="CODIGO",
                     **estilo_etiqueta_normal
                     )
labelItemTabla=CTkLabel(master=frameEncabezados,
                     text="ITEM",
                     **estilo_etiqueta_normal
                     )
labelCantidadTabla=CTkLabel(master=frameEncabezados,
                     text="CANTIDAD",
                     **estilo_etiqueta_normal
                     )
labelPrecioUnitario=CTkLabel(master=frameEncabezados,
                     text="Precio Unitario",
                     **estilo_etiqueta_normal
                     )
labelTotalTabla=CTkLabel(master=frameEncabezados,
                     text="TOTAL",
                     **estilo_etiqueta_normal
                     )

scrollFrameVentas = CTkScrollableFrame(master=frameTabla,
                                       corner_radius=0,
                                       fg_color=COLOR_FONDO)

labelCodigoTabla.grid(row=0, column=0, sticky="snew")
labelItemTabla.grid(row=0, column=1, sticky="snew")
labelCantidadTabla.grid(row=0, column=2, sticky="snew")
labelTotalTabla.grid(row=0, column=3, sticky="snew")

frameEncabezados.grid(row=0, column=0, sticky="snew",columnspan=4)
scrollFrameVentas.grid(row=1, column=0, sticky="snew",columnspan=4)
frameTabla.grid(row=3, column=0, columnspan=5, sticky="snew")

buttonFacturar=CTkButton(master=pestañasframes[1],
                         text="Facturar",
                         **estilo_boton
)
buttonFacturar.grid(row=4, column=2, )
ventana.mainloop()