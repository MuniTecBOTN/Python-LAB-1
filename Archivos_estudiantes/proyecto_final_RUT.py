from customtkinter import *
import os
import sys
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
ventana.geometry("1000x650")
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
color_morado="#b461f8"
color_naranja="#fcd34b"
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
# DEF FUNCIONES
#==========================================================================================
def ruta_recursos(relative_path):
    """ Obtiene la ruta de los recursos, compatible con desarrollo y PyInstaller """
    try:
        # Si corre desde el .exe empaquetado por PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # Si corre normal en VS Code, mantiene la carpeta 'imagenes'
        base_path = os.path.abspath(".")
        if not os.path.exists(os.path.join(base_path, relative_path)):
            return os.path.join(base_path, "imagenes", relative_path)
            
    return os.path.join(base_path, relative_path)
#-----------------------------
#INICIO DEFINICIONES
#-----------------------------
def actualizar_inicio():
    label_materia_inicio.configure(text=f"Materias: {len(lista_materias)}")

    pendientes = [t for t in lista_tareas if t[2] == "Pendiente"]
    label_tareas_pen_inicio.configure(text=f"Tareas pendientes: {len(pendientes)}")

    if pendientes:
        texto_proximas = "\n".join([f"• {t[0]} — {t[1]}" for t in pendientes[:3]])
    else:
        texto_proximas = "¡No tienes tareas pendientes! 🎉"
    datos_inicio_tareas_proxi.configure(text=texto_proximas)

#--------------------------
#  MATERIAS FUNCIONES
#--------------------------
def agregar_materia():
    nombre = campo_nombre_materia.get().strip()
    profesor = campo_profesor.get().strip()
    if nombre == "" or profesor == "":
        return
    lista_materias.append((nombre, profesor))
    tabla_materias["insertar"]((nombre, profesor))
    campo_nombre_materia.delete(0, "end")
    campo_profesor.delete(0, "end")
    actualizar_menu_materias()
    actualizar_inicio()

def eliminar_materia_tabla():
    fila = tabla_materias["obtener_fila"]()
    if fila:
        lista_materias.remove(fila)
        tabla_materias["eliminar_seleccion"]()
        actualizar_menu_materias()
        actualizar_inicio()

def editar_materia():
    fila = tabla_materias["obtener_fila"]()
    if fila:
        nombre, profesor = fila
        campo_nombre_materia.delete(0, "end")
        campo_nombre_materia.insert(0, nombre)
        campo_profesor.delete(0, "end")
        campo_profesor.insert(0, profesor)
        eliminar_materia_tabla()
        
#--------------------------
#  TAREAS FUNCIONES
#--------------------------        
def agregar_tarea():
    nombre = campo_tareas.get().strip()
    fecha_entrega = campo_fecha_tarea.get().strip()
    if nombre == "" or fecha_entrega == "":
        return
    lista_tareas.append((nombre, fecha_entrega, "Pendiente"))
    tabla_tareas["insertar"]((nombre, fecha_entrega, "Pendiente"))
    campo_tareas.delete(0, "end")
    campo_fecha_tarea.delete(0, "end")
    actualizar_inicio()
    
def marcar_como_completada():
    fila = tabla_tareas["obtener_fila"]()
    if not fila:
        return
    indice = lista_tareas.index(fila)
    lista_tareas[indice] = (fila[0], fila[1], "✅ Completada")
    tabla_tareas["actualizar"](lista_tareas)
    actualizar_inicio()
    
def eliminar_tarea_tabla():
    fila = tabla_tareas["obtener_fila"]()
    if fila:
        lista_tareas.remove(fila)
        tabla_tareas["eliminar_seleccion"]()
        actualizar_inicio()

def editar_tarea():
    fila = tabla_tareas["obtener_fila"]()
    if fila:
        nombre, fecha_entrega, estado = fila
        campo_tareas.delete(0, "end")
        campo_tareas.insert(0, nombre)
        campo_fecha_tarea.delete(0, "end")
        campo_fecha_tarea.insert(0, fecha_entrega)
        eliminar_tarea_tabla() 
        
#---------------------------------
# HORARIO FUNCIONES
#---------------------------------
def seleccionar_celda(dia, hora):
    global celda_seleccionada

    if celda_seleccionada is not None:
        botones_horario[celda_seleccionada].configure(border_width=0)

    celda_seleccionada = (dia, hora)
    botones_horario[celda_seleccionada].configure(border_width=3, border_color=color_naranja)


