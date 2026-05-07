from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("500x600")

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
frame_principal.grid_rowconfigure(1,weight=2)
frame_principal.grid_rowconfigure(2,weight=1)

#frame superior
frame_superior = CTkFrame(master=frame_principal,
                          fg_color="#2a00ac",
                          corner_radius=0)

frame_superior.grid(row=0,
                    column=0,
                    sticky="snew",
                    )

frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)

etiqueta_titulo = CTkLabel(master=frame_superior,
                           text="REGISTRO DE USUARIO",
                           height=150,
                           font=("Montserrat", 20, "bold"),
                           text_color="#ffffff")

etiqueta_titulo.grid(row=0,
                     column=0)

#frame datos

frame_datos = CTkFrame(master=frame_principal,
                        fg_color="transparent",
                        corner_radius=0,
                        )

frame_datos.grid(row=1,
                 column=0,
                 padx=10,
                 pady=10,
                 )

frame_datos.grid_columnconfigure(0, weight=1)

frame_datos.grid_rowconfigure(0, weight=1)
frame_datos.grid_rowconfigure(1, weight=1)
frame_datos.grid_rowconfigure(2, weight=1)
frame_datos.grid_rowconfigure(3, weight=1)
frame_datos.grid_rowconfigure(4, weight=1)
frame_datos.grid_rowconfigure(5, weight=1)

# NOMBRE etiqueta y campo

etiqueta_nombre = CTkLabel(master=frame_datos,
                           width=120,
                           height=50,
                           text="NOMBRE:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_nombre.grid(row=0,
                     column=0,
                     sticky="e",
                     pady = 5
                     )

campo_nombre = CTkEntry(master=frame_datos,
                        width=200,
                        height=50,
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
                           height=50,
                           text="CORREO:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_correo.grid(row=1,
                     column=0,
                     sticky="e",
                     pady = 5
                     )

campo_correo = CTkEntry(master=frame_datos,
                        width=200,
                        height=50,
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
                           height=50,
                           text="EDAD:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_edad.grid(row=2,
                     column=0,
                     sticky="e",
                     pady=5
                     )

campo_edad = CTkEntry(master=frame_datos,
                        width=200,
                        height=50,
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
                           height=50,
                           text="PAÍS:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_pais.grid(row=3,
                     column=0,
                     pady=5,
                     )

lista_paises = ["GUATEMALA", "ESPAÑA", "ALEMANIA", "MEXICO"]
pais_seleccionado = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=50,
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
    pady=5
)

# PROFESION etiqueta y menu de opciones

etiqueta_profesion = CTkLabel(master=frame_datos,
                           width=120,
                           height=50,
                           text="PROFESIÓN:",
                           font=("Montserrat", 16),
                           text_color="#ffffff",
                           fg_color="#81dc00")

etiqueta_profesion.grid(row=4,
                     column=0,
                     pady=5,
                     )

lista_profesion = ["INGENIERO", "DOCTOR", "ABOGADO", "DENTISTA"]
profecion = StringVar(value="Seleccione una Opción")
menu_opciones = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=50,
    fg_color="#2A00AC",
    text_color="#ffffff",
    button_color="#81dc00",
    dropdown_fg_color="#2a00ac",
    dropdown_text_color="#ffffff",
    dropdown_font=("Monstserat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_profesion,
    variable=profecion,
    font=("Montserrat", 16),
)

menu_opciones.grid(
    row=4,
    column=1,
    pady=5
)

# GENERO frame etiqueta y radio boton

frame_radius = CTkFrame(master=frame_datos,
                        fg_color="transparent",
                        )

frame_radius.grid(row=5,column=1, sticky="wn")

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
                     pady=5,
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
    pady=10, 
)
radio_Femenino.grid(
    row=1,
    column=0,
    pady=10
)
radio_otro.grid(
    row=2,
    column=0,
    pady=10
)




#frame inferior

frame_inferior = CTkFrame(master=frame_principal,
                          fg_color="transparent",
                          )

frame_inferior.grid(row=2,
                    column=0,
                    sticky="snew",
                    padx=10,
                    pady=10,)

frame_inferior.grid_columnconfigure(0, weight=1)

frame_inferior.grid_rowconfigure(0, weight=1)

ventana.mainloop()