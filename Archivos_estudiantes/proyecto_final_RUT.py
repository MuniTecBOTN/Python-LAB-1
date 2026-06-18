from customtkinter import *
import os
from PIL import Image
from datetime import datetime
from tabla_customtkinter import CTkTable


set_default_color_theme("dark-blue")
set_appearance_mode("light")

#==========================================================================================
# VENTANA
#==========================================================================================
ventana = CTk()
ventana.title("Organizador")
ventana.geometry("850x650")
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
    "font": (NOMBRE_FUENTE, TAMAÑO_LETRA_NORMAL, "bold"),
    "corner_radius": 0,
    "text_color":color_blanco
}

estilo_etiqueta_titulo = {
    "height": 65,
    "font": (letra_titulo, TAMAÑO_LETRA_TITULO, "bold"),
    "text_color": color_blanco,
}

estilo_etiquetas={"width":190, 
                  "height":40,
                  "justify":"center",
                  "font":(NOMBRE_FUENTE, 16, "bold"),
                  "text_color":color_blanco,
                  }

estilo_campo = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color":color_blanco,
    "border_color": color_negro,
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
frame_izquierdo.grid_propagate(False)
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
frame_derecho.grid_rowconfigure(0,weight=0)
frame_derecho.grid_rowconfigure(1,weight=50)
frame_derecho.grid_propagate(False)

etiqueta_titulo=CTkLabel(master=frame_derecho,
                        **estilo_etiqueta_titulo, 
                        text="INICIO",
                        fg_color=color_rosita,
                        anchor="center")