def asignar_materia():
    if celda_seleccionada is None:
        return
    materia = menu_materias_horario.get()
    if materia == "":
        return
    boton = botones_horario[celda_seleccionada]
    boton.configure(text=materia, fg_color=color_rosita)


def vaciar_celda():
    if celda_seleccionada is None:
        return
    boton = botones_horario[celda_seleccionada]
    boton.configure(text="", fg_color=color_blanco)


def actualizar_menu_materias():
    nombres = [m[0] for m in lista_materias]
    if nombres:
        menu_materias_horario.configure(values=nombres)
        menu_materias_horario.set(nombres[0])
    else:
        menu_materias_horario.configure(values=["Sin materias"])
        
        
#==========================================================================================
# FRAME PRINCIPAL
#==========================================================================================
frame_principal= CTkFrame(master=ventana,
                          fg_color=transparente,
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
                        
boton_inicio.grid(row=1, column=0, sticky="news")

boton_MATERIAS= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="📚 MATERIAS",
                        command=lambda: ir_a_pestaña("MATERIAS"),
                        fg_color=transparente,
                        hover_color=color_azul_2
                        )
boton_MATERIAS.grid(row=2, column=0, sticky="nsew")

boton_tareas= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="📝 TAREAS",
                        fg_color=transparente,
                        command=lambda: ir_a_pestaña("TAREAS"),
                        hover_color=color_azul_2
                        )
boton_tareas.grid(row=3, column=0, sticky="ewns")

boton_horario= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="🕣 HORARIO",
                        fg_color=transparente,
                        command=lambda: ir_a_pestaña("HORARIO"),
                        hover_color=color_azul_2
                        )
boton_horario.grid(row=4, column=0, sticky="news")

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
boton_configuracion.grid(row=5, column=0, sticky="nsew")

boton_salir= CTkButton(master=frame_izquierdo,
                        **estilo_botones,
                        text="🚪 SALIR",
                        fg_color=transparente,
                        hover_color=color_azul_2,
                        command=ventana.destroy)
boton_salir.grid(row=6, column=0, sticky="news")

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
                    fg_color=color_azul_2,)

pestañas.grid(row=0,
              column=0,
              sticky="nsew",
              padx=0,
              pady=0)

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
pestaña_inicio.grid_rowconfigure(4, weight=1)
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

subtitulo_inicio = CTkLabel(master=pestaña_inicio,
                            text="Aquí tienes un resumen de tu día 🌸",
                            font=(NOMBRE_FUENTE, 16, "bold"),
                            text_color=color_blanco,
                            fg_color=transparente)
subtitulo_inicio.grid(row=1, column=0, sticky="n", pady=(0,5))

fecha= datetime.now().strftime( "%d/%m/%Y" )
label_fecha= CTkLabel(master=pestaña_inicio,
                      text=f"Fecha actual: {fecha}",
                      font=("Arial", 24, "bold"),
                      justify="center")
label_fecha.grid(row=2, column=0, sticky="ns")

frame_izquierdo_inferior_inicio=CTkFrame(master=pestaña_inicio,
                                         corner_radius=0, 
                                         fg_color=transparente)
frame_izquierdo_inferior_inicio.grid(row=3, column=0, sticky="nswe")
frame_izquierdo_inferior_inicio.grid_columnconfigure(0, weight=1)
frame_izquierdo_inferior_inicio.grid_columnconfigure(1, weight=1)
frame_izquierdo_inferior_inicio.grid_rowconfigure(0, weight=1)
frame_izquierdo_inferior_inicio.grid_rowconfigure(1, weight=1)

label_materia_inicio=CTkLabel(master=frame_izquierdo_inferior_inicio,
                              **estilo_etiquetas,
                              corner_radius=12,
                              fg_color=color_rosita,
                              text="Materias: 0")
label_materia_inicio.grid(row=0, column=0, padx=20, sticky="sw")

label_tareas_pen_inicio=CTkLabel(master=frame_izquierdo_inferior_inicio,
                                 **estilo_etiquetas,
                                 corner_radius=12,
                                 fg_color=color_naranja,
                                 text="Tareas pendientes: 0")
