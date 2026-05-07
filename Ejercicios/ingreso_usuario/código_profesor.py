from customtkinter import *
# ------------------ CONFIGURACIÓN ------------------
set_appearance_mode("light")
set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Sign Up")
ventana.geometry("480x600")

# ------------------ GRID PRINCIPAL ------------------
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

# ------------------ FRAME PRINCIPAL ------------------
frame_principal = CTkFrame(master=ventana, fg_color="#e3e5f3", corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)

# ------------------ FRAME TÍTULO ------------------
frame_titulo = CTkFrame(master=frame_principal, height=80, fg_color="#2a00ac", corner_radius=0)
frame_titulo.grid(row=0, column=0, sticky="new")

frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(0, weight=1)

# ------------------ FRAME DATOS ------------------
frame_datos = CTkFrame(
    master=frame_principal, width=320, height=440, fg_color="transparent", corner_radius=0
)
frame_datos.grid(row=1, column=0, sticky="ns", padx=10, pady=10)
frame_datos.grid_propagate(False)

frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_columnconfigure(1, weight=1)

for i in range(7):
    frame_datos.grid_rowconfigure(i, weight=1, minsize=50)

# ------------------- FRAME INFERIOR ------------------
frame_inferior = CTkFrame(master=frame_principal,width=420, height=80, fg_color="transparent", corner_radius=0)
frame_inferior.grid(row=2, column=0, sticky="s")

frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
frame_inferior.grid_propagate(False)


# ------------------ FUNCIONES ---------------
# get() es el método para obtener el valor de las entradas
# strip() para eliminar espacios al inicio y al final 
# lower() para convertir a minúsculas
# al aplicar los tres metodos juntos, se obtiene el valor ingresado por el usuario, 
# sin espacios al inicio o al final, y en minúsculas (estandarizar el formato del dato)

def capturar_datos():
    nombre = campo_nombre.get().strip().lower()
    correo = campo_correo.get().strip().lower()
    edad = campo_edad.get().strip()
    pais = pais_seleccionado.get().strip()
    profesion = profesion_seleccionada.get().strip()
    genero = genero_seleccionado.get() 

    if( not nombre 
       or not correo 
       or not edad 
       or pais == "SELECCIONA" 
       or profesion == "SELECCIONA" 
       or genero == 0):
        etiqueta_informacion.configure(text="Por favor, completa todos los campos")
        etiqueta_informacion.after(2000, lambda: etiqueta_informacion.configure(text=""))
        return

    if  not nombre.isalpha():
        etiqueta_informacion.configure(text="El nombre no puede contener números")
        etiqueta_informacion.after(2000, lambda: etiqueta_informacion.configure(text=""))
        return
    
    if len(nombre) < 3:
        etiqueta_informacion.configure(text="El nombre debe tener al menos 3 caracteres")
        etiqueta_informacion.after(2000, lambda: etiqueta_informacion.configure(text=""))
        return
    
    lista_extensiones_validas = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@outlook.com"]
    if not correo.endswith(tuple(lista_extensiones_validas)):
        etiqueta_informacion.configure(text="Por favor, ingrese un correo valido.")
        etiqueta_informacion.after(2000, lambda: etiqueta_informacion.configure(text=""))
        return
    
def limpiar():
    campo_nombre.delete(0, "end")
    campo_correo.delete(0, "end")
    campo_edad.delete(0, "end")
    pais_seleccionado.set("SELECCIONA")
    profesion_seleccionada.set("SELECCIONA")
    genero_seleccionado.set(0)
    etiqueta_informacion.configure(text="")
    

# ------------------ LABELS ------------------
etiqueta_titulo = CTkLabel(
    master=frame_titulo,
    height=80,
    text="REGISTRO DE USUARIO",
    font=("Montserrat", 20, "bold"),
    text_color="#ffffff",
    fg_color="transparent",
)
etiqueta_titulo.grid(row=0, column=0,sticky="nsew")

etiequeta_nombre = CTkLabel(
    master=frame_datos,
    width=120,
    height=30,
    text="NOMBRE",
    font=("Montserrat", 16),
    text_color="#ffffff",
    fg_color="#81dc00",
)
etiequeta_nombre.grid(row=0, column=0, sticky="e")

etiequeta_correo = CTkLabel(
    master=frame_datos,
    width=120,
    height=30,
    text="CORREO:",
    font=("Montserrat", 16),
    text_color="#ffffff",
    fg_color="#81dc00",
)
etiequeta_correo.grid(row=1, column=0, sticky="e")

etiequeta_edad = CTkLabel(
    master=frame_datos,
    width=120,
    height=30,
    text="EDAD:",
    font=("Montserrat", 16),
    text_color="#ffffff",
    fg_color="#81dc00",
)
etiequeta_edad.grid(row=2, column=0, sticky="e")

