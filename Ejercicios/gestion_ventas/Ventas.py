from customtkinter import *

set_default_color_theme("dark-blue")
set_appearance_mode("light")

#==========================================================================================
# VENTANA
#==========================================================================================
ventana = CTk()
ventana.title("VENTAS")
ventana.geometry("800x600")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

#=========================================================================================================
#COLORES
#=========================================================================================================
color_fondo= "#e3e5f3"
color_azul= "#624be4"
color_azul_2="#9bb8ee"
color_verde="#b3e470"
color_rosita="#e89feb"
color_amarillo="#e8f195"
color_naranja="#fcdf60"
color_blanco="#FFFFFF"
color_negro="#000000"
transparente="transparent"
#==========================================================================================
#ATAJOS 
#==========================================================================================
estilo_botones={
    "width":140,
    "height":35,
    "corner_radius":0,
    "fg_color":color_rosita,
    "hover_color": color_azul_2,
    "text_color":color_blanco,
    "font":("Monteserrat", 16, "bold")}

estilo_etiquetas={"width":150, 
                  "height":50,
                  "justify":"center",
                  "font":("Montserrat", 16, "bold"),
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
estilo_titulos={"text_color":color_blanco,
                "justify":"center",
                "font":("Montserrat", 20, "bold"),
                  }

#==========================================================================================
# BOTONES DE PESTAÑAS DEF
#==========================================================================================

def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    etiquta_titulo.configure(text=nombre_pestaña)

#==========================================================================================
# FRAME PRINCIPAL
#==========================================================================================
frame_principal= CTkFrame(master=ventana,
                          fg_color=color_fondo,
                          corner_radius=0)
frame_principal.grid(row=0, 
                     column=0, 
                     sticky= "nsew", 
                     padx=5, 
                     pady=5
                     )
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=50)
frame_principal.grid_rowconfigure(0, weight=1)

#==========================================================================================
# FRAME SIDEBAR
#==========================================================================================
frame_sidebar= CTkFrame(master=frame_principal,
                        fg_color=color_rosita,
                        corner_radius=0)
frame_sidebar.grid(row=0, 
                   column=0, 
                   sticky="snwe"
                   )
frame_sidebar.grid_rowconfigure(0, weight=1)
frame_sidebar.grid_rowconfigure(1, weight=1)
frame_sidebar.grid_rowconfigure(2, weight=1)
frame_sidebar.grid_rowconfigure(3, weight=1)
frame_sidebar.grid_rowconfigure(4, weight=1)
frame_sidebar.grid_rowconfigure(5, weight=1)
frame_sidebar.grid_rowconfigure(6, weight=1)
frame_sidebar.grid_rowconfigure(7, weight=1)
frame_sidebar.grid_columnconfigure(0,weight=1)

titulo_sidebar=CTkLabel(master=frame_sidebar,
                        corner_radius=0,
                        fg_color=transparente,
                        **estilo_titulos,
                        text="SIDEBAR",
                        width=30,
                        height=60)
titulo_sidebar.grid(row=0, column=0)

boton_inicio= CTkButton(master=frame_sidebar,
                        **estilo_botones,
                        corner_radius=0,
                        text="🏡 INICIO",
                        command=lambda: ir_a_pestaña("INICIO"))
boton_inicio.grid(row=1, column=0, sticky="ns")

boton_ventas= CTkButton(master=frame_sidebar,
                        **estilo_botones,
                        corner_radius=0,
                        text="🛒 VENTAS",
                        command=lambda: ir_a_pestaña("VENTAS")
                        )
boton_ventas.grid(row=2, column=0, sticky="ns")

boton_productos= CTkButton(master=frame_sidebar,
                        **estilo_botones,
                        corner_radius=0,
                        text="📦 PRODUCTOS",
                        command=lambda: ir_a_pestaña("PRODUCTOS"))
boton_productos.grid(row=3, column=0,  sticky="ns")

boton_inventario= CTkButton(master=frame_sidebar,
                        **estilo_botones,
                        corner_radius=0,
                        text="📋 INVENTARIO",
                        command=lambda: ir_a_pestaña("INVENTARIO"))
boton_inventario.grid(row=4, column=0, sticky="ns")

boton_clientes= CTkButton(master=frame_sidebar,
                        **estilo_botones,
                        corner_radius=0,
                        text="👥 CLIENTES",
                        command=lambda: ir_a_pestaña("CLIENTES"))
boton_clientes.grid(row=5, column=0, sticky="ns")

boton_reportes= CTkButton(master=frame_sidebar,
                        **estilo_botones,
                        corner_radius=0,
                        text="📧 REPORTES",
                        command=lambda: ir_a_pestaña("REPORTES"))
boton_reportes.grid(row=6, column=0, sticky="ns")

boton_salir= CTkButton(master=frame_sidebar,
                        **estilo_botones,
                        corner_radius=0,
                        text="🚪 SALIR",
                        command=ventana.destroy)
boton_salir.grid(row=7, column=0, sticky="ns")

#==========================================================================================
# FRAME DERECHO
#==========================================================================================
frame_derecho=CTkFrame(master=frame_principal,
                       fg_color=transparente,
                       corner_radius=0)
frame_derecho.grid(row=0, 
                   column=1, 
                   sticky="nswe"
                   )