label_tareas_pen_inicio.grid(row=1, column=0, padx=20, sticky="ws")

tareas_proximas_inicio=CTkLabel(master=frame_izquierdo_inferior_inicio,
                                 width=300, 
                                 height=40,
                                 justify="center",
                                 font=(NOMBRE_FUENTE, 16, "bold"),
                                 text_color=color_blanco,
                                 fg_color=color_morado,
                                 text="Tareas a entregar proximamente:")
tareas_proximas_inicio.grid(row=0, column=1, sticky="es", padx=20)

datos_inicio_tareas_proxi=CTkLabel(master=frame_izquierdo_inferior_inicio,
                                   width=300,
                                   height=70,
                                   justify="center",
                                   anchor="center",
                                   font=(NOMBRE_FUENTE, 14, "bold"),
                                   text_color=color_negro,
                                   fg_color=color_blanco,
                                   text="")
datos_inicio_tareas_proxi.grid(row=1, column=1, sticky="sne", padx=20)
#==================================
# IMAGEN
#==================================

ruta_imagen = ruta_recursos("banner.jpg")

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
        row=4,
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
                                   width=90, 
                                   height=40,
                                   justify="center",
                                   font=(NOMBRE_FUENTE, 16, "bold"),
                                   text_color=color_blanco,
                                   fg_color=transparente,
                                   corner_radius=0,
                                   text="Materia:")
etiqueta_nombre_materia.grid(row=0, column=0, padx=10, pady=10)

campo_nombre_materia = CTkEntry(master=frame_form_materias,
                               width=190,
                      height=ALTURA_ESTANDAR_CAMPO,
                      fg_color=color_blanco,
                      text_color=color_negro,
                      border_color=color_negro,
                      justify="center",
                      corner_radius=0,
                      placeholder_text="",
                      font=(NOMBRE_FUENTE, TAMAÑO_LETRA_NORMAL))
campo_nombre_materia.grid(row=0, column=1, padx=10, pady=10)

etiqueta_profesor = CTkLabel(master=frame_form_materias,
                             width=90,
                             height=40,
                             justify="center",
                             font=(NOMBRE_FUENTE, 16, "bold"),
                             text_color=color_blanco,
                             fg_color=transparente,
                             corner_radius=0,
                             text="Profesor:")
etiqueta_profesor.grid(row=0, column=2, padx=10, pady=10)

campo_profesor = CTkEntry(master=frame_form_materias,
                          width=190,
                      height=ALTURA_ESTANDAR_CAMPO,
                      fg_color=color_blanco,
                      text_color=color_negro,
                      border_color=color_negro,
                      justify="center",
                      corner_radius=0,
                      placeholder_text="",
                      font=(NOMBRE_FUENTE, TAMAÑO_LETRA_NORMAL))
campo_profesor.grid(row=0, column=3, padx=10, pady=10)

boton_agregar_materia = CTkButton(master=frame_form_materias,
                                  **estilo_botones,
                                  text="➕ AGREGAR",
                                  fg_color=color_azul_2,
                                  hover_color=color_verde,
                                  command=agregar_materia)
                                  
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
                       hover_color=color_azul_2,
                       command=editar_materia)
boton_editar.grid(row=0, column=0, padx=10)
boton_eliminar=CTkButton(master=frame_botones_materias,
                         **estilo_botones,
                         fg_color=color_morado,
                         hover_color=color_azul_2,
                         text="🗑️ELIMINAR",
                         command=eliminar_materia_tabla)
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
frame_form_tareas.grid_columnconfigure(1, weight=2)
frame_form_tareas.grid_columnconfigure(2, weight=1)
frame_form_tareas.grid_columnconfigure(3, weight=2)
frame_form_tareas.grid_columnconfigure(4, weight=1)

etiqueta_tarea=CTkLabel(master=frame_form_tareas,
                        width=90, 
                        height=40,
                        justify="center",
                        font=(NOMBRE_FUENTE, 16, "bold"),
                        text_color=color_blanco,
                        fg_color=transparente,
                        corner_radius=0,
                        text="Tareas: ")
