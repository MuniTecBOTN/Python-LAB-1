from customtkinter import *

set_appearance_mode("light")
set_default_color_theme("green")

ventana = CTk()
ventana.title("Titulo de la Ventana")
ventana.geometry("480x600")


ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# 2a00ac
# e3e5f3
# 81dc00
frame_principal = CTkFrame(master=ventana,
                           fg_color="#e3e5f3", 
                           corner_radius=0)

frame_principal.grid(row=0, 
                     column=0, 
                     sticky="snew", 
                     padx=10,
                     pady=10)

frame_principal.grid_columnconfigure(0, weight=1)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
# código para crear un frame dentro del frame principal, para organizar mejor los widgets
frame_superior = CTkFrame(master=frame_principal,
                          fg_color="#2a00ac",
                          corner_radius=0
                          )
frame_superior.grid(row=0, 
                    column=0, 
                    sticky="snew", 
                    )
frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)

frame_datos = CTkFrame(master=frame_principal,
                       width=420,
                       fg_color="transparent",
                       corner_radius=0
                       )
frame_datos.grid(row=1,
                 column=0, 
                 sticky="sn", 
                 padx=10, 
                 pady=40)

frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_columnconfigure(1, weight=1)

frame_datos.grid_rowconfigure(0, weight=1, minsize=50)
frame_datos.grid_rowconfigure(1, weight=1, minsize=50)
frame_datos.grid_rowconfigure(2, weight=1, minsize=50)
frame_datos.grid_rowconfigure(3, weight=1, minsize=50)
frame_datos.grid_rowconfigure(4, weight=1, minsize=50)
frame_datos.grid_rowconfigure(5, weight=1, minsize=50)
frame_datos.grid_rowconfigure(6, weight=1, minsize=50)



etiqueta_titulo = CTkLabel(master=frame_superior,
                            text="REGISTRO DE USUARIO",
                            font=("Montserrat", 20, "bold"),
                            text_color="#ffffff"
                            )
etiqueta_titulo.grid(row=0, column=0)

etiequeta_nombre = CTkLabel(master=frame_datos,
                            width=120,  
                            height=30,
                            text="NOMBRE",
                            font=("Montserrat", 16),
                            text_color="#ffffff",
                            fg_color="#81dc00",
                            )
etiequeta_nombre.grid(row=0, 
                      column=0,
                      sticky="e" 
                      )

etiequeta_correo = CTkLabel(master=frame_datos,
                            width=120,
                            height=30,
                            text="CORREO:",
                            font=("Montserrat", 16),
                            text_color="#ffffff",
                            fg_color="#81dc00",
                            )
etiequeta_correo.grid(row=1, 
                      column=0, 
                      sticky="e"
                      )

etiequeta_edad = CTkLabel(master=frame_datos,
                            width=120,
                            height=30,
                            text="EDAD:",
                            font=("Montserrat", 16),
                            text_color="#ffffff",
                            fg_color="#81dc00",
                            )
etiequeta_edad.grid(row=2, 
                    column=0, 
                    sticky="e"
                    )
etiequeta_pais = CTkLabel(master=frame_datos,
                            width=120,
                            height=30,
                            text="PAÍS:",
                            font=("Montserrat", 16),
                            text_color="#ffffff",
                            fg_color="#81dc00",
                            )
etiequeta_pais.grid(row=3, 
                      column=0, 
                      sticky="e"
                      )
etiequeta_profesion = CTkLabel(master=frame_datos,
                            width=120,
                            height=30,
                            text="PROFESIÓN:",
                            font=("Montserrat", 16),
                            text_color="#ffffff",
                            fg_color="#81dc00",
                            )
etiequeta_profesion.grid(row=4, 
                         column=0, 
                         sticky="e"
                         )  

etiequeta_genero = CTkLabel(master=frame_datos,
                            width=120,
                            height=30,
                            text="GÉNERO:",
                            font=("Montserrat", 16),
                            text_color="#ffffff",
                            fg_color="#81dc00",
                            )
etiequeta_genero.grid(row=5, 
                         column=0, 
                         sticky="ne" 
                         )  

campo_nombre = CTkEntry(master=frame_datos,
                          width=200,
                          height=30,
                          border_color="#e3e5f3",
                          text_color="#2a00ac",
                          justify="center",
                          corner_radius=0,
                          placeholder_text="...",
                          font=("Montserrat", 16),
                          )
