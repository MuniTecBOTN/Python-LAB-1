import os
from customtkinter import *
from PIL import Image
from pygame import mixer
from mutagen.mp3 import MP3
from tkinter import Canvas
import random
from math import sin
from PIL import Image, ImageTk
set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("MP3 de Alisson")
ventana.geometry("580x950")
ventana.resizable(False, False)
#colores y estilos
rojo="#780606"
blanco="#FFFFFF"
verde="#00674f"
crema="#E5D9C6"
negro="#000000"
transparente="transparent"
boton={
    "width":80,
    "height":30,
    "corner_radius":0,
    "anchor":"center",
    "font": ("Montserrat", 16, "bold")
    
}

boton_volumen={
    "width":120,
    "height":80,
    "corner_radius":0,
    "anchor":"center",
    "font": ("Montserrat", 26, "bold")
}

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)
mixer.init()
#variables globales
offset_reproduccion = 0
duracion_actual = 0
indice_actual = 0
volumen = 0.9
pausado = False
cambiando_progreso= False
ruta_script = os.path.dirname(os.path.abspath(__file__))
# dicionario con las canciones
playlist = [
    ("Adolescent's Orquesta - Virgen", "virgen.jpg"),
    ("Francés Limón - Enanitos Verdes", "limon.jpg"),
    ("Ghost - Mary On A Cross", "ghost.jpg"),
    ("Josean Log - Doma", "doma.jpg"),
    ("La Maquinaria Norteña - Eres Ese Algo", "maquinaria.jpg"),
    ("La Mosca Tse Tse - Para no verte más", "lamosca.jpg"),
    ("Los Auténticos Decadentes - Loco", "tuformadeser.jpg"),
    ("Mon Laferte - Otra Noche de Llorar", "monlafter.jpg"),
    ("Romeo Santos - Imitadora", "imitadora.jpg"),
    ("Willian - Sol", "william-sol.jpg"),
]
# funciones
def cargar_cancion(indice):
    global portada
    global offset_reproduccion
    offset_reproduccion = 0
    barra.set(0)
    mp3 = os.path.join(
        ruta_script,
        "canciones",
        f"{playlist[indice][0]}.mp3"
    )

    imagen = os.path.join(
        ruta_script,
        "imagenes",
        playlist[indice][1]
    )

    mixer.music.load(mp3)
    global duracion_actual

    duracion_actual = MP3(mp3).info.length

    portada = CTkImage(
        light_image=Image.open(imagen),
        dark_image=Image.open(imagen),
        size=(500, 400)
    )

    etiqueta_imagen.configure(image=portada)

    label_cancion.configure(
        text=playlist[indice][0].replace(".mp3", "")
    )

def mover_cursor(valor):
    global cambiando_progreso
    cambiando_progreso = True
    
def mover_cancion(event=None):
    global offset_reproduccion
    global duracion_actual
    global cambiando_progreso

    if duracion_actual <= 0:
        return

    valor = barra.get()

    posicion_segundos = (
        valor / 100
    ) * duracion_actual

    mixer.music.play(
        start=posicion_segundos
    )

    global pausado
    pausado = False
    offset_reproduccion = posicion_segundos
    
    cambiando_progreso = False
    
def reproducir_pausar():
    global pausado

    if not mixer.music.get_busy() and not pausado:
        mixer.music.play()
        return

    if pausado:
        mixer.music.unpause()
        pausado = False
    else:
        mixer.music.pause()
        pausado = True

def siguiente():
    global indice_actual

    indice_actual += 1

    if indice_actual >= len(playlist):
        indice_actual = 0

    cargar_cancion(indice_actual)
    mixer.music.play()

def anterior():
    global indice_actual

    indice_actual -= 1

    if indice_actual < 0:
        indice_actual = len(playlist) - 1

    cargar_cancion(indice_actual)
    mixer.music.play()
def subir_volumen():
    global volumen

    volumen += 0.3

    if volumen > 1:
        volumen = 1

    mixer.music.set_volume(volumen)


def bajar_volumen():
    global volumen

    volumen -= 0.1

    if volumen < 0:
        volumen = 0

    mixer.music.set_volume(volumen)

