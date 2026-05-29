from customtkinter import *

set_default_color_theme("dark-blue")

#=================================================
#COLORES
#=================================================

color_fondo = "#e3e5f3"
color_azul = "#143a81"
color_amarillo = "#ffcf03"
color_verde = "#81dc00"
color_blanco = "#ffffff"
color_otro = "#0062ff"
color_tambien = "#008cff"
altura_campo = 45
tamaño_texto = 16

#=================================================
#ESTILOS
#=================================================

# ETIQUETAS

estilo_etiquetas ={
    "width":150,
    "height":altura_campo,
    "font":("Montserrat", 16,"bold"),
    "text_color":color_blanco,
    "fg_color":color_amarillo,
    "corner_radius":0
}

# BOTONES

estilo_botones = {
    "width": 120,
    "height": altura_campo,
    "corner_radius": 0,
    "fg_color": color_azul,
    "hover_color": color_amarillo,
    "text_color": color_blanco,
    "font": ("Montserrat", 16, "bold")
}

estilo_boton_spinbox = {
    "width": 180,
    "height": altura_campo,
    "corner_radius": 0,
    "fg_color": color_azul,
    "hover_color": color_amarillo,
    "text_color": color_blanco,
    "font": ("Montserrat", 16, "bold")
}

#CUADRO DE TEXTO

estilo_cuadro_texto = {
"width":400,
"height": altura_campo,
"corner_radius":0,
"fg_color":color_blanco,
"justify":"center",
"border_color":color_blanco,
"font":("Montserrat", 16, "bold")}

#=================================================
# FUNCIONES
#=================================================

def decrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    if cantidad_actual > 0:
        cantidad_boletos.set(cantidad_actual - 1)
    calcular_total()
        
def incrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    cantidad_boletos.set(cantidad_actual + 1)
    calcular_total()

    
def pelicula_seleccionada(nombre_pelicula):
    horarios = peliculas.get(nombre_pelicula, [])
    menu_horario.configure(values=horarios)
    menu_horario.set("Seleccione una Opción")
    calcular_total()

def calcular_precio_unitario(tipo_boleto):
    precio_boleto.set(boletos_precio.get(tipo_boleto, 0))
    calcular_total()

def calcular_total():
    total=cantidad_boletos.get()*precio_boleto.get()
    total_calculado.set(total)

def boton_limpiar():
    menu_peliculas.set(value="Seleccione una Opción")
    menu_horario.configure(values=["Seleccione una Opción"])
    opcion_seleccionada_menu_horario.set("Seleccione una Opción")
    pelicula.set("Seleccione una Opción")
    valor_botones_agrupados.set(value=None)
    cantidad_boletos.set(value=0)
    precio_boleto.set(value=0)
    total_calculado.set(value=0)

#=================================================
# DICCIONARIOS
#=================================================

peliculas = {
    "El Origen": ["14:00-16:30", "19:00-21:30"],
    "Matrix": ["15:00-17:30", "20:00-22:30"],
    "Inception": ["16:00-18:30", "21:00-23:30"],
    "Interstellar": ["17:00-19:30", "22:00-00:30"],
    "Michael Jackson: This Is It": ["18:00-20:30", "23:00-01:30"],
    "Mario Bros.": ["19:00-21:30", "00:00-02:30"],
    "El Conjuro": ["20:00-22:30", "01:00-03:30"],
}

boletos_precio = {
    "NIÑO": 35,
    "NORMAL": 45,
    "VIP": 90,
}


#=================================================
# VENTANA
#=================================================

ventana = CTk()
ventana.title("CINE PYTHON")
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
frame_principal.grid_rowconfigure(0,weight=2)
frame_principal.grid_rowconfigure(1,weight=5)
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

lista_peliculas = list(peliculas.keys())
pelicula = StringVar(value="Seleccione una Opción")

