from customtkinter import *

set_default_color_theme("dark-blue")

#=================================================
#COLORES
#=================================================

color_fondo = "#e3e5f3"
color_azul = "#143a81"
color_verde = "#81dc00"
color_blanco = "#ffffff"
color_otro = "#0062ff"
color_tambien = "#008cff"
color_amarillo = "#ffcf03"


#=================================================
#ESTILOS
#=================================================

# ETIQUETAS

estilo_etiquetas ={
    "width":150,
    "height":30,
    "font":("Montserrat", 16,"bold"),
    "text_color":color_blanco,
    "fg_color":color_amarillo,
    "corner_radius":0
}

# BOTONES

estilo_botones = {
    "width": 120,
    "height": 35,
    "corner_radius": 0,
    "fg_color": color_azul,
    "hover_color": color_amarillo,
    "text_color": color_blanco,
    "font": ("Montserrat", 16, "bold")
}

#CUADRO DE TEXTO

estilo_cuadro_texto = {
"width":400,
"corner_radius":0,
"fg_color":color_blanco,
"justify":"center",
"border_color":color_blanco,
"font":("Montserrat", 16, "bold")}



def funcion_disminuir():
   cantidad_actual=cantidad_boletos.get()
   if cantidad_actual>0:
       cantidad_boletos.set(cantidad_actual-1) 

def funcion_aumentar():
   cantidad_actual=cantidad_boletos.get()
   cantidad_boletos.set(cantidad_actual+1)
   
def pelicula_seleccionada(valor):
    menu_peliculas=pelicula.get()
    print(f"pelicula seleccionada:{menu_peliculas}")
    menu_horario.configure(values =peliculas[valor])

peliculas = {
    "Avatar": ["13:00-15:45", "18:00-20:45"],
    "Titanic": ["14:30-17:15", "21:00-23:45"],
    "Avengers: Endgame": ["15:00-18:00", "19:30-22:30"],
    "Jurassic Park": ["16:00-18:30", "20:00-22:30"],
    "Spider-Man: No Way Home": ["17:00-19:45", "22:00-00:45"],
    "The Batman": ["18:00-20:50", "23:00-01:50"],
    "Doctor Strange": ["19:00-21:30", "00:00-02:30"],
    "Toy Story": ["12:00-14:00", "16:00-18:00"],
    "Rapidos y Furiosos": ["20:00-22:20", "01:00-03:20"],
    "John Wick": ["21:00-23:10", "02:00-04:10"],
}
#=================================================
# VENTANA
#=================================================

ventana = CTk()
ventana.title("AGENDA")
ventana.geometry("800x600")

ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)

#=================================================
# FRAME PRINCIPAL
#=================================================

frame_principal = CTkFrame(
    master=ventana,
    fg_color=color_fondo,
    corner_radius=0
    )

frame_principal.grid(
    row=0,
    column=0,
    sticky="snew",
    padx=10,
    pady=10
    )

frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_rowconfigure(1,weight=1)
frame_principal.grid_rowconfigure(2,weight=1)

#=================================================
# FRAME SPERIOR
#=================================================

frame_superior = CTkFrame(
    master=frame_principal,
    fg_color=color_azul,
    corner_radius=0,
    )

frame_superior.grid(
    row=0,
    column=0,
    pady=10,
    sticky="nsew"
    )
frame_superior.grid_columnconfigure(0,weight=1)
frame_superior.grid_rowconfigure(0,weight=1)

frame_inferior=CTkFrame(
    master=frame_principal,
    fg_color=color_azul,
    corner_radius=0
)


frame_inferior.grid(
    row=2,
    column=0,
   
    sticky="nsew"
)

frame_inferior.grid_columnconfigure(0,weight=1)
frame_inferior.grid_columnconfigure(1,weight=1)
frame_inferior.grid_rowconfigure(0,weight=1)


frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_rowconfigure(0,weight=1)

# TITULO

texto_titulo = CTkLabel(
    master= frame_superior,
    text= "🎬 CINE PYTHON",
    font= ("Montserrat", 25,"bold"),
    fg_color=color_azul,
    text_color=color_blanco,
    justify="center"
    
)

texto_titulo.grid(row=0, column=0,sticky="nsew")

#=================================================
# FRAME CONTENIDO
#=================================================
frame_contenido = CTkFrame(
    master=frame_principal,
    fg_color=color_fondo,
    corner_radius=0
    )

frame_contenido.grid(
    row=1,
    column=0,
    sticky="nsew")

frame_contenido.grid_columnconfigure([0,1],weight=1)
frame_contenido.grid_rowconfigure([0,1,2,3,4,5],weight=1)

#PELICULA etiqueta y menu de opciones

etiqueta_pelicula = CTkLabel(
    master=frame_contenido,
    text="PLICULA:",
    **estilo_etiquetas
    )

etiqueta_pelicula.grid(
    row=0,
    column=0,
    sticky="ew"
    )

lista_peliculas = list(peliculas.keys())
pelicula = StringVar(value="Seleccione una Opción")

