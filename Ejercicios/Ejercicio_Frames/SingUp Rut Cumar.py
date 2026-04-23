from customtkinter import *
set_appearance_mode("dark")
set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("600x800")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

#Frame principal------------------------------------------------------------------------------
frame_principal= CTkFrame(master=ventana,
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=10)
frame_principal.grid_rowconfigure(2, weight=1)

#Frame Titulo------------------------------------------------------------------------------

frame_titulo=CTkFrame(master=frame_principal,
                     corner_radius=0)
frame_titulo.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(0, weight=1)

etiqueta_titulo = CTkLabel(
    master=frame_titulo,
    fg_color="transparent",
    text="SINGUP",
    font=("Montserrat", 24),
)
etiqueta_titulo.grid(row=0,column=0,)

#Frame Datos------------------------------------------------------------------------------

frame_datos= CTkFrame(master=frame_principal,
                      corner_radius=0)
frame_datos.grid(row=1, column=0, sticky= "nsew", padx=10, pady=10)
frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_columnconfigure(1, weight=1)
frame_datos.grid_rowconfigure(0, weight=1)
frame_datos.grid_rowconfigure(1, weight=1)
frame_datos.grid_rowconfigure(2, weight=1)
frame_datos.grid_rowconfigure(3, weight=1)
frame_datos.grid_rowconfigure(4, weight=1)
frame_datos.grid_rowconfigure(5, weight=1)

campo_texto = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Escriba su nombre...",
    font=("Montserrat", 16),
)
#Ingresar texto------------------------------------------------------------------------------
campo_texto.grid(row=0, column=1, sticky="w", pady=15)
campo_texto = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Escriba su apellido...",
    font=("Montserrat", 16),
)
campo_texto.grid(row=1, column=1, sticky="w", pady=15)
campo_texto = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Escriba su correo...",
    font=("Montserrat", 16),
)
campo_texto.grid(row=2, column=1, sticky="w", pady=15)
campo_texto = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Escriba su telefono...",
    font=("Montserrat", 16),
)
campo_texto.grid(row=3, column=1, sticky="w", pady=15)
campo_texto = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Escriba su edad...",
    font=("Montserrat", 16),
)
campo_texto.grid(row=4, column=1,sticky="w", pady=15)
campo_texto = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Escriba su Contraseña...",
    font=("Montserrat", 16),
)
campo_texto.grid(row=5, column=1, sticky="w", pady=15)
#nombres------------------------------------------------------------------------------
etiqueta_nom = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Nombre",
    font=("Montserrat", 16),
)
etiqueta_nom.grid(row=0,column=0,sticky ="e",padx=20)
etiqueta_ape = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Apellido",
    font=("Montserrat", 16),
)
etiqueta_ape.grid(row=1,column=0,sticky ="e",padx=20)
etiqueta_correo = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Correo",
    font=("Montserrat", 16),
)
etiqueta_correo.grid(row=2,column=0,sticky ="e",padx=20)
etiqueta_tele = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Telefono",
    font=("Montserrat", 16),
)
etiqueta_tele.grid(row=3,column=0,sticky ="e",padx=20)
etiqueta_edad = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Edad",
    font=("Montserrat", 16),
)
etiqueta_edad.grid(row=4,column=0,sticky ="e",padx=20)
etiqueta_cont = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Contraseña",
    font=("Montserrat", 16)
    )
etiqueta_cont.grid(row=5,column=0,sticky ="e",padx=20)

#Frame boton------------------------------------------------------------------------------
frame_boton= CTkFrame(master=frame_principal,
                      corner_radius=0)
frame_boton.grid(row=2, column=0, sticky= "nsew", padx=10, pady=10)
frame_boton.grid_columnconfigure(0, weight=1)
frame_boton.grid_rowconfigure(0, weight=1)
def funcion_boton_1():
    print(f"Has presionado el Botón 1")

boton_1 = CTkButton(master=frame_boton,
                    width=80,
                    height=30,
                    corner_radius=0,
                    fg_color="#3a86ff",
                    hover_color="#265df2",
                    text="Aceptar",
                    anchor="center",
                    font=("Montserrat", 16),
                    command=funcion_boton_1)
boton_1.grid( row=0, column=0,)

ventana.mainloop()