def actualizar_barra():
    global duracion_actual
    duracion = duracion_actual
    posicion = (offset_reproduccion + mixer.music.get_pos() / 1000)
    porcentaje = (posicion / duracion) * 100
    if porcentaje>=100:
        porcentaje = 0
    if not cambiando_progreso:
        barra.set(porcentaje)
            
    ventana.after(1000, actualizar_barra)




def verificar_fin():
    if not mixer.music.get_busy() and not pausado:
        siguiente()

    ventana.after(1000, verificar_fin)



def crear_petalo():



    x = random.randint(150, 350)

    imagen = random.choice(
        imagenes_petalos
    )

    petalo = canvas_rosas.create_image(
        x,
        20,
        image=imagen
    )

    petalos.append({
        "id": petalo,
        "fase": random.uniform(0, 6.28),
        "imagen": imagen
    })

def animar_rosas():

    if mixer.music.get_busy():

        if random.random() < 0.15:
            crear_petalo()

    for petalo in petalos[:]:

        coords = canvas_rosas.coords(
            petalo["id"]
        )

        if not coords:
            continue

        x,y = coords

        petalo["fase"] += 0.1

        dx = sin(
        petalo["fase"]
)       * random.uniform(1.5, 3)
        
        dy = random.uniform(1.5, 3)

        canvas_rosas.move(
            petalo["id"],
            dx,
            dy
        )

        if y > 130:

            canvas_rosas.delete(
                petalo["id"]
            )

            petalos.remove(
                petalo
            )

    ventana.after(
        30,
        animar_rosas
    )


def abrir_reproductor():

    frame_bienvenida.grid_remove()

    frame_principal.grid()

    cargar_cancion(0)

    mixer.music.play()

    actualizar_barra()

    verificar_fin()

    animar_rosas()

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_bienvenida=CTkFrame(master=ventana,
                      fg_color=crema,
                      corner_radius=20)
frame_bienvenida.grid(row=0,
                      column=0,
                      sticky="nsew",
                      padx=20,
                      pady=20)
frame_bienvenida.grid_columnconfigure(0, weight=1)
frame_bienvenida.grid_rowconfigure(0, weight=1)
frame_bienvenida.grid_rowconfigure(1, weight=1)
frame_bienvenida.grid_rowconfigure(2, weight=1)

frame_principal=CTkFrame(master=ventana,
                        fg_color=rojo,
                        corner_radius=20)

frame_principal.grid(row=0, 
                     column=0, 
                     sticky="nsew", 
                     padx=20,
                     pady=20)
frame_principal.grid_remove()
frame_principal.grid_columnconfigure(0, weight=1)


frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)

frame_musica=CTkFrame(master=frame_principal,
                      fg_color=rojo,
                      corner_radius=20)
frame_musica.grid(row=0,column=0,sticky="nsew",padx=20,pady=20)
frame_musica.grid_columnconfigure(0,weight=1)
frame_musica.grid_rowconfigure([0,1,2,3], weight=1)
frame_controles=CTkFrame(master=frame_principal,
                         fg_color=verde,
                         corner_radius=1200)
frame_controles.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
frame_controles.grid_columnconfigure(0,weight=1)
frame_controles.grid_columnconfigure(1,weight=1)
frame_controles.grid_columnconfigure(2,weight=1)
frame_controles.grid_rowconfigure(0,weight=1)
frame_controles.grid_rowconfigure(1,weight=1)  
frame_controles.grid_rowconfigure(2,weight=1)

# =========================================================
# CARGAR IMAGEN
# =========================================================
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(ruta_script, "imagenes/doma.jpg")  


# Cargar imagen
imagen_cancion = CTkImage(
    light_image=Image.open(ruta_imagen),  
    dark_image=Image.open(ruta_imagen),   
    size=(500, 400),

)


ruta_arbol = os.path.join(
    ruta_script,
    "imagenes",
    "arbol.png"
)

imagen_arbol = Image.open(ruta_arbol)

imagen_arbol = imagen_arbol.resize(
    (500, 120)
)

arbol_tk = ImageTk.PhotoImage(
    imagen_arbol
)


ruta_petalo1 = os.path.join(
    ruta_script,
    "imagenes",
    "petalo1.png"
)

ruta_petalo2 = os.path.join(
    ruta_script,
    "imagenes",
    "petalo2.png"
)

ruta_petalo3 = os.path.join(
    ruta_script,
    "imagenes",
    "petalo3.png"
)

