from customtkinter import *
COLOR_AMARILLO = "#ffcf03"

etiqueta_medio={
    "width":60,
    "height":30,
    "fg_color":COLOR_AMARILLO,
    "text_color":"#ffffff",
    "font":("Montserrat", 26)
    
  
}

cajas_de_texto={
    "width":180,
   
    "font":("Montserrat", 16)
}
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
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=0,pady=0)
frame_principal.grid_columnconfigure(0, weight=1)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)

frame_superior=CTkFrame(master=frame_principal,
                            corner_radius=0)
frame_superior.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)



frame_medio=CTkFrame(master=frame_principal,   
                            corner_radius=0)
frame_medio.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
frame_medio.grid_columnconfigure(0, weight=1)
frame_medio.grid_columnconfigure(1, weight=1)
frame_medio.grid_rowconfigure(0, weight=1)
frame_medio.grid_rowconfigure(1, weight=1)
frame_medio.grid_rowconfigure(2, weight=1)
frame_medio.grid_rowconfigure(3, weight=1)
frame_medio.grid_rowconfigure(4, weight=1)
frame_medio.grid_rowconfigure(5, weight=1)

frame_inferior=CTkFrame(master=frame_principal,
                            corner_radius=0)
frame_inferior.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1,weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)

#   Etiqueta - CTkLabel
etiqueta_nombre_cine = CTkLabel(
    master=frame_principal,
    fg_color="#143a81",
    text_color="#ffffff",
    text="CINE PYTHON JP",
    font=("Montserrat", 36),
)
etiqueta_nombre_cine.grid(
    row=0,
    column=0,
    sticky="ewns"
)

etiqueta_pelicula=CTkLabel(
    master=frame_medio,
    text="pelicula:",
    **etiqueta_medio
   
    )
etiqueta_pelicula.grid(
    row=0,
    column=0,
    sticky="ew"
)
etiqueta_horario=CTkLabel(
    master=frame_medio,
    text="HORARIO",
    **etiqueta_medio
    
)
etiqueta_horario.grid(
    row=1,
    column=0,
    sticky="ew"
)

etiqueta_boleto=CTkLabel(
    master=frame_medio,
    text="TIPO DEL BOLETO",
    **etiqueta_medio
)
etiqueta_boleto.grid(
    row=2,
    column=0,
    sticky="ew"
)
etiqueta_cantidad=CTkLabel(
    master=frame_medio,
    text="CANTIDAD",
    **etiqueta_medio
)
etiqueta_cantidad.grid(
    row=3,
    column=0,
    sticky="ew"
)
etiqueta_preciou=CTkLabel(
    master=frame_medio,
    text="PRECIO UNITARIO", 
    **etiqueta_medio
)
etiqueta_preciou.grid(
 row=4,
 column=0,
sticky="ew"    
)
etiqueta_total=CTkLabel(
    master=frame_medio,
    text="TOTAL",
    **etiqueta_medio,
)
etiqueta_total.grid(
    row=5,
    column=0,
    sticky="ew"
)

lista_de_peliculas = ["MICHAEL JACKSON", "MARIO BROS", "EL Diablo viste ala Moda 2","Mortal Kombat"]
valor_menu_opciones = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_medio,
    width=180,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_de_peliculas,
    variable=valor_menu_opciones,
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=0,
    column=1,
)
"""def cambio_horarios ():
    
    if lista_de_horarios=="MARIO BROS":
        print=(f"sus horarios son estos {lista_de_horariosMB}")
    """
    
    
    
    
    
    
    
lista_de_horarios = ["15:00 ", "16:30", "21:00","23:00"]
valor_menu_opciones = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_medio,
    width=180,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_de_horarios,
    variable=valor_menu_opciones,
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=1,
    column=1,
   
)

valor_botones_agrupados = StringVar(value=None)

botones_agrupados = CTkSegmentedButton(
    master=frame_medio,
    values=["Niño", "Vip", "Normal"],
    variable=valor_botones_agrupados,
    font=("Montserrat", 16),
    unselected_hover_color="#ffcf03",
    fg_color="#143a81",
    unselected_color="#143A81"
)

botones_agrupados.grid(
    row=2,
    column=1,
)


campo_texto_cantidad = CTkEntry(
    master=frame_medio,
    placeholder_text="Escriba la cantidad ",
    **cajas_de_texto
)

campo_texto_cantidad.grid(
    row=3,
    column=1,
)

campo_texto_precio =CTkEntry(
    master=frame_medio,
    placeholder_text="el valor es",
    **cajas_de_texto
    
)
campo_texto_precio.grid(
    row=4,
    column=1
)
campo_texto_precio = CTkEntry(
    master=frame_medio,
    placeholder_text="su total es",
    **cajas_de_texto
)
campo_texto_precio.grid(
    row=5,
    column=1
)

boton_1 = CTkButton(
    master=frame_inferior,
    width=80,
    height=30,
    corner_radius=0,
    text="Facturar",
    anchor="center",
    font=("Montserrat", 16),
    
)

boton_1.grid(
    row=0,
    column=0,
)



boton_2 = CTkButton(
    master=frame_inferior,
    width=80,
    height=30,
    corner_radius=0,
    text="Limpiar",
    anchor="center",
    font=("Montserrat", 16),
    
)

boton_2.grid(
    row=0,
    column=1,
)

ventana.mainloop()