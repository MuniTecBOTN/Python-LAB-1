from customtkinter import *
import os
from PIL import Image
from datetime import datetime
set_default_color_theme("dark-blue")
set_appearance_mode("dark")

#==========================================================================================
# VENTANA
#==========================================================================================
ventana = CTk()
ventana.title("Organizador")
ventana.geometry("800x600")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

#=========================================================================================================
#COLORES
#=========================================================================================================
color_blanco = "#ffffff"
color_fondo= "#e3e5f3"
color_rosita= "#563af5"
color_azul_2="#7aa3ee"
color_verde="#b3e470"
color_rosita="#edabf0"
color_amarillo="#e8f195"
color_naranja="#fcdf60"
color_negro="#000000"
transparente = "transparent"
ALTURA_ESTANDAR_CAMPO = 50
TAMAÑO_LETRA_NORMAL = 18
TAMAÑO_LETRA_TITULO = 28 
NOMBRE_FUENTE = "Monteserrat"
letra_cursiva="Lobster"
letra_titulo="Ultra"
#==========================================================================================
#ATAJOS 
#==========================================================================================
estilo_botones={
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "text_color": color_blanco,
    "font": (NOMBRE_FUENTE, TAMAÑO_LETRA_NORMAL, "bold"),
    "corner_radius": 0,
}

estilo_etiqueta_titulo = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": (letra_titulo, TAMAÑO_LETRA_TITULO, "bold"),
    "text_color": color_blanco,
}

estilo_etiquetas={"width":180, 
                  "height":40,
                  "justify":"center",
                  "font":(NOMBRE_FUENTE, 16, "bold"),
                  "text_color":color_blanco,
                  }

estilo_campo = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": color_blanco,
    "border_color": color_blanco,
    "text_color": color_negro,
    "justify": "center",
    "corner_radius": 0,
    "placeholder_text": "",
    "font": (NOMBRE_FUENTE, TAMAÑO_LETRA_NORMAL),
}

#==========================================================================================
# FRAME PRINCIPAL
#==========================================================================================
frame_principal= CTkFrame(master=ventana,
                          fg_color=color_fondo,
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=20)
frame_principal.grid_rowconfigure(0, weight=1)
#==========================================================================================
# FRAME IZQUIERDO
#==========================================================================================

frame_izquierdo= CTkFrame(master=frame_principal,
                        fg_color=color_rosita,
                        corner_radius=0)
frame_izquierdo.grid(row=0, 
                   column=0, 
                   sticky="snwe"
                   )
frame_izquierdo.grid_rowconfigure(0, weight=1)
frame_izquierdo.grid_rowconfigure(1, weight=1)
frame_izquierdo.grid_rowconfigure(2, weight=1)
frame_izquierdo.grid_rowconfigure(3, weight=1)
frame_izquierdo.grid_rowconfigure(4, weight=1)
frame_izquierdo.grid_rowconfigure(5, weight=1)
frame_izquierdo.grid_rowconfigure(6, weight=1)
frame_izquierdo.grid_columnconfigure(0,weight=1)

titulo_izquierdo=CTkLabel(master=frame_izquierdo,
                        corner_radius=0,
                        fg_color=transparente,
                        **estilo_etiqueta_titulo,
                        text="CONTROL")
titulo_izquierdo.grid(row=0, column=0)

boton_inicio= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="🏡 INICIO",
                        command=lambda: ir_a_pestaña("INICIO"),
                        fg_color=transparente,
                        hover_color=color_azul_2)
                        
boton_inicio.grid(row=1, column=0, sticky="ns")

boton_MATERIAS= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="📚 MATERIAS",
                        command=lambda: ir_a_pestaña("MATERIAS"),
                        fg_color=transparente,
                        hover_color=color_azul_2
                        )
boton_MATERIAS.grid(row=2, column=0, sticky="ns")

boton_tareas= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="📝 TAREAS",
                        fg_color=transparente,
                        command=lambda: ir_a_pestaña("TAREAS"),
                        hover_color=color_azul_2
                        )
boton_tareas.grid(row=3, column=0, sticky="ns")

boton_horario= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="🕣 HORARIO",
                        fg_color=transparente,
                        command=lambda: ir_a_pestaña("HORARIO"),
                        hover_color=color_azul_2
                        )
boton_horario.grid(row=4, column=0, sticky="ns")

boton_configuracion= CTkButton(master=frame_izquierdo,
                               width= 120,
                               height= ALTURA_ESTANDAR_CAMPO,
                               text_color= color_blanco,
                               font=(NOMBRE_FUENTE, 16, "bold"),
                               corner_radius= 0,
                               text="⚙️ CONFIGURACION",
                               fg_color=transparente,
                               command=lambda: ir_a_pestaña("CONFIGURACION"),
                               hover_color=color_azul_2
                               )
boton_configuracion.grid(row=5, column=0, sticky="ns")

boton_salir= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="🚪 SALIR",
                        fg_color=transparente,
                        hover_color=color_azul_2,
                        command=ventana.destroy)
boton_salir.grid(row=6, column=0, sticky="n")

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
                        **estilo_etiqueta_titulo, 
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
                            sticky="news",
                            padx=0,
                            pady=0
                            )
frame_derecho_inferior.grid_columnconfigure(0, weight=1)
frame_derecho_inferior.grid_rowconfigure(0, weight=1)


#==========================================================================================
# TABVIEW
#==========================================================================================
pestañas=CTkTabview(master=frame_derecho_inferior,
                    corner_radius=0,
                    fg_color=color_fondo)

pestañas.grid(row=0,
              column=0,
              sticky="nsew",
              padx=0,
              pady=0)