etiqueta_titulo.grid(row=0, 
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

pestaña_horario=pestañas.add("HORARIO")
pestaña_horario.grid_columnconfigure(0, weight=1)
pestaña_horario.grid_rowconfigure(0, weight=1)
pestaña_horario.configure(fg_color=color_azul_2)



pestañas._segmented_button.grid_forget()

def ir_a_pestaña(nombre_pestaña):
    pestañas.set(nombre_pestaña)
    etiqueta_titulo.configure(text=nombre_pestaña)
    etiqueta_titulo.grid_propagate(False)

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
ruta_imagen = os.path.join(ruta_script, "banner.jpg")

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
frame_principal_materias.grid_columnconfigure(0, weight=1)
frame_principal_materias.grid_rowconfigure(0, weight=1)
frame_principal_materias.grid_rowconfigure(1, weight=8)
frame_principal_materias.grid_rowconfigure(2, weight=1)


lista_materias = [] 

frame_form_materias = CTkFrame(master=frame_principal_materias,
                               corner_radius=10,
                               fg_color=color_rosita)
frame_form_materias.grid(row=0, column=0, sticky="new", padx=10, pady=10)
frame_form_materias.grid_columnconfigure(0, weight=1)
frame_form_materias.grid_columnconfigure(1, weight=1)
frame_form_materias.grid_columnconfigure(2, weight=1)
frame_form_materias.grid_columnconfigure(3, weight=1)

etiqueta_nombre_materia = CTkLabel(master=frame_form_materias,
                                   **estilo_etiquetas,
                                   fg_color=transparente,
                                   text="Materia:")
etiqueta_nombre_materia.grid(row=0, column=0, padx=10, pady=10)

campo_nombre_materia = CTkEntry(master=frame_form_materias,
                                **estilo_campo)
campo_nombre_materia.grid(row=0, column=1, padx=10, pady=10)

etiqueta_profesor = CTkLabel(master=frame_form_materias,
                             **estilo_etiquetas,
                             fg_color=transparente,
                             text="Profesor:")
etiqueta_profesor.grid(row=0, column=2, padx=10, pady=10)

campo_profesor = CTkEntry(master=frame_form_materias,
                          **estilo_campo)
campo_profesor.grid(row=0, column=3, padx=10, pady=10)

boton_agregar_materia = CTkButton(master=frame_form_materias,
                                  **estilo_botones,
                                  text="➕ AGREGAR",
                                  fg_color=color_azul_2,
                                  hover_color=color_verde)
                                  
boton_agregar_materia.grid(row=0, column=4, pady=10, padx=5)  

tabla_materias=CTkTable(master=frame_principal_materias,
                        columnas=["Materia", "Profesor"],
                        datos=[],
                        row=1,
                        column=0,
                        padx=10,
                        pady=10,
                        sticky="nswe",
                        height=6)

frame_botones_materias=CTkFrame(master=frame_principal_materias,
                                corner_radius=0,
                                fg_color=transparente)
frame_botones_materias.grid(column=0, row=2, pady=10),
frame_botones_materias.grid_rowconfigure(0, weight=1)
frame_principal_materias.grid_columnconfigure(0, weight=1)
frame_principal_materias.grid_columnconfigure(1, weight=1)

boton_editar=CTkButton(master=frame_botones_materias,
                       **estilo_botones,
                       text="✏️ EDITAR",
                       fg_color=color_verde,
                       hover_color=color_azul_2)
boton_editar.grid(row=0, column=0, padx=10)
boton_eliminar=CTkButton(master=frame_botones_materias,
                         **estilo_botones,
                         fg_color=color_amarillo,
                         hover_color=color_azul_2,
                         text="🗑️ELIMINAR")
boton_eliminar.grid(row=0,column=1, padx=10)

#==========================================================================================
# Frame Tareas
#==========================================================================================
pestaña_tareas=pestañas.add("TAREAS")
pestaña_tareas.grid_columnconfigure(0, weight=1)
pestaña_tareas.grid_rowconfigure(0, weight=1)
pestaña_tareas.grid_rowconfigure(1, weight=50)
pestaña_tareas.configure(fg_color=color_azul_2)

titiulo_tareas= CTkLabel(master=pestaña_tareas,
                          corner_radius=0,
                          fg_color=transparente,
                          text="Tareas",
                          text_color=color_negro,
                          font=(letra_cursiva, 50, "bold"),
                          justify="center"
                          )
titiulo_tareas.grid(row=0, column=0)
frame_principal_tareas=CTkFrame(master=pestaña_tareas,
                                  corner_radius=10, 
                                  fg_color=color_blanco)
frame_principal_tareas.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
frame_principal_tareas.grid_columnconfigure(0, weight=1)
frame_principal_tareas.grid_rowconfigure(0, weight=1)
frame_principal_tareas.grid_rowconfigure(1, weight=8)
frame_principal_tareas.grid_rowconfigure(2, weight=1)


lista_tareas = [] 

frame_form_tareas = CTkFrame(master=frame_principal_tareas,
                               corner_radius=10,
                               fg_color=color_rosita)
frame_form_tareas.grid(row=0, column=0, sticky="new", padx=10, pady=10)
frame_form_tareas.grid_columnconfigure(0, weight=1)
frame_form_tareas.grid_columnconfigure(1, weight=1)
frame_form_tareas.grid_columnconfigure(2, weight=1)
frame_form_tareas.grid_columnconfigure(3, weight=1)
frame_form_tareas.grid_columnconfigure(4, weight=1)

etiqueta_tarea=CTkLabel(master=frame_form_tareas,
                        **estilo_etiquetas,
                        fg_color=transparente,
                        corner_radius=0,
                        text="Tareas: ")
etiqueta_tarea.grid(row=0, column=0,padx=10, pady=10)
campo_tareas=CTkEntry(master=frame_form_tareas,
                      **estilo_campo,)
campo_tareas.grid(row=0, column=1,padx=10, pady=10)

etiqueta_entrega=CTkLabel(master=frame_form_tareas,
                        **estilo_etiquetas,
                        fg_color=transparente,
                        corner_radius=0,
                        text="Fecha entrega: ")
etiqueta_entrega.grid(row=0, column=2,padx=10, pady=10)
campo_entrega=CTkEntry(master=frame_form_tareas,
                      **estilo_campo,)
campo_entrega.grid(row=0, column=3,padx=10, pady=10)

boton_agregar_tareas=CTkButton(master=frame_form_tareas,
                               **estilo_botones,
                               fg_color=color_azul_2,
                               hover_color=color_verde,
                               text="➕ Agregar")
boton_agregar_tareas.grid(row=0, column=4, padx=10, pady=10)
#==========================================================================================
# PESTAÑA CONFIGURACION
#==========================================================================================

pestaña_configuracion=pestañas.add("CONFIGURACION")
pestaña_configuracion.grid_columnconfigure(0, weight=1)
pestaña_configuracion.grid_rowconfigure(0, weight=1)
pestaña_configuracion.grid_rowconfigure(1, weight=1)
pestaña_configuracion.grid_rowconfigure(2, weight=1)

pestaña_configuracion.configure(fg_color=color_azul_2)



titulo_configuracion = CTkLabel(master=pestaña_configuracion,
                                corner_radius=0,
                                fg_color=transparente,
                                text="Configuración",
                                text_color=color_negro,
                                font=(letra_cursiva, 50, "bold"),
                                justify="center")
titulo_configuracion.grid(row=0, column=0, pady=10)

frame_opciones = CTkFrame(master=pestaña_configuracion,
                          corner_radius=10,
                          fg_color=color_blanco)
frame_opciones.grid(row=1, column=0, sticky="nswe", padx=20, pady=10)
frame_opciones.grid_columnconfigure(0, weight=1)
frame_opciones.grid_columnconfigure(1, weight=1)
frame_opciones.grid_rowconfigure(0, weight=1)
frame_opciones.grid_rowconfigure(1, weight=1)
frame_opciones.grid_rowconfigure(2, weight=1)

# CAMBIAR NOMBRE DE USUARIO

nombre_usuario= CTkLabel(master=frame_opciones,
                         **estilo_etiquetas,
                         fg_color=color_rosita,
                         text="Nuevo nombre")
nombre_usuario.grid(row=0, column=0, padx=20, pady=15, sticky="e")

campo_nuevo_nombre = CTkEntry(master=frame_opciones,
                              **estilo_campo)
campo_nuevo_nombre.grid(row=0, column=1, padx=20, pady=15, sticky="w")

def guardar_nombre():
    nuevo = campo_nuevo_nombre.get().strip()
    if nuevo != "":
        titulo_bienvenida.configure(text=f"Bienvenida, {nuevo}")

boton_guardar=CTkButton(master=frame_opciones,
          **estilo_botones,
          text="💾 Guardar",
          fg_color=color_rosita,
          hover_color=color_azul_2,
          command=guardar_nombre).grid(row=0, column=2, padx=20, pady=15)

etiqueta_tema=CTkLabel(master=frame_opciones,
         **estilo_etiquetas,
         fg_color=color_rosita,
         text="Tema:").grid(row=1, column=0, padx=20, pady=15, sticky="e")

#CAMBIAR TEMA

def cambiar_tema(opcion):
    set_appearance_mode(opcion)

selector_tema = CTkSegmentedButton(master=frame_opciones,
                                   values=["Light", "Dark", "System"],
                                   font=(NOMBRE_FUENTE, 15, "bold"),
                                   selected_color=color_rosita,
                                   selected_hover_color=color_azul_2,
                                   unselected_color=color_fondo,
                                   text_color=color_negro,
                                   command=cambiar_tema)
selector_tema.set("Dark")
selector_tema.grid(row=1, column=1, padx=20, pady=15, sticky="w")

#ACERCA DE
frame_acerca = CTkFrame(master=frame_opciones,
                        corner_radius=10,
                        fg_color=transparente)
frame_acerca.grid(row=2, column=0, columnspan=3, sticky="nswe", padx=20, pady=15)
frame_acerca.grid_columnconfigure(0, weight=1)

texto_acerca_de=CTkLabel(master=frame_acerca,
         text="Acerca de",
         font=(letra_cursiva, 28, "bold"),
         fg_color=transparente)
texto_acerca_de.grid(row=0, column=0, pady=(10, 2))

texto_configuracio=CTkLabel(master=frame_acerca,
         text="Organizador Escolar  •  Versión 1.0",
         font=(NOMBRE_FUENTE, 15),
         fg_color=transparente)
texto_configuracio.grid(row=1, column=0, pady=2)

texto_desarrolado_por= CTkLabel(master=frame_acerca,
         text="Desarrollado por Abi 💜",
         font=(NOMBRE_FUENTE, 15, "bold"),
         fg_color=transparente)
texto_desarrolado_por.grid(row=2, column=0, pady=(2, 10))

etiqueta_titulo
#==========================================================================================
# 
#==========================================================================================

ventana.mainloop()