etiqueta_tarea.grid(row=0, column=0,padx=5, pady=10)
campo_tareas=CTkEntry(master=frame_form_tareas,
                      width=190,
                      height=ALTURA_ESTANDAR_CAMPO,
                      fg_color=color_blanco,
                      text_color=color_negro,
                      border_color=color_negro,
                      justify="center",
                      corner_radius=0,
                      placeholder_text="",
                      font=(NOMBRE_FUENTE, TAMAÑO_LETRA_NORMAL))
campo_tareas.grid(row=0, column=1,padx=5, pady=10,sticky="w")

etiqueta_entrega_fecha=CTkLabel(master=frame_form_tareas,
                                    width=135, 
                                    height=40,
                                    justify="center",
                                    font=(NOMBRE_FUENTE, 16, "bold"),
                                    text_color=color_blanco,
                                    fg_color=transparente,
                                    corner_radius=0,
                                    text="Fecha entrega: ")

etiqueta_entrega_fecha.grid(row=0, column=2,padx=5, pady=10)
campo_fecha_tarea=CTkEntry(master=frame_form_tareas,
                      width=190,
                      height=ALTURA_ESTANDAR_CAMPO,
                      fg_color=color_blanco,
                      border_color=color_negro,
                      text_color=color_negro,
                      justify="center",
                      corner_radius=0,
                      placeholder_text="",
                      font=(NOMBRE_FUENTE, TAMAÑO_LETRA_NORMAL))
campo_fecha_tarea.grid(row=0, column=3,padx=5, pady=10)

boton_agregar_tareas=CTkButton(master=frame_form_tareas,
                               **estilo_botones,
                               fg_color=color_azul_2,
                               hover_color=color_verde,
                               text="➕ Agregar",
                               command=agregar_tarea)
boton_agregar_tareas.grid(row=0, column=4, padx=5, pady=10, sticky="nswe")

tabla_tareas= CTkTable(master=frame_principal_tareas,
                       columnas=["Tarea", "Fecha entrega", "Estado"],
                       datos=[],
                       row=1,
                       column=0, 
                       padx=10,
                       pady=10,
                       sticky="nswe",
                       height=6)

frame_botones_tareas=CTkFrame(master=frame_principal_tareas,
                              corner_radius=0,
                              fg_color=transparente)
frame_botones_tareas.grid(row=2, column=0, sticky="nswe", padx=10)
frame_botones_tareas.grid_rowconfigure(0, weight=1)
frame_botones_tareas.grid_columnconfigure(0, weight=1)
frame_botones_tareas.grid_columnconfigure(1, weight=1)
frame_botones_tareas.grid_columnconfigure(2, weight=1)

boton_editar_tareas=CTkButton(master=frame_botones_tareas,
                              **estilo_botones,
                              fg_color=color_verde,
                              hover_color=color_azul_2,
                              text="✏️ EDITAR",
                              command=editar_tarea)
boton_editar_tareas.grid(row=0, column=0,padx=10, pady=10)

boton_tarea_completada=CTkButton(master=frame_botones_tareas,
                              **estilo_botones,
                              fg_color=color_naranja,
                              hover_color=color_azul_2,
                              text="✅ COMPLETADA",
                              command=lambda: marcar_como_completada())
boton_tarea_completada.grid(row=0, column=1,padx=10, pady=10)

boton_eliminar_tareas=CTkButton(master=frame_botones_tareas,
                              **estilo_botones,
                              fg_color=color_morado,
                              hover_color=color_azul_2,
                              text="🗑️ ELIMINAR",
                              command=eliminar_tarea_tabla)
boton_eliminar_tareas.grid(row=0, column=2,padx=10, pady=10)

#==========================================================================================
# PESTAÑA HORARIO
#========================================================================================== 
pestaña_horario=pestañas.add("HORARIO")
pestaña_horario.grid_columnconfigure(0, weight=1)
pestaña_horario.grid_rowconfigure(0, weight=1)
pestaña_horario.grid_rowconfigure(1, weight=20)
pestaña_horario.configure(fg_color=color_azul_2)

titiulo_horario= CTkLabel(master=pestaña_horario,
                          corner_radius=0,
                          fg_color=transparente,
                          text="Horario",
                          text_color=color_negro,
                          font=(letra_cursiva, 50, "bold"),
                          justify="center"
                          )
titiulo_horario.grid(row=0, column=0, sticky="n")  

frame_principal_horario = CTkFrame(master=pestaña_horario,
                                   corner_radius=10,
                                   fg_color=color_blanco)
