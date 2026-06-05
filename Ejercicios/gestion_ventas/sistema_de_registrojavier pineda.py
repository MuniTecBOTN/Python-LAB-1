from customtkinter import *

set_default_color_theme("dark-blue")
color_fondo = "#e3e5f3"
color_azul = "#143a81"
color_verde = "#81dc00"
color_blanco = "#ffffff"
color_otro = "#0062ff"
color_tambien = "#008cff"
color_amarillo = "#ffcf03"
color_rojo="#cc0000"
color_scroll="#D4CBCB"




estilo_etiquetas = {
    "width": 150,
    "height": 30,
    "font": ("Montserrat", 16, "bold"),
    "text_color": color_blanco,
    "fg_color": color_amarillo,
    "corner_radius": 0,
}


estilo_botones = {
    "width": 120,
    "height": 35,
    "corner_radius": 0,
    "fg_color": color_azul,
    "hover_color": color_amarillo,
    "text_color": color_blanco,
    "font": ("Montserrat", 16, "bold"),
}

# CUADRO DE TEXTO

estilo_cuadro_texto = {
    "width": 400,
    "corner_radius": 0,
    "fg_color": color_blanco,
    "justify": "center",
    "border_color": color_blanco,
    "font": ("Montserrat", 16, "bold"),
}



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
frame_principal=CTkFrame(master=ventana,
                        fg_color=color_fondo,
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", )
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=12)


frame_principal.grid_rowconfigure(0, weight=1)




frame_derecho=CTkFrame(master=frame_principal,
                       fg_color=color_fondo,
                       corner_radius=0,
                       height=400
                         )
frame_derecho.grid(row=0,column=1,sticky="news")
frame_derecho.grid_columnconfigure(0,weight=1)
frame_derecho.grid_rowconfigure(0,weight=1)
frame_derecho.grid_rowconfigure(1,weight=10)


frame_superior=CTkFrame(master=frame_derecho,
                        fg_color=color_fondo,
                        corner_radius=0)
frame_superior.grid(row=0,column=0,sticky="new")


frame_izquierdo=CTkFrame(master=frame_principal,
                         fg_color=color_fondo,
                         corner_radius=0)
frame_izquierdo.grid(row=0, column=0,sticky="wnse")
frame_izquierdo.grid_columnconfigure(0,weight=1)
frame_izquierdo.grid_columnconfigure(1,weight=1)
pestañas=CTkTabview(
    master=frame_derecho,
    corner_radius=0,
    fg_color=color_fondo,
    segmented_button_fg_color=color_azul,
    segmented_button_selected_color=color_rojo,
    segmented_button_selected_hover_color=color_rojo,
    text_color=color_blanco
)

pestañas.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=8,
)

inicio= pestañas.add("inicio")
ventas= pestañas.add("ventas")
productos=pestañas.add("productos")
invetario=pestañas.add("inventario")
clientes=pestañas.add("clientes")
reportes=pestañas.add("reportes")
salir=pestañas.add("salir")
inicio.configure(fg_color=color_fondo)
inicio.configure(fg_color=color_blanco)

inicio.grid_columnconfigure(0,weight=1)
inicio.grid_columnconfigure(1,weight=1)
inicio.grid_rowconfigure([0,1,2,3,4,5],weight=1)
pestañas._segmented_button.grid_forget()


ventas.grid_columnconfigure(0,weight=1)
ventas.rowconfigure(0,weight=1)
ventas.rowconfigure(1,weight=1)
ventas.rowconfigure(2,weight=1)
    
def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    nombre_progama.configure(text=nombre_pestaña)









boton_formulario=CTkButton(
    master=frame_izquierdo,
    text="INICIO",
    fg_color=color_azul,
    hover_color="#031b5e",
    command=lambda:ir_a_pestaña("inicio")
)

boton_formulario.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

boton_registro=CTkButton(
    master=frame_izquierdo,
    text="VENTAS    ",
    fg_color=color_azul,
    command=lambda:ir_a_pestaña("ventas")
)
boton_registro.grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
)