menu_peliculas = CTkOptionMenu(
    master=frame_contenido,
    width=200,
    height=30,
    fg_color=color_blanco,
    text_color=color_azul,
    button_color=color_amarillo,
    dropdown_fg_color=color_amarillo,
    dropdown_text_color=color_blanco,
    dropdown_font=("Monstserat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_peliculas,
    command=pelicula_seleccionada,
    variable=pelicula,
    font=("Montserrat", 16),
)

menu_peliculas.grid(row=0,column=1,sticky="ew")

#HORARIO etiqueta y menu de opciones

etiqueta_horario = CTkLabel(
    master=frame_contenido,
    text="HORARIO:",
    **estilo_etiquetas
    )

etiqueta_horario.grid(
    row=1, 
    column=0,
    sticky="ew"
    )

lista_horario = ["15:00 - 17:00", "17:00 - 19:00"]
horario_seleccionado = StringVar(value="Seleccione una Opción")

menu_horario = CTkOptionMenu(
    master=frame_contenido,
    width=200,
    height=30,
    fg_color=color_blanco,
    text_color=color_azul,
    button_color=color_amarillo,
    dropdown_fg_color=color_amarillo,
    dropdown_text_color=color_blanco,
    dropdown_font=("Monstserat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_horario,
    
    font=("Montserrat", 16),
)

menu_horario.grid(
    row=1,
    column=1,
    sticky="ew"
    )

# TIPO DE BOLETO etiqueta y botones

etiqueta_boleto = CTkLabel(
    master=frame_contenido,
    text="TIPO DE BOLETO:",
    **estilo_etiquetas
    )

etiqueta_boleto.grid(
    row=2,
    column=0,
    sticky="ew"
    )

valor_botones_agrupados = StringVar(value=None)

botones_tipo_boleto = CTkSegmentedButton(
    master=frame_contenido,
    values=["NIÑO", "VIP", "NORMAL"],
    variable=valor_botones_agrupados,
    font=("Montserrat", 16),
    fg_color=color_fondo,
    text_color=color_blanco,
    unselected_color=color_azul,
    selected_color=color_amarillo,
    unselected_hover_color=color_otro
    
)

botones_tipo_boleto.grid(
    row=2,
    column=1,
    sticky="ew"
    )



etiqueta_cantidad = CTkLabel(
    master=frame_contenido,
    text="CANTIDAD:",
    **estilo_etiquetas)

etiqueta_cantidad.grid(
    row=3, 
    column=0, 
    sticky="ew")

frame_spinbox=CTkFrame(
    master=frame_contenido,
    fg_color=color_fondo

)
frame_spinbox.grid(
    row=3,
    column=1,
    sticky="nsew"
)
frame_spinbox.grid_columnconfigure([0,1,2],weight=1)
frame_spinbox.grid_rowconfigure(0,weight=1)

boton_disminuir=CTkButton(
    master=frame_spinbox,
    width=80,
    height=30,
    corner_radius=0,
    text="-",
    anchor="center",
    font=("Montserrat",16),
    command=funcion_disminuir
)

boton_disminuir.grid(
    row=0,
    column=0,
    sticky="e",
    padx=2
)
#   Caja de texto - CTkTextBox
cantidad_boletos=IntVar(value=0)
caja_cantidad = CTkEntry(
    master=frame_spinbox,
    width=80,
    height=30,
    state="readonly",
    fg_color="#afaaaa",
    corner_radius=0,
    
    textvariable=cantidad_boletos,
    font=("Montserrat", 16),
   
)
caja_cantidad.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=2
)


boton_aumentar=CTkButton(
    master=frame_spinbox,
    width=80,
    height=30,
    corner_radius=0,
    text="+",
    anchor="center",
    font=("Montserrat",16),
    command=funcion_aumentar
)

boton_aumentar.grid(
    row=0,
    column=2,
    sticky="w",
    padx=2
)






etiqueta_preciou = CTkLabel(
    master=frame_contenido,
    text="PRECIO UNITARIO:",
    **estilo_etiquetas
    )

etiqueta_preciou.grid(
    row=4, 
    column=0, 
    sticky="ew")

campo_preciou = CTkEntry(
    master=frame_contenido,
    
    state="readonly",
    **estilo_cuadro_texto)

campo_preciou.grid(
    row=4,
    column=1,
    sticky="ew"
)
etiqueta_total=CTkLabel(master=frame_contenido,
                        text ="TOTAL",
                         **estilo_etiquetas)
etiqueta_total.grid(row=5,column=0,sticky="ew")

campo_total=CTkEntry(master=frame_contenido,
                      state="readonly",
                     **estilo_cuadro_texto)
campo_total.grid(
    row=5,
    column=1,
    sticky="ew"
)
def funcion_calcular():
    print(f"Has presionado el Botón 1")


boton_calcular = CTkButton(
    master=frame_inferior,
    width=80,
    height=30,
    corner_radius=0,
    text="CALCULAR",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_calcular,
)

boton_calcular.grid(
    row=0,
    column=0,
)


def funcion_limpiar():
    pelicula_seleccionada
    horario_seleccionado
    botones_tipo_boleto.set("NORMAL"),
    campo_preciou.delete(0,END),
    campo_total.delete(0,END)


boton_limpiar=CTkButton(
    master=frame_inferior,
    width=80,
    height=30,
    corner_radius=0,
    text="LIMPIAR",
    anchor="center",
    font=("Montserrat",16),
    command=funcion_limpiar
)

boton_limpiar.grid(
    row=0,
    column=1,
)



ventana.mainloop()