frame_derecho.grid_columnconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(0,weight=1)
frame_derecho.grid_rowconfigure(1,weight=50)

etiquta_titulo=CTkLabel(master=frame_derecho,
                        **estilo_titulos, 
                        width=45,
                        height=65,
                        text="INICIO",
                        fg_color=color_rosita
                        )
etiquta_titulo.grid(row=0, 
                    column=0, 
                    sticky="wens"
                    )

frame_derecho_inferior=CTkFrame(master=frame_derecho,
                                corner_radius=0,
                                fg_color=color_fondo)
frame_derecho_inferior.grid(row=1, 
                            column=0, 
                            sticky="news"
                            )
frame_derecho_inferior.grid_columnconfigure(0, weight=1)
frame_derecho_inferior.grid_rowconfigure(0, weight=1)

#==========================================================================================
# PESTAÑAS
#==========================================================================================
pestañas=CTkTabview(master=frame_derecho_inferior,
                    corner_radius=0,
                    fg_color=color_fondo)

pestañas.grid(row=0,
              column=0,
              sticky="nsew",
              padx=8,
              pady=10)

pestaña_inicio=pestañas.add("INICIO")
pestaña_inicio.grid_columnconfigure (0,weight=1)
pestaña_inicio.grid_rowconfigure (0, weight=1)
pestaña_inicio.configure(fg_color= color_azul_2,
                         corner_radius=0)


pestaña_productos=pestañas.add("PRODUCTOS")
pestaña_productos.grid_columnconfigure(0, weight=1)
pestaña_productos.grid_rowconfigure(0, weight=1)
pestaña_productos.configure(fg_color=color_amarillo)

pestaña_inventario=pestañas.add("INVENTARIO")
pestaña_inventario.grid_columnconfigure(0, weight=1)
pestaña_inventario.grid_rowconfigure(0, weight=1)
pestaña_inventario.configure(fg_color=color_azul)

pestaña_clientes=pestañas.add("CLIENTES")
pestaña_clientes.grid_columnconfigure(0, weight=1)
pestaña_clientes.grid_rowconfigure(0, weight=1)
pestaña_clientes.configure(fg_color=color_verde)

pestaña_reportes=pestañas.add("REPORTES")
pestaña_reportes.grid_columnconfigure(0, weight=1)
pestaña_reportes.grid_rowconfigure(0, weight=1)
pestaña_reportes.configure(fg_color=color_negro)

pestaña_salir=pestañas.add("SALIR")
pestaña_salir.grid_columnconfigure(0, weight=1)
pestaña_salir.grid_rowconfigure(0, weight=1)
pestaña_salir.configure(fg_color=color_blanco)


pestañas._segmented_button.grid_forget()

#==========================================================================================
#PESTAÑA VENTAS
#==========================================================================================
pestaña_ventas=pestañas.add("VENTAS")
pestaña_ventas.grid_columnconfigure(0, weight=1)
pestaña_ventas.grid_rowconfigure(0, weight=1)
pestaña_ventas.configure(
    fg_color=transparente,
    corner_radius=0)

frame_ventas=CTkFrame(master=pestaña_ventas,
                      fg_color=transparente,
                      corner_radius=0)
frame_ventas.grid(row=0, column=0, sticky="nsew")
frame_ventas.grid_rowconfigure(0, weight=1)
frame_ventas.grid_rowconfigure(1, weight=1)
frame_ventas.grid_rowconfigure(2, weight=1)
frame_ventas.grid_columnconfigure(0, weight=1)

frame_ventas_superior=CTkFrame(master=frame_ventas,
                               fg_color=color_blanco,
                               corner_radius=0)

frame_ventas_superior.grid(row=0, column=0, sticky="wnse")

frame_ventas_superior.grid_columnconfigure(0, weight=1)
frame_ventas_superior.grid_columnconfigure(1, weight=1)
frame_ventas_superior.grid_columnconfigure(2, weight=1)

frame_ventas_superior.grid_rowconfigure(0,weight=1)
frame_ventas_superior.grid_rowconfigure(1,weight=1)
frame_ventas_superior.grid_rowconfigure(2,weight=1)

etiqueta_item=CTkLabel(master=frame_ventas_superior,
                       fg_color=color_amarillo,
                       **estilo_etiquetas,
                       text="ITEM"
                       )
etiqueta_item.grid(row=0, column=0, sticky="e")

lista_items=["1","2", "3", "4", "5", "6"]
item_seleccionado=StringVar(value="Selec. un Item")
menu_items= CTkOptionMenu(
    master=frame_ventas_superior,
    width=200,
    height=50,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_items,
    variable=item_seleccionado,
    fg_color=color_blanco,
    text_color=color_negro,
    button_color=color_azul,
    button_hover_color=color_azul_2,
    dropdown_fg_color=color_amarillo,
    dropdown_text_color=color_negro,
    dropdown_font=("Montserrat",16),
    font=("Montserrat", 16, "bold")
)
menu_items.grid(row=0, column=1, sticky="e")

etiqueta_cantidad=CTkLabel(master=frame_ventas_superior,
                           fg_color=color_amarillo,
                           **estilo_etiquetas,
                           text="CANTIDAD")
etiqueta_cantidad.grid(row=1, column=0, sticky="e")

#==========================================================================================
# 
#==========================================================================================


ventana.mainloop()