boton_producto=CTkButton(
    master=frame_izquierdo,
    text="PRODUCTOS",
    fg_color=color_azul,
    command=lambda:ir_a_pestaña("productos")
)
boton_producto.grid(
    row=3,
    column=0,
    padx=10,
    pady=10,
)
boton_inventario=CTkButton(
    master=frame_izquierdo,
    text="inventario",
    fg_color=color_azul,
    command=lambda:ir_a_pestaña("inventario")
)
boton_inventario.grid(
    row=4,
    column=0,
    padx=10,
    pady=10,
)
boton_clientes=CTkButton(
    master=frame_izquierdo,
    text="CLIENTES",
    fg_color=color_azul,
    command=lambda:ir_a_pestaña("clientes")
)
boton_clientes.grid(
    row=5,
    column=0,
    padx=10,
    pady=10,
)
boton_reportes=CTkButton(
    master=frame_izquierdo,
    text="REPORTES",
    fg_color=color_azul,
    command=lambda:ir_a_pestaña("reportes")
)
boton_reportes.grid(
    row=6,
    column=0,
    padx=10,
    pady=10,
)
boton_salir=CTkButton(
    master=frame_izquierdo,
    text="SALIR",
    fg_color=color_azul,
    hover_color=color_rojo,
    command=ventana.destroy
)
boton_salir.grid(
    row=7,
    column=0,
    padx=10,
    pady=10,
)
nombre_progama = CTkLabel(
    master=frame_superior,
    fg_color="transparent",
    text="SISTEMA DE REGISTRO",
    font=("Montserrat", 26),
    anchor=CENTER
)
nombre_progama.grid(
    row=0,
    column=0,
)
frame_escroleable=CTkScrollableFrame(
    master=ventas,
    fg_color=color_scroll,
    corner_radius=0
)
frame_escroleable.grid(
    row=1,
    column=0,
    sticky="wes"
)
frame_escroleable.grid_columnconfigure(0,weight=1)
frame_escroleable.grid_columnconfigure(1,weight=1)
frame_escroleable.grid_columnconfigure(2,weight=1)
frame_escroleable.grid_columnconfigure(3,weight=1)
frame_escroleable.grid_columnconfigure(4,weight=1)

frame_escroleable.grid_rowconfigure(0,weight=1)








frame_ventas_arriba=CTkFrame(
    master=ventas,
    fg_color=color_fondo,    
    corner_radius=0
)
frame_ventas_arriba.grid(
    row=0,
    column=0
)
frame_ventas_arriba.grid_columnconfigure(0,weight=1)
frame_ventas_arriba.grid_columnconfigure(1,weight=1)
frame_ventas_arriba.rowconfigure(0,weight=1)
frame_ventas_arriba.rowconfigure(1,weight=1)












item=CTkLabel(
    master=frame_ventas_arriba,
    text="ITEM",
    **estilo_etiquetas
)
item.grid(
    row=0,
    column=0,
    sticky="w"
)
lista_opciones = ["LAPTOP DELL", "LAPTOP HP", "LAPTOP XIAOMI","LAPTOP THINKERCARD"]
valor_menu_opciones = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_ventas_arriba,
    width=280,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_opciones,
    variable=valor_menu_opciones,
    anchor="center",
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=0,
    column=1,
    sticky="ew"
)




etiqueta_cantidad = CTkLabel(
    master=frame_ventas_arriba, 
    text="CANTIDAD:",
   **estilo_etiquetas
)

etiqueta_cantidad.grid(row=1, column=0, sticky="ew")

frame_spinbox = CTkFrame(master=frame_ventas_arriba,fg_color=color_fondo)
frame_spinbox.grid(row=1, column=1, sticky="nsew")
frame_spinbox.grid_columnconfigure([0, 1, 2], weight=1)
frame_spinbox.grid_rowconfigure(0, weight=1)




def funcion_disminuir():
    cantidad_actual = cantidad.get()
    if cantidad_actual > 0:
        cantidad.set(cantidad_actual - 1)
   




boton_disminuir = CTkButton(
    master=frame_spinbox,
    text="-",
    command=funcion_disminuir,
    **estilo_botones
)
boton_disminuir.grid(row=0, column=0, sticky="e", padx=15,pady=15)


def funcion_aumentar():
    cantidad_actual = cantidad.get()
    cantidad.set(cantidad_actual + 1)
    

boton_aumentar = CTkButton(
    master=frame_spinbox,
    text="+",
    command=funcion_aumentar,
    **estilo_botones
)
boton_aumentar.grid(row=0, column=2, sticky="w", padx=15,
    pady=15)

cantidad=IntVar(value=0)
caja_cantidad = CTkEntry(
    master=frame_spinbox,
    state="readonly",
    textvariable=cantidad
    
)
caja_cantidad.grid(row=0, column=1, sticky="ew", padx=2)



def funcion_boton_1():
    print(f"Has presionado el Botón 1")


boton_agregar = CTkButton(
    master=frame_ventas_arriba,
    width=80,
    height=30,
    corner_radius=0,
    text="AGREGAR",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_1,
)

boton_agregar.grid(
    row=2,
    column=1,
    sticky="s"
)

etiqueta_codigo=CTkLabel(
    master=frame_escroleable,
    text="CODIGO",
    **estilo_etiquetas
)
etiqueta_codigo.grid(
    row=0,
    column=0
)
etiquetaitem=CTkLabel(
    master=frame_escroleable,
    text="ITEM",
    **estilo_etiquetas
)
etiquetaitem.grid(
    row=0,
    column=1
)

etiqueta_cantidades=CTkLabel(
    master=frame_escroleable,
    text="CANTIDAD",
    **estilo_etiquetas
)

etiqueta_cantidades.grid(
    row=0,
    column=2
)
etiqueta_precio=CTkLabel(
    master=frame_escroleable,
    text="PRECiO",
    **estilo_etiquetas
)
etiqueta_precio.grid(
    row=0,
    column=3
)
etiquetatotal=CTkLabel(
    master=frame_escroleable,
    text="TOTAL",
    **estilo_etiquetas
)
etiquetatotal.grid(
    row=0,
    column=4
)






























ventana.mainloop()