petalo1_img = ImageTk.PhotoImage(
    Image.open(ruta_petalo1).resize((20,20))
)

petalo2_img = ImageTk.PhotoImage(
    Image.open(ruta_petalo2).resize((20,20))
)

petalo3_img = ImageTk.PhotoImage(
    Image.open(ruta_petalo3).resize((20,20))
)

imagenes_petalos = [
    petalo1_img,
    petalo2_img,
    petalo3_img
]

#widgets
label_cancion = CTkLabel(
    frame_musica,
    text="",
    text_color="black",
    font=("Montserrat", 18, "bold")
)
label_cancion.grid(row=1, column=0, pady=10)



canvas_rosas = Canvas(
    frame_musica,
    width=500,
    height=120,
    bg="white",
    highlightthickness=0
)

canvas_rosas.grid(
    row=2,
    column=0,
    pady=5
)
canvas_rosas.create_image(
    0,
    0,
    image=arbol_tk,
    anchor="nw"
)




petalos = []

etiqueta_imagen = CTkLabel(
    master=frame_musica,
    image=imagen_cancion,  
    text="",
    
)
etiqueta_imagen.grid(
    row=0,
    column=0,
    sticky="nsew",
    
)



barra = CTkSlider(
    frame_musica,
    from_=0,
    to=100,
    progress_color="#c96f00",   
    button_color="#ff7b00",     
    button_hover_color="#ff9900", 
    fg_color="#2b2b2b",
    command=mover_cursor        
)

barra.grid(
    row=3,
    column=0,
    sticky="ew",
    padx=20,
    pady=10
)

barra.set(0)
barra.bind("<ButtonRelease-1>",
    mover_cancion)
#botones
boton_pausarepoducir = CTkButton(
    master=frame_controles,
    text="pausa/reproducir",
    fg_color=transparente,
    text_color=blanco,
    **boton,
    command=reproducir_pausar
)

boton_pausarepoducir.grid(
    row=1,
    column=1,
)
boton_suma=CTkButton(
    master=frame_controles,
    text="+",
    fg_color=transparente,
    text_color=blanco,
    **boton_volumen,
    command=subir_volumen
)

boton_suma.grid(row=0,column=1)

boton_resta=CTkButton(
    master=frame_controles,
    text="-",
    fg_color=transparente,
    text_color=blanco,
    **boton_volumen,
    command=bajar_volumen
)
boton_resta.grid(
    row=2,
    column=1
)

boton_anterior=CTkButton(
    master=frame_controles,
    text="anterior",
    fg_color=transparente,
    text_color=blanco,
    **boton,
    command=anterior
)
boton_anterior.grid(
    row=1,
    column=0,
   
)

boton_siguiente=CTkButton(
    master=frame_controles,
    text="siguiente",
    fg_color=transparente,
    text_color=blanco,
    **boton,
    command=siguiente
)
boton_siguiente.grid(
    row=1,
    column=2,
    
)
label_bienvenida = CTkLabel(
    frame_bienvenida,
    text="Para Alisson con mucho cariño",
    text_color=negro,

    font=("Montserrat", 24, "bold")
)
label_bienvenida.grid(
    row=0,
    column=0,
    padx=20,
    pady=20
)
label_descripcion = CTkLabel(
    frame_bienvenida,
    text="""
Qué tal, Ali.

Espero que te guste este pequeño reproductor de música que hice para ti.

Aquí encontrarás algunas canciones que sé que te gustan y otras que descubrí en el camino y que, por alguna razón, me hicieron pensar en ti. Cada una tiene algo especial y forma parte de esta pequeña colección que preparé.

No es algo muy grande, pero sí está hecho con dedicación. Así que relájate, disfruta la música y 

Cuando estés lista, presiona el botón "Entrar".
""",
    text_color=negro,
    wraplength=250,
    font=("Montserrat", 18, "bold")
)
label_descripcion.grid(
    row=1,
    column=0,
    padx=20,
    pady=20
)
boton_entrar = CTkButton(
    frame_bienvenida,
    text="🍂 Entrar 🍂",
    command=abrir_reproductor
)

boton_entrar.grid(
    row=2,
    column=0,
    padx=20,
    pady=20
)


mixer.music.set_volume(0.5)

ventana.mainloop()