campo_nombre.grid(row=0, column=1,sticky="w")

campo_correo = CTkEntry(master=frame_datos,
                          width=200,
                          height=30,
                          border_color="#e3e5f3",
                          text_color="#2a00ac",
                          justify="center",
                          corner_radius=0,
                          placeholder_text="...",
                          font=("Montserrat", 16),
                          )
campo_correo.grid(row=1, column=1,sticky="w")

campo_edad = CTkEntry(master=frame_datos,
                          width=200,
                          height=30,
                          border_color="#e3e5f3",
                          text_color="#2a00ac",
                          justify="center",
                          corner_radius=0,
                          placeholder_text="...",
                          font=("Montserrat", 16),
                          )
campo_edad.grid(row=2, column=1,sticky="w")

lista_paises = ["ESPAÑA", "GUATEMALA", "ALEMANIA", "MEXICO"]
pais_selecionado = StringVar(value="SELECIONA")
menu_pais = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=30,
    fg_color="#FFFFFF",
    text_color="#2A00AC",
    button_color="#81dc00",
    dropdown_fg_color="#2A00AC",
    dropdown_text_color="#FFFFFF",
    dropdown_font=("Montserrat", 16),
    anchor="center",
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_paises,
    variable=pais_selecionado,
    font=("Montserrat", 16),
)

menu_pais.grid(
    row=3,
    column=1,
    sticky="w"
)

lista_profesiones = ["INGENIERO", "DOCTOR", "ABOGADO", "ARTISTA","TECNICO"]
profesion_selecionada = StringVar(value="SELECIONA")
menu_profesion = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=30,
    fg_color="#FFFFFF",
    text_color="#2A00AC",
    button_color="#81dc00",
    dropdown_fg_color="#2A00AC",
    dropdown_text_color="#FFFFFF",
    anchor="center",
    dropdown_font=("Montserrat", 16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_profesiones,
    variable=profesion_selecionada,
    font=("Montserrat", 16),
)


menu_profesion.grid(
    row=4,
    column=1,
    sticky="w"
)


frame_radios = CTkFrame(master=frame_datos,
                       fg_color="transparent",
                       corner_radius=0,
                       )    
frame_radios.grid(row=5,column=1,sticky="wn")

frame_radios.grid_columnconfigure(0, weight=1)
frame_radios.grid_rowconfigure(0, weight=1)
frame_radios.grid_rowconfigure(1, weight=1)
frame_radios.grid_rowconfigure(2, weight=1)


genero_selecionado = IntVar(value=0)
radio_femenino = CTkRadioButton(
    master=frame_radios,
    text="FEMENINO",
    value=1,
    variable=genero_selecionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
    border_color="#2a00ac",
    fg_color="#81dc00",
)
radio_masculino= CTkRadioButton(
    master=frame_radios,
    text="MASCULINO",
    value=2,
    variable=genero_selecionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
    border_color="#2a00ac",
    fg_color="#81dc00",
)
radio_otro= CTkRadioButton(
    master=frame_radios,
    text="OTRO",
    value=3,
    variable=genero_selecionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
    border_color="#2a00ac",
    fg_color="#81dc00",
)
radio_femenino.grid(
    row=0,
    column=0,
    sticky="w",
    padx=10
)
radio_masculino.grid(
    row=1,
    column=0,
    sticky="w",
    padx=10
)
radio_otro.grid(
    row=2,
    column=0,
    sticky="w",
    padx=10
)

boton_enviar = CTkButton(
    master=frame_datos,
    width=120,
    height=40,
    text="ENVIAR",
    fg_color="#2a00ac",
    hover_color="#81dc00",
    text_color="#ffffff",
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    )
boton_enviar.grid(
    row=6,
    column=0,
    sticky="w",
)
boton_limpiar = CTkButton(
    master=frame_datos,
    width=120,
    height=40,
    text="LIMPIAR",
    fg_color="#2a00ac",
    hover_color="#81dc00",
    text_color="#ffffff",
    font=("Montserrat", 16, "bold"),
    corner_radius=0,
    )
boton_limpiar.grid(
    row=6,
    column=1,
    sticky="e",
)
ventana.mainloop()