frame_principal_horario.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
frame_principal_horario.grid_columnconfigure(0, weight=1)
frame_principal_horario.grid_rowconfigure(0, weight=0)
frame_principal_horario.grid_rowconfigure(1, weight=1)

horario_clases=[" 7:00 ", " 8:00 ", " 9:00 ", " 10:00 ", " 11:00 ", " 12:00 ", " 13:00 "]
dias_semana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
botones_horario={}
celda_seleccionada=None
#FRAME HORARIO-----------------------------------------------------------------------------
frame_form_horario = CTkFrame(master=frame_principal_horario,
                              corner_radius=10,
                              fg_color=color_rosita)
frame_form_horario.grid(row=0, column=0, sticky="new", padx=10, pady=10)
frame_form_horario.grid_columnconfigure(0, weight=2)
frame_form_horario.grid_columnconfigure(1, weight=1)
frame_form_horario.grid_columnconfigure(2, weight=1)
frame_form_horario.grid_columnconfigure(3, weight=1)

CTkLabel(master=frame_form_horario,
         text="Clic en celda, elige materia y asigna:",
         font=(NOMBRE_FUENTE, 14, "bold"),
         text_color=color_blanco,
         fg_color=transparente).grid(row=0, column=0, padx=10, pady=10)

menu_materias_horario = CTkOptionMenu(master=frame_form_horario,
                                      values=["Sin materias"],
                                      width=180,
                                      height=ALTURA_ESTANDAR_CAMPO,
                                      font=(NOMBRE_FUENTE, 14),
                                      fg_color=color_blanco,
                                      text_color=color_negro,
                                      button_color=color_azul_2)
menu_materias_horario.grid(row=0, column=1, padx=5, pady=10)

CTkButton(master=frame_form_horario,
          **estilo_botones,
          text="✅ Asignar",
          fg_color=color_azul_2,
          hover_color=color_verde,
          command=lambda: asignar_materia()).grid(row=0, column=2, padx=5, pady=10)

CTkButton(master=frame_form_horario,
          **estilo_botones,
          text="🗑️ Vaciar",
          fg_color=color_morado,
          hover_color=color_naranja,
          command=lambda: vaciar_celda()).grid(row=0, column=3, padx=5, pady=10)

frame_cuadricula_horario=CTkFrame(master=frame_principal_horario,
                                  corner_radius=0,
                                  fg_color=color_negro)
frame_cuadricula_horario.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
#DIAS
frame_cuadricula_horario.grid_columnconfigure(0, weight=2)  # Horas
frame_cuadricula_horario.grid_columnconfigure(1, weight=2)  # Lunes
frame_cuadricula_horario.grid_columnconfigure(2, weight=2)  # Martes
frame_cuadricula_horario.grid_columnconfigure(3, weight=2)  # Miércoles
frame_cuadricula_horario.grid_columnconfigure(4, weight=2)  # Jueves
frame_cuadricula_horario.grid_columnconfigure(5, weight=2)  # Viernes

# Filas de horario
frame_cuadricula_horario.grid_rowconfigure(0, weight=1) 
for i in range(1, len(horario_clases) + 1):
    frame_cuadricula_horario.grid_rowconfigure(i, weight=1)  # Filas de horario
    
etiqueta_esquina_horario = CTkLabel(master=frame_cuadricula_horario,
                                    text="Hora",
                                    fg_color=color_rosita,
                                    corner_radius=0,
                                    text_color=color_blanco,)
etiqueta_esquina_horario.grid(row=0, column=0, sticky="nswe", padx=1, pady=1)

for col, dia in enumerate(dias_semana, start=1):
    etiqueta_dia = CTkLabel(master=frame_cuadricula_horario,
                            text=dia,
                            font=(NOMBRE_FUENTE, 13, "bold"),
                            text_color=color_blanco,
                            fg_color=color_rosita,
                            corner_radius=0)
    etiqueta_dia.grid(row=0, column=col, sticky="nswe", padx=1, pady=1)

for fila, hora in enumerate(horario_clases, start=1):
    etiqueta_hora = CTkLabel(master=frame_cuadricula_horario,
                             text=hora,
                             font=(NOMBRE_FUENTE, 11, "bold"),
                             text_color=color_blanco,
                             fg_color=color_rosita,
                             corner_radius=0)
    etiqueta_hora.grid(row=fila, column=0, sticky="nswe", padx=1, pady=1)

