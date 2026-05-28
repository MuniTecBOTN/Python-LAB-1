from customtkinter import *

set_default_color_theme("dark-blue")
set_appearance_mode("light")

#==========================================================================================
# VENTANA
#==========================================================================================
ventana = CTk()
ventana.title("CINE")
ventana.geometry("720x600")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

#=========================================================================================================
#COLORES
#=========================================================================================================
color_fondo= "#e3e5f3"
color_azul= "#143a81"
color_azul_2="#4a71b9"
color_amarillo="#FFCF03"
color_amarillo_2="#F0DA78"
color_blanco="#FFFFFF"
color_negro="#000000"
transparente="transparent"
altura_estandar_campo=55
tamaño_letra_normal=16
estilo_letra=("Montserrat", tamaño_letra_normal, "bold")
#==========================================================================================
#ATAJOS 
#==========================================================================================
estilo_botones={
    "width":120,
    "height":altura_estandar_campo,
    "fg_color":color_azul,
    "hover_color": color_azul_2,
    "text_color":color_blanco,
    "font":("Monteserrat", 16, "bold")}

estilo_etiquetas={"width":150, 
                  "height":altura_estandar_campo,
                  "justify":"center",
                  "corner_radius":0,
                  "text_color":color_blanco,
                  }

estilo_campo_texto={"width":150,
                    "height":altura_estandar_campo,
                    "border_color":color_blanco,
                    "fg_color":color_blanco,
                    "text_color":color_negro,
                    "corner_radius":0,
                    "justify":"center",
                    "placeholder_text":"",
                    "font":("Montserrat", 16, "bold"),}

#==========================================================================================
# DEFINICIONES
#==========================================================================================
def decrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    if cantidad_actual>0:
        cantidad_boletos.set(cantidad_actual-1)
        
def incrementar_boletos():
    cantidad_actual = cantidad_boletos.get()
    cantidad_boletos.set(cantidad_actual+1)
    
def pelicula_seleccionada(valor):
    nombre_pelicula=pelicula.get()
    #print(f "Pelicula Seleccionada":{nombre_pelicula}")
    menu_peliculas.configure(values=peliculas[valor])
       
def limpiar():
    cantidad_boletos.set(0)
    pelicula.set("Seleccione una pelicula")
    horario_seleccionado.set("Seleccione un horario")
    boleto_seleccionado.set(None)
    

peliculas={"Super Mario Galaxy":["14:15-16:00", "16:45-17:30", "19:00-20:15"],
           "El diablo viste a la moda 2": ["13:00-14:55", "15:30-17:00", "18:15-19:30", "21:00-22:10"],
           "Michel": ["14:00-15:20", "17:15-18:15", "20:30-22:00"],
           "En la Zona Gris": ["16:00-17:45", "19:30", "22:15"],
           "BTS World Tour ARIRANG In Busan: Live": ["1:00-4:30", "15:00-18:30"]
}
    
#==========================================================================================
# FRAME PRINCIPAL
#==========================================================================================
frame_principal= CTkFrame(master=ventana,
                          fg_color=color_fondo,
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=10)
frame_principal.grid_rowconfigure(1, weight=25)
frame_principal.grid_rowconfigure(2, weight=5)


#==========================================================================================
# FRAME TITULO
#==========================================================================================
frame_titulo=CTkFrame(master=frame_principal,
                      corner_radius=0,
                      fg_color=color_azul,
                      )
frame_titulo.grid(row=0, column=0,sticky="nsew")
frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(0, weight=1)

etiqueta_titulo=CTkLabel(master=frame_titulo,
                         **estilo_etiquetas,
                         fg_color=color_azul,
                         text="🎬 CINE PYTHON",
                         font=("Montserrat",20, "bold"),)
etiqueta_titulo.grid(row=0, column=0)


#==========================================================================================
# FRAME OPCIONES
#==========================================================================================
frame_opciones=CTkFrame(master=frame_principal,
                        corner_radius=0,
                        fg_color=color_fondo)
frame_opciones.grid(row=1, 
                    column=0, 
                    sticky="nsew", 
                    padx=10,
                    pady=5)
frame_opciones.grid_columnconfigure([0,1], weight=1)
for i in range(6):
    frame_opciones.grid_rowconfigure(i, weight=1)

#==========================================================================================
# ETIQUETAS
#==========================================================================================
etiqueta_pelicula=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="PELÍCULA",
                           fg_color=color_amarillo,
                           font=estilo_letra)
etiqueta_pelicula.grid(row=0, 
                       column=0,
                       sticky="we")

etiqueta_horario=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="HORARIO",
                           fg_color=color_amarillo,
                           font=estilo_letra)
etiqueta_horario.grid(row=1, 
                      column=0, 
                      sticky="nwe", 
                      pady=5)

etiqueta_tipo=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="TIPO BOLETO",
                           fg_color=color_amarillo,
                           font=estilo_letra)
etiqueta_tipo.grid(row=2, 
                   column=0, 
                   sticky="nwe", 
                   pady=5)

etiqueta_cantidad=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="CANTIDAD",
                           fg_color=color_amarillo,
                           font=estilo_letra)
etiqueta_cantidad.grid(row=3, 
                       column=0, 
                       sticky="nwe", 
                       pady=5)

etiqueta_precio=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="PRECIO UNITARIO",
                           fg_color=color_amarillo,
                           font=estilo_letra)
etiqueta_precio.grid(row=4, 
                     column=0, 
                     sticky="nwe", 
                     pady=5)