pestaña_tareas=pestañas.add("TAREAS")
pestaña_tareas.grid_columnconfigure(0, weight=1)
pestaña_tareas.grid_rowconfigure(0, weight=1)
pestaña_tareas.configure(fg_color=color_azul_2, 
                             corner_radius=0,
                             border_width=0)

pestaña_horario=pestañas.add("HORARIO")
pestaña_horario.grid_columnconfigure(0, weight=1)
pestaña_horario.grid_rowconfigure(0, weight=1)
pestaña_horario.configure(fg_color=color_azul_2)

pestaña_configuracion=pestañas.add("CONFIGURACION")
pestaña_configuracion.grid_columnconfigure(0, weight=1)
pestaña_configuracion.grid_rowconfigure(0, weight=1)
pestaña_configuracion.configure(fg_color=color_azul_2)


pestañas._segmented_button.grid_forget()

def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    etiquta_titulo.configure(text=nombre_pestaña)

#==========================================================================================
# PESTAÑA INICIO
#==========================================================================================
nombre_usuario="Abi"
pestaña_inicio=pestañas.add("INICIO")
pestaña_inicio.grid_columnconfigure (0,weight=1)
pestaña_inicio.grid_rowconfigure (0, weight=1)
pestaña_inicio.grid_rowconfigure (1, weight=1)
pestaña_inicio.grid_rowconfigure (2, weight=1)
pestaña_inicio.grid_rowconfigure(3, weight=1)
pestaña_inicio.configure(fg_color= color_azul_2,
                         corner_radius=0)

titulo_bienvenida=CTkLabel(master=pestaña_inicio,
                           corner_radius=0,
                           fg_color=transparente,
                           text=f"Bienvenida, {nombre_usuario}",
                           text_color=color_negro,
                           font=(letra_cursiva, 65, "bold"),
                           justify="center"
                           )
titulo_bienvenida.grid(row=0, column=0)

fecha= datetime.now().strftime( "%d/%m/%Y" )
label_fecha= CTkLabel(master=pestaña_inicio,
                      text=f"Fecha actual: {fecha}",
                      font=("Arial", 24, "bold"),
                      justify="center")
label_fecha.grid(row=1, column=0, sticky="ns")

frame_izquierdo_inferior_inicio=CTkFrame(master=pestaña_inicio,
                                         corner_radius=0, 
                                         fg_color=transparente)
frame_izquierdo_inferior_inicio.grid(row=2, column=0, sticky="nswe")
frame_izquierdo_inferior_inicio.grid_columnconfigure(0, weight=1)
frame_izquierdo_inferior_inicio.grid_columnconfigure(1, weight=1)
frame_izquierdo_inferior_inicio.grid_rowconfigure(0, weight=1)
frame_izquierdo_inferior_inicio.grid_rowconfigure(1, weight=1)

num_materias="2"
label_materia_inicio=CTkLabel(master=frame_izquierdo_inferior_inicio,
                              **estilo_etiquetas,
                              fg_color=color_rosita,
                              text=f"Materias: {num_materias}")
label_materia_inicio.grid(row=0, column=0, padx=20, sticky="sw")
materias_pend="5"
label_tareas_pen_inicio=CTkLabel(master=frame_izquierdo_inferior_inicio,
                                 **estilo_etiquetas,
                                 fg_color=color_rosita,
                                 text=f"Tareas pendientes: {materias_pend}")
label_tareas_pen_inicio.grid(column=0, row=1, padx=20, sticky="ws")

tareas_proximas_inicio=CTkLabel(master=frame_izquierdo_inferior_inicio,
                                 **estilo_etiquetas,
                                 fg_color=color_rosita,
                                 text="Tareas a entregar proximamente:")
tareas_proximas_inicio.grid(row=0, column=1, sticky="es", padx=20)
datos_inicio_tareas_proxi=CTkLabel(master=frame_izquierdo_inferior_inicio,
                                   width= 252, 
                                   height=40,
                                   justify="center",
                                   font=(NOMBRE_FUENTE, 16, "bold"),
                                   text_color=color_negro,
                                   fg_color=color_blanco,
                                   text="")
datos_inicio_tareas_proxi.grid(row=1, column=1, sticky="sne", padx=20)
#==================================
# IMAGEN
#==================================
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(ruta_script, "imagenes/banner.jpg")

imagen_banner = CTkImage(
    light_image=Image.open(ruta_imagen),
    dark_image=Image.open(ruta_imagen),
    size=(600, 130)
)

etiqueta_imagen = CTkLabel(
        master=pestaña_inicio,
        image=imagen_banner, 
        text="",
)
etiqueta_imagen.grid(
        row=3,
        column=0,
        sticky="snew",
        padx=20,
        pady=5
)

#==========================================================================================
#FRAME MATERIAS 
#==========================================================================================
pestaña_materias=pestañas.add("MATERIAS")
pestaña_materias.grid_columnconfigure(0, weight=1)
pestaña_materias.grid_rowconfigure(0, weight=1)
pestaña_materias.grid_rowconfigure(1, weight=50)
pestaña_materias.configure(fg_color=color_azul_2)

titulo_materias= CTkLabel(master=pestaña_materias,
                          corner_radius=0,
                          fg_color=transparente,
                          text="Materias",
                          text_color=color_negro,
                          font=(letra_cursiva, 50, "bold"),
                          justify="center"
                          )
titulo_materias.grid(row=0, column=0)
frame_principal_materias=CTkFrame(master=pestaña_materias,
                                  corner_radius=10, 
                                  fg_color=color_blanco)
frame_principal_materias.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

#==========================================================================================
# 
#==========================================================================================

ventana.mainloop()