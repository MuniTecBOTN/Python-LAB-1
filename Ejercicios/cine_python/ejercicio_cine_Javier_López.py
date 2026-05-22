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

frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_rowconfigure(0,weight=1)

# TITULO

texto_titulo = CTkLabel(
    master= frame_superior,
    text= "🎬 CINE PYTHON",
    font= ("Montserrat", 25,"bold"),
    fg_color=color_azul,
    text_color=color_blanco,
    
)

texto_titulo.grid(row=0, column=0)

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

lista_peliulas = ["MARIO BROS", "MICHAEL JACKSON"]
pelicula_seleccionada = StringVar(value="Seleccione una Opción")

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
    values=lista_peliulas,
    variable=pelicula_seleccionada,
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
    variable=horario_seleccionado,
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

# CANTIDAD etiqueta y cuadro de texto

etiqueta_cantidad = CTkLabel(master=frame_contenido,
                             text="CANIDAD:",
                             **estilo_etiquetas)

etiqueta_cantidad.grid(row=3, column=0, sticky="ew")

campo_cantdad = CTkEntry(master=frame_contenido,
                         **estilo_cuadro_texto)

campo_cantdad.grid(
    row=3, 
    column=1,
    sticky="ew"
    )



ventana.mainloop()