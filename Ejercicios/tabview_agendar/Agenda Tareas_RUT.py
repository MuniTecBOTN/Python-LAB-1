from customtkinter import *

set_default_color_theme("dark-blue")
set_appearance_mode("light")

#=========================================================================================================
#VENTANA
#=========================================================================================================
ventana = CTk()
ventana.title("Agenda de Tareas")
ventana.geometry("820x640")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
#=========================================================================================================
#COLORES
#=========================================================================================================
color_fondo= "#e3e5f3"
color_azul= "#4c3af5"
color_azul_2="#5243d6"
color_verde="#81dc00"
color_verde_2="#93e5a1"
color_blanco="#ffffff"
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
frame_principal.grid_columnconfigure(0, weight=5)
frame_principal.grid_columnconfigure(1, weight=15)
frame_principal.grid_rowconfigure(0, weight=1)
#=========================================================================================================
#FRAME IZQUIERDO 
#=========================================================================================================
frame_izquierdo= CTkFrame(master=frame_principal,
                          fg_color=color_azul,
                          corner_radius=0)
frame_izquierdo.grid(row=0, column=0, sticky= "nsew")

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
frame_datos.grid_columnconfigure(0, weight=1)
for i in range (3):
    frame_datos.grid_rowconfigure(0, weight=5)

etiqueta_nombre= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="NOMBRE:",
                          justify="center",
                          font=("Montserrat", 16, "bold"),
                          text_color=color_blanco,
                          fg_color=color_verde
                          )
etiqueta_nombre.grid( row=0, 
                     column=0, 
                     sticky="e",
                     padx=0,
                     pady=10)
campo_nombre = CTkEntry(
    master=frame_datos,
    width=200,
    height=55,
    border_color="#e3e5f3",
    text_color="#2a00ac",
    corner_radius=0,
    justify="center",
    placeholder_text="...",
    font=("Montserrat", 16),
)
campo_nombre.grid(row=0,column=1, sticky="w", padx=10)

etiqueta_descripcion= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="DESCRIPCION:",
                          font=("Montserrat", 16, "bold"),
                          text_color=color_blanco,
                          fg_color=color_verde
                          )
etiqueta_descripcion.grid( row=1, 
                          column=0, 
                          sticky="ew",
                          padx=10)

etiqueta_fecha= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="NOMBRE:",
                          font=("Montserrat", 16, "bold"),
                          text_color=color_blanco,
                          fg_color=color_verde
                          )
etiqueta_fecha.grid(row=2, 
                    column=0, 
                    sticky="w",
                    padx=10,
                    pady=20)


ventana.mainloop()