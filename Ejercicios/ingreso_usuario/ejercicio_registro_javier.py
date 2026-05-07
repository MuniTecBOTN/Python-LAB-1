from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("480x640")

# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)

# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           fg_color="#e3e5f3",
                           corner_radius=0)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10, pady=10)

frame_principal.grid_columnconfigure(0,weight=1)


frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_rowconfigure(1,weight=1)
frame_principal.grid_rowconfigure(2,weight=1)

#frame superior
frame_superior = CTkFrame(master=frame_principal,
                          fg_color="#2a00ac",
                          height=80,
                          corner_radius=0)

frame_superior.grid(row=0,
                    column=0,
                    sticky="ew",
                    )

frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)

etiqueta_titulo = CTkLabel(master=frame_superior,
                           text="REGISTRO DE USUARIO",
                           height=80,
                           font=("Montserrat", 20, "bold"),
                           text_color="#ffffff")

etiqueta_titulo.grid(row=0,
                     column=0,
                     sticky="snew",)

#frame datos

frame_datos = CTkFrame(master=frame_principal,
                        fg_color="transparent",
                        corner_radius=0,

                        )

frame_datos.grid(row=1,
                 column=0,
                 sticky="ns",
                 padx=10,
                 )

frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_columnconfigure(1, weight=1)

frame_datos.grid_rowconfigure(0, weight=1, minsize=50)
frame_datos.grid_rowconfigure(1, weight=1, minsize=50)
frame_datos.grid_rowconfigure(2, weight=1, minsize=50)
frame_datos.grid_rowconfigure(3, weight=1, minsize=50)
frame_datos.grid_rowconfigure(4, weight=1, minsize=50)
frame_datos.grid_rowconfigure(5, weight=1, minsize=50)
frame_datos.grid_rowconfigure(6, weight=1, minsize=50)

# ------------------ FUNCIONES ---------------

def capturar_datos():
    nombre = campo_nombre.get().strip().lower()
    correo = campo_correo.get().strip().lower()
    edad = campo_edad.get().strip()
    pais = pais_seleccionado.get().strip()
    profesion = profesion_seleccionada.get().strip()
    genero = genero_seleccionado.get() 
    
    #------ Validaciones de Nombre ----------------
    if(not nombre
       or not correo
       or not edad
       or pais == "Seleccione una Opción"
       or genero == 0):
        etiqueta_informacion.configure(text="Por favor, completa todos los campos")
        etiqueta_informacion.after(3000, lambda: etiqueta_informacion.configure(text=""))
        return
    
    if not nombre.replace(" ","").isalpha():
        etiqueta_informacion.configure(text="El nombre no puede contener núneros")
        etiqueta_informacion.after(2000, lambda:etiqueta_informacion.configure(text=""))
        return

    if len(nombre) < 3:
        etiqueta_informacion.configure(text= "El nombre debe tener al menos 3 caracteres")
        etiqueta_informacion.after(2000, lambda: etiqueta_informacion.configure(text=""))
        return
    
    #------------------- Validacion de correo ------------------
    
    lista_extenciones_validas = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@outlook.com"]
    if not correo.endswith(tuple(lista_extenciones_validas)):
        etiqueta_informacion.configure(text="por favor ingrese un correo valido.")
        etiqueta_informacion.after(2000, lambda:etiqueta_informacion.configure(text=""))
        campo_correo.configure(border_color="#ff0000")
        campo_correo.after(2000, lambda: campo_correo.configure(border_color="#e3e5f3"))
        return

#------------------- Validacion de edad ------------------

    if len(edad) > 3:
        etiqueta_informacion.configure(text= "La edad no puede tener 3 caracteres")
        etiqueta_informacion.after(2000, lambda: etiqueta_informacion.configure(text=""))
        return
    
def limpiar():
    campo_nombre.delete(0, "end")
    campo_correo.delete(0, "end")
    campo_edad.delete(0, "end")
    pais_seleccionado.set("Seleccione una Opción")
    profesion_seleccionada.set("Seleccione una Opción")
    genero_seleccionado.set(0)
    etiqueta_informacion.configure(text="")

# NOMBRE etiqueta y campo

etiqueta_nombre = CTkLabel(master=frame_datos,
                           width=120,
                           height=30,
                           text="NOMBRE:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_nombre.grid(row=0,
                     column=0,
                     sticky="e",
                     )

campo_nombre = CTkEntry(master=frame_datos,
                        width=200,
                        height=30,
                        border_color="#e3e5f3",
                        text_color="#2a00ac",
                        justify= "center",
                        corner_radius=0,
                        placeholder_text="...",
                        font=("Montserrat", 16),
                        )

campo_nombre.grid(row=0,column=1,sticky="w",pady = 5)

# CORREO etiqueta y campo

etiqueta_correo = CTkLabel(master=frame_datos,
                           width=120,
                           height=30,
                           text="CORREO:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_correo.grid(row=1,
                     column=0,
                     sticky="e",
                     )

