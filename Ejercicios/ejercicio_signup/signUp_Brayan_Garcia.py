from customtkinter import *
set_appearance_mode("light")
set_default_color_theme("green")

def funcion_boton_1():
    nombre = campo_nombre.get()
    password = campo_pass.get()
    correo = campo_correo.get()
    edad = campo_edad.get()
    apellidos= campo_Apellido.get()
    apellido = campo_Telefono.get()
    if nombre == "":
        escribirAdvertencia("Nombre no puede estar vacio")
    print(f"Hola {nombre}, has hecho tu primera interfaz gráfica con CustomTkinter")
    
def escribirAdvertencia(advertencia=""):
    warning = CTkLabel (
        master=frame_btnWarning,
        fg_color="transparent",
        text="",
        font=("Montserrat", 16),
        text_color="#E40F0F",
    )
    warning.grid(row=1, column=0)    
ventana = CTk()
ventana.title("Titulo de la Ventana")
ventana.geometry("800x600")


ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           fg_color="#e3e5f3", 
                           corner_radius=0)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10,pady=10)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=3)
frame_principal.grid_rowconfigure(2, weight=1)

frame_datos = CTkFrame(master = frame_principal,
                       fg_color = "#DAEDF1",
                       corner_radius= 3
)

campos = []
frame_datos.grid(row=1, column=0, sticky="snew", padx=5, pady=5)
frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_columnconfigure(1, weight=1)
frame_datos.grid_rowconfigure(0, weight=1)
frame_datos.grid_rowconfigure(1, weight=1)
frame_datos.grid_rowconfigure(2, weight=1)
frame_datos.grid_rowconfigure(3, weight=1)
frame_datos.grid_rowconfigure(4, weight=1)
frame_datos.grid_rowconfigure(5, weight=1)

campo_nombre = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Nombre",
    font=("Montserrat", 16),
)
label_nombre = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Nombre",
    font=("Montserrat", 16),
)
campo_nombre.grid(column=1, row=0, sticky="w", padx=20)
label_nombre.grid(column=0, row= 0, sticky="e", padx=20)

campo_Apellido = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Apellido",
    font=("Montserrat", 16),
)
label_apellido = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Apellido",
    font=("Montserrat", 16),
)
campo_Apellido.grid(column=1, row=1, sticky="w", padx=20)
label_apellido.grid(column=0, row= 1, sticky="e", padx=20)
                  
campo_correo = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Correo",
    font=("Montserrat", 16),
)
label_correo = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Correo",
    font=("Montserrat", 16),
)
campo_correo.grid(column=1, row=2, sticky="w", padx=20)
label_correo.grid(column=0, row= 2, sticky="e", padx=20)

campo_Telefono = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Telefono",
    font=("Montserrat", 16),
)
label_telefono = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Telefono",
    font=("Montserrat", 16),
)
campo_Telefono.grid(column=1, row=3, sticky="w", padx=20)
label_telefono.grid(column=0, row= 3, sticky="e", padx=20)

campo_edad = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Edad",
    font=("Montserrat", 16),
)
label_edad = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Edad",
    font=("Montserrat", 16),
)

campo_edad.grid(column=1, row=4, sticky="w", padx=20)
label_edad.grid(column=0, row= 4, sticky="e", padx=20)

campo_pass = CTkEntry(
    master=frame_datos,
    width=180,
    corner_radius=0,
    placeholder_text="Contraseña",
    font=("Montserrat", 16),
)
label_pass = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="Contraseña",
    font=("Montserrat", 16),
)
campo_pass.grid(column=1, row=5, sticky="w", padx=20)
label_pass.grid(column=0, row=5, sticky="e", padx=20)

frame_btnWarning = CTkFrame(
    master = frame_principal,
    corner_radius=3,
    fg_color="#e3e5f3",
)

frame_btnWarning.rowconfigure(0, weight=1)
frame_btnWarning.rowconfigure(1, weight=1)
frame_btnWarning.columnconfigure(0, weight=1)
frame_btnWarning.grid(row=2, column=0)   
boton_1 = CTkButton(
    master=frame_btnWarning,
    width=100,
    height=40,
    fg_color="#2a00ac",
    hover_color= "#2751B3",
    corner_radius=0,
    text="HAZ CLICK",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_1,
)

boton_1.grid(row=0, column=0)
label_signUp = CTkLabel(
    master=frame_principal,
    fg_color="transparent",
    text="SING UP",
    font=("Montserrat", 23),
    text_color="#1167C9"
)
label_signUp.grid(row=0, column=0)
# campo_texto.grid(row=0, column=0)


ventana.mainloop()