#-------------------------------
for fila, hora in enumerate(horario_clases, start=1):
    for col, dia in enumerate(dias_semana, start=1):
        boton_celda_horario = CTkButton(master=frame_cuadricula_horario,
                                        text="",
                                        font=(NOMBRE_FUENTE, 11),
                                        fg_color=color_blanco,
                                        text_color=color_negro,
                                        hover_color=color_fondo,
                                        corner_radius=0,
                                        command=lambda d=dia, h=hora: seleccionar_celda(d, h))
        boton_celda_horario.grid(row=fila, column=col, sticky="nswe", padx=1, pady=1)
        botones_horario[(dia, hora)] = boton_celda_horario


for boton in botones_horario.values():
    boton.configure(border_width=2)
    boton.configure(border_width=0)

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

#---------------------------------
# CAMBIAR NOMBRE DE USUARIO
#---------------------------------
def guardar_nombre():
    nuevo = campo_nuevo_nombre.get().strip()
    if nuevo != "":
        titulo_bienvenida.configure(text=f"Bienvenida, {nuevo}")
        
frame_nombre_usuario = CTkFrame(master=frame_opciones, 
                                fg_color=transparente)
frame_nombre_usuario.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=15)
frame_nombre_usuario.grid_columnconfigure(0, weight=1)
frame_nombre_usuario.grid_columnconfigure(1, weight=1)
frame_nombre_usuario.grid_columnconfigure(2, weight=1)
frame_nombre_usuario.grid_rowconfigure(0, weight=1)

etiqueta_nombre_usuario = CTkLabel(master=frame_nombre_usuario,
                                   **estilo_etiquetas,
                                    fg_color=color_rosita,
                                    text="Nombre de usuario:")
etiqueta_nombre_usuario.grid(row=0, column=0, padx=5, pady=15, sticky="w")

campo_nuevo_nombre = CTkEntry(master=frame_nombre_usuario,
                              **estilo_campo,)
campo_nuevo_nombre.grid(row=0, column=1, pady=15, sticky="ew")

boton_guardar=CTkButton(master=frame_nombre_usuario,
          **estilo_botones,
          text="💾 Guardar",
          fg_color=color_rosita,
          hover_color=color_azul_2,
          command=guardar_nombre,
          anchor="w")
boton_guardar.grid(row=0, column=2, padx=5, pady=15, sticky="e")

#------------------------
#CAMBIAR TEMA
#------------------------
etiqueta_tema=CTkLabel(master=frame_opciones,
         **estilo_etiquetas,
         fg_color=color_rosita,
         text="Tema:").grid(row=1, column=0, padx=5, pady=15, sticky="e")

def cambiar_tema(opcion):
    set_appearance_mode(opcion)

selector_tema = CTkSegmentedButton(master=frame_opciones,
                                   width=350,
                                   height=50,
                                   values=["Light", "Dark", "System"],
                                   font=(NOMBRE_FUENTE, 18, "bold"),
                                   corner_radius=10,
                                   selected_color=color_naranja,
                                   selected_hover_color=color_azul_2,
                                   unselected_color=color_rosita,
                                   unselected_hover_color=color_morado,
                                   text_color=color_negro,
                                   command=cambiar_tema)
selector_tema.set("Light")
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
         fg_color=transparente,
         text_color=color_negro)
texto_acerca_de.grid(row=0, column=0, pady=(10, 2))

texto_configuracio=CTkLabel(master=frame_acerca,
         text="Organizador Escolar  •  Versión 1.0",
         font=(NOMBRE_FUENTE, 15),
         fg_color=transparente,
         text_color=color_negro)
texto_configuracio.grid(row=1, column=0, pady=2)

texto_desarrolado_por= CTkLabel(master=frame_acerca,
         text="Desarrollado por Abi 💜",
         font=(letra_cursiva, 15, "bold"),
         fg_color=transparente,
         text_color=color_negro)
texto_desarrolado_por.grid(row=2, column=0, pady=(2, 10))

pestañas._segmented_button.grid_forget()

#==========================================================================================
# 
#==========================================================================================

actualizar_menu_materias()         
actualizar_inicio()        
ventana.mainloop()
