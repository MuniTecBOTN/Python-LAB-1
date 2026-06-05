from customtkinter import *

set_default_color_theme("dark-blue")

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
                        fg_color="#c9c6c6",
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", )
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=12)


frame_principal.grid_rowconfigure(0, weight=1)




frame_derecho=CTkFrame(master=frame_principal,
                       fg_color="#ffffff",
                       corner_radius=0,
                       height=400
                         )
frame_derecho.grid(row=0,column=1,sticky="news")
frame_derecho.grid_columnconfigure(0,weight=1)
frame_derecho.grid_rowconfigure(0,weight=1)
frame_derecho.grid_rowconfigure(1,weight=10)


frame_superior=CTkFrame(master=frame_derecho,
                        fg_color="#747474",
                        corner_radius=0)
frame_superior.grid(row=0,column=0,sticky="new")


frame_izquierdo=CTkFrame(master=frame_principal,
                         fg_color="#6e6e6e",
                         corner_radius=0)
frame_izquierdo.grid(row=0, column=0,sticky="wnse")
frame_izquierdo.grid_columnconfigure(0,weight=1)
frame_izquierdo.grid_columnconfigure(1,weight=1)
pestañas=CTkTabview(
    master=frame_derecho,
    corner_radius=0,
    fg_color="#414141",
    segmented_button_fg_color="#1519db",
    segmented_button_selected_color="#5e0606",
    segmented_button_selected_hover_color="#5e0606",
    text_color="#ffffff"
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
inicio.configure(fg_color="#3f3f42")
inicio.configure(fg_color="#ffffff")

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
    fg_color="#1519DB",
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
    fg_color="#1519db",
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
    fg_color="#1519db",
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
    fg_color="#1519db",
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
    fg_color="#1519db",
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
    fg_color="#1519db",
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
    fg_color="#1519db",
    hover_color="#e40f0f",
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
    fg_color="#F0CDCD",
    corner_radius=0
)
frame_escroleable.grid(
    row=1,
    column=0,
    sticky="wes"
)
frame_ventas_arriba=CTkFrame(
    master=ventas,
    fg_color="#414141",    
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
    text_color="#ddc436",
    font=("Montserrat", 26),
)
item.grid(
    row=0,
    column=0,
    sticky="E"
)
lista_opciones = ["LAPTOP DELL", "LAPTOP HP", "LAPTOP XIAOMI","LAPTOP THINKERCARD"]
valor_menu_opciones = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_ventas_arriba,
    width=180,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_opciones,
    variable=valor_menu_opciones,
    
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=0,
    column=1,
    sticky="w"
)


ventana.mainloop()