from customtkinter import *

set_default_color_theme("dark-blue")
set_appearance_mode("light")

#=========================================================================================================
#VENTANA
#=========================================================================================================
ventana = CTk()
ventana.title("Sistema de Registro")
ventana.geometry("820x640")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
#=========================================================================================================
#COLORES
#=========================================================================================================
color_fondo= "#e3e5f3"
color_azul= "#4c3af5"
color_azul_2="#301ecf"
color_verde="#81dc00"
color_verde_2="#93e5a1"
color_blanco="#ffffff"
color_negro="#000000"
#=========================================================================================================
#BOTONES
#=========================================================================================================
estilo_botones={
    "width":220,
    "height":35,
    "fg_color":color_azul,
    "hover_color": color_verde,
    "text_color":color_blanco,
    "font":("Monteserrat", 16, "bold")}
#=========================================================================================================
#FRAME PRINCIPAL 
#=========================================================================================================
frame_principal= CTkFrame(master=ventana,
                          fg_color=color_fondo,
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=15)
frame_principal.grid_rowconfigure(0, weight=1)

#=========================================================================================================
#FRAME DERECHO 
#=========================================================================================================
frame_derecho=CTkFrame(master=frame_principal,
                       corner_radius=0,
                       fg_color=color_fondo)
frame_derecho.grid(row=0, column=1,sticky="nsew")
frame_derecho.grid_columnconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(1, weight=10)

frame_titulo= CTkFrame(master=frame_derecho,
                       corner_radius=0,
                       fg_color=color_azul)
frame_titulo.grid(row=0, column=0,sticky="nsew")
frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(0, weight=1)

titulo=CTkLabel(
    master=frame_titulo,
    fg_color=color_azul,
    text="AGENDA DE TAREAS",
    text_color=color_blanco,
    font=("Montserrat", 16, "bold"),
    justify="center"
)
titulo.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="nsew"
)

#=========================================================================================================
#FRAME DATOS 
#=========================================================================================================
frame_datos=CTkFrame(master=frame_derecho,
                     corner_radius=0,
                     fg_color=color_fondo)
frame_datos.grid(row=1,column=0,sticky="nswe")
frame_datos.grid_columnconfigure([0,1], weight=1)
for i in range (5):
    frame_datos.grid_rowconfigure(i, weight=1)
#=========================================================================================================
#FRAME IZQUIERDO 
#=========================================================================================================
frame_izquierdo= CTkFrame(master=frame_principal,
                          fg_color=color_azul,
                          corner_radius=0)
frame_izquierdo.grid(row=0, column=0, sticky= "nsew")

#=========================================================================================================
#BOTONES NAVEGACION
#=========================================================================================================
frame_botones=CTkFrame(master=frame_izquierdo,
                       corner_radius=0,
                       fg_color="transparent")
frame_botones.grid(row=1, column=0, pady=90)

frame_botones.grid_columnconfigure(0, weight=1)
frame_botones.grid_rowconfigure(0, weight=1)
frame_botones.grid_rowconfigure(1, weight=1)

boton_agendar_tarea= CTkButton(
    master=frame_botones,
    width=150,
    height=60,
    text="AGENDAR TAREA",
    anchor="center",
    font=("Montserrat", 16, "bold"),
    fg_color=color_azul_2,
    hover_color=color_verde
)

boton_agendar_tarea.grid(
    row=0,
    column=0,
    pady=10,
    padx=20,
)

boton_agenda= CTkButton(
    master=frame_botones,
    width=150,
    height=60,
    text="AGENDA",
    anchor="center",
    font=("Montserrat", 16,"bold"),
    fg_color=color_azul_2,
    hover_color=color_verde
)

boton_agenda.grid(
    row=1,
    column=0,
    pady=10,
    padx=20
)


ventana.mainloop()