campo_correo = CTkEntry(master=frame_datos,
                        width=200,
                        height=30,
                        border_color="#e3e5f3",
                        text_color="#2a00ac",
                        justify= "center",
                        corner_radius=0,
                        placeholder_text="...",
                        font=("Montserrat", 16),
                        )

campo_correo.grid(row=1,column=1,sticky="w")

#EDAD etiqueta y campo

etiqueta_edad = CTkLabel(master=frame_datos,
                           width=120,
                           height=30,
                           text="EDAD:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_edad.grid(row=2,
                     column=0,
                     sticky="e",
                     )

campo_edad = CTkEntry(master=frame_datos,
                        width=200,
                        height=30,
                        border_color="#e3e5f3",
                        text_color="#2a00ac",
                        justify= "center",
                        corner_radius=0,
                        placeholder_text="...",
                        font=("Montserrat", 16),
                        )

campo_edad.grid(row=2,column=1,sticky="w")

# PAIS etiqueta y menu de opciones

etiqueta_pais = CTkLabel(master=frame_datos,
                           width=120,
                           height=30,
                           text="PAÍS:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_pais.grid(row=3,
                     column=0,
                     )

lista_paises = ["GUATEMALA", "ESPAÑA", "ALEMANIA", "MEXICO"]
pais_seleccionado = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=30,
    fg_color="#2A00AC",
    text_color="#ffffff",
    button_color="#81dc00",
    dropdown_fg_color="#2a00ac",
    dropdown_text_color="#ffffff",
    dropdown_font=("Monstserat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_paises,
    variable=pais_seleccionado,
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=3,
    column=1,
)

# PROFESION etiqueta y menu de opciones

etiqueta_profesion = CTkLabel(master=frame_datos,
                           width=120,
                           height=30,
                           text="PROFESIÓN:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_profesion.grid(row=4,
                     column=0,
                     )

lista_profesion = ["INGENIERO", "DOCTOR", "ABOGADO", "DENTISTA"]
profesion_seleccionada = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=30,
    fg_color="#2A00AC",
    text_color="#ffffff",
    button_color="#81dc00",
    dropdown_fg_color="#2a00ac",
    dropdown_text_color="#ffffff",
    dropdown_font=("Monstserat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_profesion,
    variable=profesion_seleccionada,
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=4,
    column=1,
)

# GENERO frame etiqueta y radio boton

frame_radius = CTkFrame(master=frame_datos,
                        fg_color="transparent",
                        )

frame_radius.grid(row=5,column=1, sticky="sn")

frame_radius.grid_columnconfigure(0, weight=1)

frame_radius.grid_rowconfigure(0, weight=1)
frame_radius.grid_rowconfigure(1, weight=1)
frame_radius.grid_rowconfigure(2, weight=1)

etiqueta_genero = CTkLabel(master=frame_datos,
                           width=120,
                           height=30,
                           text="GENERO:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_genero.grid(row=5,
                     column=0,
                     )


genero_seleccionado = IntVar(value=0)

radio_Masculino = CTkRadioButton(
    master=frame_radius,
    text="Masculino",
    value=1,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
    
)
radio_Femenino = CTkRadioButton(
    master=frame_radius,
    text="Femenino",
    value=2,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
)
radio_otro =CTkRadioButton(
    master=frame_radius,
    text="Otro",
    value=3,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
)

radio_Masculino.grid(
    row=0,
    column=0,
)
radio_Femenino.grid(
    row=1,
    column=0,
)
radio_otro.grid(
    row=2,
    column=0,
)




#frame inferior

frame_inferior = CTkFrame(master=frame_principal,
                          fg_color="transparent",
                          )

frame_inferior.grid(row=2,
                    column=0,
                    sticky="s",
                    padx=10,
                    pady=10,)

frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1, weight=1)

frame_inferior.grid_rowconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(1, weight=1)

# ------------------ BOTONES ------------------
boton_enviar = CTkButton(
    master=frame_inferior,
    width=120,
    height=30,
    text="ENVIAR",
    fg_color="#2a00ac",
    hover_color="#81dc00",
    text_color="#ffffff",
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    command= capturar_datos,
)
boton_enviar.grid(row=0, column=0, sticky="w")

boton_limpiar = CTkButton(
    master=frame_inferior,
    width=120,
    height=30,
    text="LIMPIAR",
    fg_color="#2a00ac",
    hover_color="#81dc00",
    text_color="#ffffff",
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    command= limpiar,
)
boton_limpiar.grid(row=0, column=1, sticky="e")

#----------etiqueta de informacion----------------------

etiqueta_informacion= CTkLabel(
    master=frame_inferior,
    width=300,
    height=80,
    text="Hola",
    font=("Montserrat", 16,"bold"),
    text_color="#223ac2",
    fg_color="transparent"
    
)
etiqueta_informacion.grid(row = 1, column = 0,columnspan=2, sticky="nsew")

ventana.mainloop()