etiqueta_total=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="TOTAL",
                           fg_color=color_amarillo,
                           font=estilo_letra)
etiqueta_total.grid(row=5, 
                    column=0,sticky="nwe", 
                    pady=5)

#==========================================================================================
# DATOS
#==========================================================================================
lista_peliculas=list(peliculas.keys())
pelicula= StringVar(value="Seleccione una pelicula")
menu_peliculas=CTkOptionMenu(master=frame_opciones,
                             corner_radius=0,
                             fg_color=color_blanco,
                             width=250,
                             height=altura_estandar_campo,
                             dynamic_resizing=False,
                             values=lista_peliculas,
                             variable=pelicula,
                             command=pelicula_seleccionada,
                             anchor="center",
                             text_color=color_azul,
                             button_color=color_amarillo,
                             button_hover_color=color_amarillo_2,
                             dropdown_fg_color=color_amarillo,
                             dropdown_hover_color=color_azul_2,
                             dropdown_text_color=color_blanco,
                             dropdown_font=("Montserrat",16, "bold"),
                             font=("Montserrat", 16, "bold")
                             )
menu_peliculas.grid(row=0,
                    column=1,
                    sticky="ew")

horario_seleccionado= StringVar(value="Seleccione un horario")
menu_horarios=CTkOptionMenu(master=frame_opciones,
                             corner_radius=0,
                             fg_color=color_blanco,
                             width=250,
                             height=altura_estandar_campo,
                             dynamic_resizing=False,
                             variable=horario_seleccionado,
                             text_color=color_azul,
                             anchor="center",
                             button_color=color_amarillo,
                             button_hover_color=color_amarillo_2,
                             dropdown_fg_color=color_amarillo,
                             dropdown_hover_color=color_azul_2,
                             dropdown_text_color=color_negro,
                             dropdown_font=("Montserrat",16, "bold"),
                             font=("Montserrat", 16, "bold")
                             )
menu_horarios.grid(row=1,
                   column=1,
                   sticky="wen", 
                   pady=5)

boleto_seleccionado = StringVar(value=None)

botones_agrupados = CTkSegmentedButton(
    master=frame_opciones,
    width=250,
    height=altura_estandar_campo,
    values=["NIÑO", "VIP", "NORMAL"],
    variable=boleto_seleccionado,
    font=("Montserrat", 16,"bold"),
    fg_color=color_azul,
    unselected_color=color_azul,
    unselected_hover_color=color_azul,
    selected_hover_color=color_amarillo,
    selected_color=color_amarillo, 
    text_color=color_blanco,
    corner_radius=0
)

botones_agrupados.grid(
    row=2,
    column=1,
    sticky="wen",
    pady=5
)

#==========================================================================================
#CAMPOS TEXTO
#==========================================================================================
campo_precio=CTkEntry(master=frame_opciones,
                         **estilo_campo_texto,
                         state="readonly")
campo_precio.grid(row=4,
                  column=1,
                  sticky="ewn",
                  pady=5
                  )
campo_total=CTkEntry(master=frame_opciones,
                         **estilo_campo_texto,
                         state="readonly")
campo_total.grid(row=5,
                  column=1,
                  sticky="enw",
                  pady=5
                  )

#==========================================================================================
# FRAME CANTIDAD
#==========================================================================================
frame_cantidad=CTkFrame(master=frame_opciones,
                        corner_radius=0,
                        fg_color=transparente)
frame_cantidad.grid(row=3, column=1, sticky="enw")
frame_cantidad.grid_rowconfigure(0, weight=1)
frame_cantidad.grid_columnconfigure(0, weight=1)
frame_cantidad.grid_columnconfigure(1, weight=1)
frame_cantidad.grid_columnconfigure(2, weight=1)

boton_decrementar=CTkButton(master=frame_cantidad,
                      corner_radius=0,
                      fg_color=color_azul,
                      height=altura_estandar_campo,
                      width=120,
                      text="-",
                      hover_color= color_azul_2,
                      text_color=color_blanco,
                      command=decrementar_boletos,
                      font=("Monteserrat", 16, "bold"))
boton_decrementar.grid(row=0, column=0, sticky="nwe", pady=5)
boton_incrementar=CTkButton(master=frame_cantidad,
                      corner_radius=0,
                      fg_color=color_azul,
                      height=altura_estandar_campo,
                      width=120,
                      text="+",
                      command=incrementar_boletos,
                      hover_color= color_azul_2,
                      text_color=color_blanco,
                      font=("Monteserrat", 16, "bold"),
                    )
boton_incrementar.grid(row=0, column=2,sticky="nwe", pady=5)

cantidad_boletos=IntVar(value=0)
campo_cantidad= CTkEntry(master=frame_cantidad,
                         **estilo_campo_texto,
                         state="readonly",
                         textvariable=cantidad_boletos)
campo_cantidad.grid(row=0, column=1, sticky="nwe",pady=5)


#==========================================================================================
#BOTONES FINALES
#==========================================================================================
boton_facturar=CTkButton(master=frame_opciones,
                         **estilo_botones,
                         text="FACTURAR", 
                         corner_radius=0)
boton_facturar.grid(row=6, column=0,sticky="wse")

boton_limpiar=CTkButton(master=frame_opciones,
                         **estilo_botones,
                         text="LIMPIAR", 
                         corner_radius=0,
                         command=limpiar)
boton_limpiar.grid(row=6, column=1,sticky="esw",)

#==========================================================================================
# 
#==========================================================================================



ventana.mainloop()
