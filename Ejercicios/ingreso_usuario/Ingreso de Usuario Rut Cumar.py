from customtkinter import *

set_default_color_theme("dark-blue")
set_appearance_mode("light")

ventana = CTk()
ventana.title("Registro de Usuario")
ventana.geometry("500x700")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

#FRAME PRINCIPAL------------------------------------------------------------------------------
frame_principal= CTkFrame(master=ventana,
                          fg_color="#e3e5f3",
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)

#FRAME SUPERIOR------------------------------------------------------------------------------
frame_superior= CTkFrame(master=frame_principal,
                         fg_color="#2a00ac",
                         corner_radius=0)
frame_superior.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)

texto_superior = CTkLabel(master=frame_superior,
                          text="REGISTRO DE USUARIO",
                          font=("Montserrat", 20, "bold"),
                          text_color="#ffffff")

texto_superior.grid(row=0,column=0,)

#FRAME DATOS TEXTO ------------------------------------------------------------------------------

frame_datos= CTkFrame(master=frame_principal,
                      fg_color="transparent")
frame_datos.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_columnconfigure(1, weight=1)
frame_datos.grid_rowconfigure(0, weight=1)
frame_datos.grid_rowconfigure(1, weight=1)
frame_datos.grid_rowconfigure(2, weight=1)
frame_datos.grid_rowconfigure(3, weight=1)
frame_datos.grid_rowconfigure(4, weight=1)
frame_datos.grid_rowconfigure(5, weight=3)

#ETIQUETAS------------------------------------------------------------------------------
etiqueta_nombre= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="NOMBRE:",
                          font=("Montserrat", 16),
                          text_color="#ffffff",
                          fg_color="#81dc00"
                          )
etiqueta_nombre.grid( row=0, column=0, sticky="e")
etiqueta_correo= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="CORREO:",
                          font=("Montserrat", 16),
                          text_color="#ffffff",
                          fg_color="#81dc00"
                          )
etiqueta_correo.grid(row=1, column=0, sticky="e")
etiqueta_edad= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="EDAD:",
                          font=("Montserrat", 16),
                          text_color="#ffffff",
                          fg_color="#81dc00"
                          )
etiqueta_edad.grid( row=2, column=0, sticky="e")
etiqueta_pais= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="PAÍS:",
                          font=("Montserrat", 16),
                          text_color="#ffffff",
                          fg_color="#81dc00"
                          )
etiqueta_pais.grid (row=3, column=0, sticky="e")
etiqueta_profesion= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="PROFESIÓN:",
                          font=("Montserrat", 16),
                          text_color="#ffffff",
                          fg_color="#81dc00"
                          )
etiqueta_profesion.grid(row=4, column=0, sticky="e")
etiqueta_genero= CTkLabel(master=frame_datos,
                          width=120,
                          height=50,
                          text="GENERO:",
                          font=("Montserrat", 16),
                          text_color="#ffffff",
                          fg_color="#81dc00"
                          )
etiqueta_genero.grid(row=5, column=0, sticky="ne")

#FRAME DATOS------------------------------------------------------------------------------
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
campo_nombre.grid(row=0,column=1, sticky="w")
campo_correo = CTkEntry(
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
campo_correo.grid(row=1,column=1, sticky="w")
campo_edad = CTkEntry(
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
campo_edad.grid(row=2,column=1, sticky="w")

#LISTAS DESPLEGABLES------------------------------------------------------------------------------

lista_paises = ["GUATEMALA", "ESPAÑA", "ALEMANIA","MÉXICO"]
pais_seleccionado = StringVar(value="Selec. un País")
menu_paises = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=50,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_paises,
    variable=pais_seleccionado,
    fg_color="#2A00AC",
    text_color="#FFFFFF",
    button_color="#81dc00",
    button_hover_color="#81cf13",
    dropdown_fg_color="#2A00AC",
    dropdown_text_color="#ffffff",
    dropdown_font=("Montserrat",16),
    font=("Montserrat", 16)
)
menu_paises.grid(row=3,column=1,sticky="w")

lista_profesiones = ["PROGRAMADOR", "MEDICO", "ABOGADO","ARTISTA", "TECNICO", "INGENIERO"]
menu_profesion = StringVar(value="Selec. una Profesión")
menu_profesiones = CTkOptionMenu(
    master=frame_datos,
    width=200,
    height=50,
    fg_color="#2A00AC",
    text_color="#FFFFFF",
    button_color="#81dc00",
    button_hover_color="#81cf13",
    variable=menu_profesion,
    dropdown_fg_color="#2A00AC",
    dropdown_text_color="#ffffff",
    dropdown_font=("Montserrat",16),
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_profesiones,
    font=("Montserrat", 16)
)
menu_profesiones.grid(row=4,column=1,sticky="w")

#FRAME GENERO------------------------------------------------------------------------------

frame_genero= CTkFrame(master=frame_datos,
                       corner_radius=0,
                       fg_color="#e3e5f3",
                       width=400)
frame_genero.grid(row=5, column=1, sticky="wn")

frame_genero.grid_columnconfigure(0, weight=1)
frame_genero.grid_rowconfigure(0, weight=1)
frame_genero.grid_rowconfigure(1, weight=1)
frame_genero.grid_rowconfigure(2, weight=1)

genero_seleccionado= IntVar(value=0)
radio_femenino = CTkRadioButton(
    master=frame_genero,
    text="FEMENINO",
    value=1,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    border_color="#2A00AC",
    text_color="#2A00AC"
)
radio_masculino = CTkRadioButton(
    master=frame_genero,
    text="MASCULINO",
    value=2,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    border_color="#2A00AC",
    text_color="#2A00AC"
)
radio_otro = CTkRadioButton(
    master=frame_genero,
    text="OTRO",
    value=3,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    border_color="#2A00AC",
    text_color="#2A00AC"
)

radio_femenino.grid(
    row=0,
    column=0,
    sticky="wn",
    padx=10
)
radio_masculino.grid(
    row=1,
    column=0,
    sticky="wn",
    padx=10,
    pady=5
)
radio_otro.grid(
    row=2,
    column=0,
    sticky="wn",
    padx=10
)

#FRAME INFERIOR------------------------------------------------------------------------------
frame_inferior= CTkFrame(master=frame_principal,
                         fg_color="transparent")

frame_inferior.grid(row=2, column=0, sticky="senw", padx=10, pady=10)
frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)

boton_1 = CTkButton (master=frame_inferior,
                    width=120,
                    height=60,
                    corner_radius=0,
                    fg_color="#2a00ac",
                    hover_color="#3811b0",
                    text="Enviar",
                    anchor="center",
                    font=("Montserrat", 16))
boton_1.grid( row=0, column=0,)

boton_2 = CTkButton (master=frame_inferior,
                    width=120,
                    height=60,
                    corner_radius=0,
                    fg_color="#2a00ac",
                    hover_color="#3811b0",
                    text="Limpiar",
                    anchor="center",
                    font=("Montserrat", 16))
boton_2.grid( row=0, column=1,)


ventana.mainloop()



#2a00ac    e3e5f3    81dc00