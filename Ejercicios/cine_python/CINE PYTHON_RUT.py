from customtkinter import *

set_default_color_theme("dark-blue")
set_appearance_mode("light")

#==========================================================================================
# VENTANA
#==========================================================================================
ventana = CTk()
ventana.title("CINE")
ventana.geometry("520x700")
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
#==========================================================================================
#ATAJOS 
#==========================================================================================
estilo_botones={
    "width":150,
    "height":60,
    "fg_color":color_azul,
    "hover_color": color_azul_2,
    "text_color":color_blanco,
    "font":("Monteserrat", 16, "bold")}

estilo_etiquetas={"width":150, 
                  "height":40,
                  "justify":"center",
                  "text_color":color_blanco,
                  }

estilo_campo_texto={"width":250,
                    "height":40,
                    "border_color":color_blanco,
                    "fg_color":color_blanco,
                    "text_color":color_negro,
                    "corner_radius":0,
                    "justify":"center",
                    "placeholder_text":"...",
                    "font":("Montserrat", 16)}

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
                         text="CINE PYTHON",
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
                    pady=20)
frame_opciones.grid_columnconfigure([0,1], weight=1)
for i in range(5):
    frame_opciones.grid_rowconfigure(i, weight=1)

#==========================================================================================
# ETIQUETAS
#==========================================================================================
etiqueta_pelicula=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="PELÍCULA",
                           fg_color=color_amarillo)
etiqueta_pelicula.grid(row=0, 
                       column=0,
                       sticky="e")

etiqueta_horario=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="HORARIO",
                           fg_color=color_amarillo)
etiqueta_horario.grid(row=1, 
                      column=0, 
                      sticky="ne", 
                      pady=5)

etiqueta_tipo=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="TIPO BOLETO",
                           fg_color=color_amarillo)
etiqueta_tipo.grid(row=2, 
                   column=0, 
                   sticky="ne", 
                   pady=5)

etiqueta_cantidad=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="CANTIDAD",
                           fg_color=color_amarillo)
etiqueta_cantidad.grid(row=3, 
                       column=0, 
                       sticky="ne", 
                       pady=5)

etiqueta_precio=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="PRECIO UNITARIO",
                           fg_color=color_amarillo)
etiqueta_precio.grid(row=4, 
                     column=0, 
                     sticky="ne", 
                     pady=5)

etiqueta_total=CTkLabel(master=frame_opciones,
                           **estilo_etiquetas,
                           text="TOTAL",
                           fg_color=color_amarillo)
etiqueta_total.grid(row=5, 
                    column=0,sticky="ne", 
                    pady=5)

#==========================================================================================
# DATOS
#==========================================================================================
lista_peliculas=["Super Mario Galaxy", "El diablo viste a la moda 2", "Michel", "En la Zona Gris", "TXT in Japan:Live Viewing"]
pelicula_seleccionada= StringVar(value="Seleccione una pelicula")
menu_peliculas=CTkOptionMenu(master=frame_opciones,
                             corner_radius=0,
                             fg_color=color_blanco,
                             width=250,
                             height=40,
                             dynamic_resizing=False,
                             values=lista_peliculas,
                             variable=pelicula_seleccionada,
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
                    sticky="w")

lista_horarios=["8:00","12:00","13:30","15:00","16:30","17:00","18:30"]
horario_seleccionado= StringVar(value="Seleccione un horario")
menu_horarios=CTkOptionMenu(master=frame_opciones,
                             corner_radius=0,
                             fg_color=color_blanco,
                             width=250,
                             height=40,
                             dynamic_resizing=False,
                             values=lista_horarios,
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
                   sticky="wn", 
                   pady=5)

boleto_seleccionado = StringVar(value=None)

botones_agrupados = CTkSegmentedButton(
    master=frame_opciones,
    width=250,
    height=40,
    values=["NIÑO", "VIP", "NORMAL"],
    variable=boleto_seleccionado,
    font=("Montserrat", 16,"bold"),
    fg_color=color_azul,
    unselected_color=color_azul,
    unselected_hover_color=color_azul,
    selected_hover_color=color_amarillo,
    selected_color=color_amarillo, 
    text_color=color_blanco
)

botones_agrupados.grid(
    row=2,
    column=1,
    sticky="wn",
    pady=5
)




#==========================================================================================
# FRAME BOTONES
#==========================================================================================
frame_botones=CTkFrame(master=frame_principal,
                       corner_radius=0,
                       fg_color=color_fondo)
frame_botones.grid(row=2, column=0)
frame_botones.grid_columnconfigure([0,1], weight=1)
frame_botones.grid_rowconfigure(0,weight=1)

boton_facturar=CTkButton(master=frame_botones,
                         **estilo_botones,
                         text="FACTURAR")
boton_facturar.grid(row=0, column=0,sticky="w", padx=10)

boton_limpiar=CTkButton(master=frame_botones,
                         **estilo_botones,
                         text="LIMPIAR")
boton_limpiar.grid(row=0, column=1,sticky="e", padx=10)

#==========================================================================================
# 
#==========================================================================================

ventana.mainloop()