etiequeta_pais = CTkLabel(
    master=frame_datos,
    width=120,
    height=30,
    text="PAÍS:",
    font=("Montserrat", 16),
    text_color="#ffffff",
    fg_color="#81dc00",
)
etiequeta_pais.grid(row=3, column=0, sticky="e")

etiequeta_profesion = CTkLabel(
    master=frame_datos,
    width=120,
    height=30,
    text="PROFESIÓN:",
    font=("Montserrat", 16),
    text_color="#ffffff",
    fg_color="#81dc00",
)
etiequeta_profesion.grid(row=4, column=0, sticky="e")

etiequeta_genero = CTkLabel(
    master=frame_datos,
    width=120,
    height=30,
    text="GÉNERO:",
    font=("Montserrat", 16),
    text_color="#ffffff",
    fg_color="#81dc00",
)
etiequeta_genero.grid(row=5, column=0, sticky="e")

etiqueta_informacion= CTkLabel(
    master=frame_inferior,
    width=300,
    height=80,
    text="",
    font=("Montserrat", 12,"bold"),
    text_color="#223ac2",
    fg_color="transparent"
    
)
etiqueta_informacion.grid(row = 0, column = 0, sticky="nsew")

# ------------------ ENTRADAS ------------------
campo_nombre = CTkEntry(
    master=frame_datos,
    width=200,
    height=30,
    border_color="#e3e5f3",
    text_color="#2a00ac",
    justify="center",
    corner_radius=0,
    placeholder_text="...",
    font=("Montserrat", 16),
)
campo_nombre.grid(row=0, column=1, sticky="w")

campo_correo = CTkEntry(
    master=frame_datos,
    width=200,
    height=30,
    border_color="#e3e5f3",
    text_color="#2a00ac",
    justify="center",
    corner_radius=0,
    placeholder_text="...",
    font=("Montserrat", 16),
)
campo_correo.grid(row=1, column=1, sticky="w")

campo_edad = CTkEntry(
    master=frame_datos,
    width=200,
    height=30,
    border_color="#e3e5f3",
    text_color="#2a00ac",
    justify="center",
    corner_radius=0,
    placeholder_text="...",
    font=("Montserrat", 16),
)
campo_edad.grid(row=2, column=1, sticky="w")

# ------------------ OPTION MENU ------------------
lista_paises = ["GUATEMALA", "MEXICO", "COLOMBIA", "SALVADOR", "COSTA RICA", "PANAMA"]

pais_seleccionado = StringVar(value="SELECCIONA")

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
    variable=pais_seleccionado,
    font=("Montserrat", 16),
)
menu_pais.grid(row=3, column=1, sticky="w")

lista_profesiones = [
    "INGENIERO",
    "DOCTOR",
    "ABOGADO",
    "ARTISTA",
    "TECNICO",
    "PROGRAMADOR",
]

profesion_seleccionada = StringVar(value="SELECCIONA")

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
    variable=profesion_seleccionada,
    font=("Montserrat", 16),
)
menu_profesion.grid(row=4, column=1, sticky="w")

# ------------------ RADIO BUTTONS ------------------
frame_radios = CTkFrame(master=frame_datos, fg_color="transparent", corner_radius=0)
frame_radios.grid(row=5, column=1, sticky="W")

frame_radios.grid_columnconfigure(0, weight=1)
for i in range(3):
    frame_radios.grid_rowconfigure(i, weight=1) 
genero_seleccionado = IntVar(value=0)

radio_femenino = CTkRadioButton(
    master=frame_radios,
    text="FEMENINO",
    value=1,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
    border_color="#2a00ac",
    fg_color="#81dc00",
)
radio_femenino.grid(row=0, column=0, sticky="w", padx=10, pady=2)

radio_masculino = CTkRadioButton(
    master=frame_radios,
    text="MASCULINO",
    value=2,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
    border_color="#2a00ac",
    fg_color="#81dc00",
)
radio_masculino.grid(row=1, column=0, sticky="w", padx=10, pady=2)

radio_otro = CTkRadioButton(
    master=frame_radios,
    text="OTRO",
    value=3,
    variable=genero_seleccionado,
    font=("Montserrat", 16),
    text_color="#2a00ac",
    border_color="#2a00ac",
    fg_color="#81dc00",
)
radio_otro.grid(row=2, column=0, sticky="w", padx=10, pady=2)

# ------------------ BOTONES ------------------
boton_enviar = CTkButton(
    master=frame_datos,
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
boton_enviar.grid(row=6, column=0, sticky="w")

boton_limpiar = CTkButton(
    master=frame_datos,
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
boton_limpiar.grid(row=6, column=1, sticky="e")

# ------------------ MAIN LOOP ------------------
ventana.mainloop()