menu_peliculas = CTkOptionMenu(
    master=frame_contenido,
    width=200,
    height=altura_campo,
    fg_color=color_blanco,
    text_color=color_azul,
    button_color=color_amarillo,
    dropdown_fg_color=color_amarillo,
    dropdown_text_color=color_blanco,
    dropdown_font=("Monstserat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_peliculas,
    variable=pelicula,
    font=("Montserrat", 16),
    command=pelicula_seleccionada,
)

menu_peliculas.grid(row=0,column=1,sticky="ew")

#HORARIO etiqueta y menu de opciones

etiqueta_horario = CTkLabel(
    master=frame_contenido,
    text="HORARIO:",
    **estilo_etiquetas,
    )

etiqueta_horario.grid(
    row=1, 
    column=0,
    sticky="ew"
    )


opcion_seleccionada_menu_horario = StringVar(value="Seleccione una Opción")

menu_horario = CTkOptionMenu(
    master=frame_contenido,
    width=200,
    values=["Seleccione una Opción"],
    height=altura_campo,
    fg_color=color_blanco,
    text_color=color_azul,
    button_color=color_amarillo,
    dropdown_fg_color=color_amarillo,
    dropdown_text_color=color_blanco,
    dropdown_font=("Monstserat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    variable=opcion_seleccionada_menu_horario,
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

tipos_de_boletos= list(boletos_precio.keys())
botones_agrupados_boleto = CTkSegmentedButton(
    master=frame_contenido,
    height=altura_campo,
    values=tipos_de_boletos,
    variable=valor_botones_agrupados,
    font=("Montserrat", 16),
    fg_color=color_azul,
    corner_radius=0,
    text_color=color_blanco,
    unselected_color=color_azul,
    selected_color=color_amarillo,
    unselected_hover_color=color_otro,
    command=calcular_precio_unitario,
)

botones_agrupados_boleto.set("NORMAL", 0)

botones_agrupados_boleto.grid(
    row=2,
    column=1,
    sticky="ew"
    )

ventana.after(
    100,
    lambda: [boton.configure(width=100) for boton in botones_agrupados_boleto._buttons_dict.values()]
)

# CANTIDAD etiqueta y cuadro de texto

etiqueta_cantidad = CTkLabel(
    master=frame_contenido,
    text="CANIDAD:",
    **estilo_etiquetas)

etiqueta_cantidad.grid(row=3, column=0, sticky="ew")

#frame spinbox

frame_spinbox = CTkFrame(
    master=frame_contenido,
    fg_color="transparent",
    corner_radius=0
)

frame_spinbox.grid(
    row=3,
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
    command=decrementar_boletos,
    )

boton_restar.grid(
    row=0,
    column=0,
    sticky="nsew"
    )

#texto spinbox

cantidad_boletos = IntVar(value=0)

campo_cantidad = CTkEntry(
    master=frame_spinbox,
    state="readonly",
    width= 180,
    height= altura_campo,
    corner_radius= 0,
    fg_color= color_blanco,
    justify= "center",
    border_color= color_blanco,
    textvariable=cantidad_boletos,
    font= ("Montserrat", 16, "bold"))

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
    command= incrementar_boletos,
    )

boton_sumar.grid(
    row=0,
    column=2,
    sticky="nsew"
    )


# PRECIO etiqueta y cuadro de texto

etiqueta_precio = CTkLabel(
    master=frame_contenido,
    text="PRECIO UNITARIO:",
    **estilo_etiquetas)

etiqueta_precio.grid(row=4, column=0, sticky="ew")

precio_boleto = IntVar(value=0)
precio_boleto.set(boletos_precio.get("NORMAL", 0))

campo_precio = CTkEntry(
    master=frame_contenido,
    state="readonly",
    textvariable=precio_boleto,
    **estilo_cuadro_texto)

campo_precio.grid(
    row=4, 
    column=1,
    sticky="ew"
    )

# TOTAL etiqueta y cuadro de texto

etiqueta_total = CTkLabel(
    master=frame_contenido,
    text="TOTAL:",
    **estilo_etiquetas)

etiqueta_total.grid(row=5, column=0, sticky="ew")

total_calculado = IntVar(value=0)

campo_total = CTkEntry(
    master=frame_contenido,
    state="readonly",
    **estilo_cuadro_texto,
    textvariable=total_calculado
    )


campo_total.grid(
    row=5, 
    column=1,
    sticky="ew"
    )

#=================================================
# FRAME INFERIOR
#=================================================

frame_inferior = CTkFrame(
    master=frame_principal,
    fg_color=color_azul,
    corner_radius=0,
    )

frame_inferior.grid(
    row=2,
    column=0,
    sticky="nsew"
    )

frame_inferior.grid_columnconfigure(0,weight=1)
frame_inferior.grid_columnconfigure(1,weight=1)
frame_inferior.grid_rowconfigure(0,weight=1)


#BOTONES

boton_calcular = CTkButton(
    master=frame_inferior,
    text="CALCULAR",
    **estilo_botones,
    )

boton_calcular.grid(
    row=0,
    column=0,
    sticky="nsew"
    )

boton_limpiar = CTkButton(
    master=frame_inferior,
    text="LIMPIAR",
    **estilo_botones,
    command=boton_limpiar
    )

boton_limpiar.grid(
    row=0,
    column=1,
    sticky="nsew"
    )


ventana.mainloop()

#py -m PyInstaller --noconfirm --onedir --windowed "C:/Users/CC2Z03/Desktop/ejercicio_cine_javier_lópez_3.py"

