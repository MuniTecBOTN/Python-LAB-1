from customtkinter import *

color_fondo= "#e3e5f3"
color_azul= "#4c3af5"
color_azul_2="#5243d6"
color_verde="#81dc00"
color_verde_2="#93e5a1"
color_blanco="#ffffff"
color_negro="#000000"


ventana = CTk()
ventana.title("Sistema de Registro")
ventana.geometry("820x640")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
#=========================================================================================================
#FRAME DATOS 
#=========================================================================================================
frame_datos=CTkFrame(master=ventana,
                     corner_radius=0,
                     fg_color=color_fondo)
frame_datos.grid(row=1,column=0,sticky="nswe")
frame_datos.grid_columnconfigure([0,1], weight=1)
for i in range (5):
    frame_datos.grid_rowconfigure(i, weight=1)

#=========================================================================================================
#FRAME NOMBRE 
#========================================================================================================
etiqueta_nombre= CTkLabel(master=frame_datos,
                          width=150,
                          height=55,
                          text="NOMBRE:",
                          justify="center",
                          font=("Montserrat", 16, "bold"),
                          text_color=color_blanco,
                          fg_color=color_verde
                          )

etiqueta_nombre.grid(row=0, 
                     column=0, 
                     sticky="e"
                     )

campo_nombre = CTkEntry(
    master=frame_datos,
    width=250,
    height=55,
    border_color=color_blanco,
    fg_color=color_blanco,
    text_color=color_negro,
    corner_radius=0,
    justify="center",
    placeholder_text="...",
    font=("Montserrat", 16),
)
campo_nombre.grid(row=0,
                  column=1, 
                  sticky="w",
                  padx=2
                  )

#=========================================================================================================
#FRAME DESCRIPCION 
#=========================================================================================================
etiqueta_descripcion= CTkLabel(master=frame_datos,
                               width=200,
                               height=50,
                               text="DESCRIPCION:",
                               font=("Montserrat", 16, "bold"),
                               justify="center",
                               text_color=color_blanco,
                               fg_color=color_verde
                               )

etiqueta_descripcion.grid(row=1, 
                          column=0,
                          sticky="ews",
                          columnspan=2)

campo_descrip = CTkEntry(master=frame_datos,
                         width=200,
                         height=155,
                         fg_color=color_blanco,
                         border_color=color_fondo,
                         text_color=color_negro,
                         corner_radius=0,
                         justify="center",
                         placeholder_text="...",
                         font=("Montserrat", 16)
                         )

campo_descrip.grid(row=2,
                   column=0,
                   sticky="ewn",
                   columnspan=2,
                   rowspan=2)

#=========================================================================================================
#FRAME FECHA 
#=========================================================================================================
etiqueta_fecha= CTkLabel(master=frame_datos,
                          width=150,
                          height=55,
                          text="FECHA:",
                          font=("Montserrat", 16, "bold"),
                          text_color=color_blanco,
                          fg_color=color_verde
                          )

etiqueta_fecha.grid(row=3, 
                    column=0, 
                    sticky="es"
                    )

campo_fecha = CTkEntry(master=frame_datos,
                       width=250,
                       height=55,
                       corner_radius=0,
                       fg_color=color_blanco,
                       border_color=color_blanco,
                       text_color=color_negro,
                       justify="center",
                       placeholder_text="...",
                       font=("Montserrat", 16))

campo_fecha.grid(row=3,
                 column=1,
                 sticky="ws"
                 )

#=========================================================================================================
#BOTONES 
#=========================================================================================================

boton_1 = CTkButton(
    master=frame_datos,
    width=120,
    height=60,
    corner_radius=5,
    text="Haz Click",
    fg_color=color_azul,
    hover_color=color_azul_2,
    font=("Montserrat", 16)
    )

boton_1.grid(row=4,
             column=0,
             sticky="we",
             padx=20
             )

boton_2 = CTkButton(
    master=frame_datos,
    width=120,
    height=60,
    corner_radius=5,
    text="Haz Click",
    fg_color=color_azul,
    hover_color=color_azul_2,
    font=("Montserrat", 16)
    )

boton_2.grid(row=4,
             column=1,
             sticky="we",
             padx=20
             )