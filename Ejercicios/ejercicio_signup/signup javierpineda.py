from customtkinter import *

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("500x600")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_principal=CTkFrame(master=ventana,
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=0,pady=0)
frame_principal.grid_columnconfigure(0, weight=1)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)

frame_superior=CTkFrame(master=frame_principal,
                            corner_radius=0)
frame_superior.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)



frame_medio=CTkFrame(master=frame_principal,   
                            corner_radius=0)
frame_medio.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
frame_medio.grid_columnconfigure(0, weight=1)
frame_medio.grid_columnconfigure(1, weight=1)
frame_medio.grid_rowconfigure(0, weight=1)
frame_medio.grid_rowconfigure(1, weight=1)
frame_medio.grid_rowconfigure(2, weight=1)
frame_medio.grid_rowconfigure(3, weight=1)
frame_medio.grid_rowconfigure(4, weight=1)
frame_medio.grid_rowconfigure(5, weight=1)

frame_inferior=CTkFrame(master=frame_principal,
                            corner_radius=0)
frame_inferior.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)



etiqueta_1 = CTkLabel(
    master=frame_superior,
    fg_color="transparent",
    text="SING UP",
    font=("Montserrat", 16),
)
etiqueta_1.grid(row=0, column=0, padx=10, pady=10)


nombre_usuario = CTkLabel(
    master=frame_medio,
    fg_color="transparent",
    text="Nombre de usuario:",
    font=("Montserrat", 14),
)
nombre_usuario.grid(row=0, column=0, sticky="e", padx=10, pady=10)


apellido_usuario = CTkLabel(
    master=frame_medio,
    fg_color="transparent",
    text="Apellido de usuario:",
    font=("Montserrat", 14),
)
apellido_usuario.grid(row=1, column=0, sticky="e", padx=10, pady=10)



correo= CTkLabel(
    master=frame_medio,
    fg_color="transparent",
    text="Correo electrónico:",
    font=("Montserrat", 14),
)
correo.grid(row=2, column=0, sticky="e", padx=10, pady=10)



telefono= CTkLabel(
    master=frame_medio,
    fg_color="transparent",
    text="Número de teléfono:",
    font=("Montserrat", 14),
)
telefono.grid(row=3, column=0, sticky="e", padx=10, pady=10)


edad= CTkLabel(
    master=frame_medio,
    fg_color="transparent",
    text="Edad:",
    font=("Montserrat", 14),
)
edad.grid(row=4, column=0, sticky="e", padx=10, pady=10)



contraseña= CTkLabel(
    master=frame_medio,
    fg_color="transparent",
    text="Contraseña:",
    font=("Montserrat", 14),
)
contraseña.grid(row=5, column=0, sticky="e",padx=10, pady=10)




caja_textonombre = CTkEntry(
    master=frame_medio,
    width=100,
    height=30,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_textonombre.grid(row=0, column=1, sticky="w", padx=10, pady=10)

caja_textoapellido = CTkEntry(
    master=frame_medio,
    width=100,
    height=30,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_textoapellido.grid(row=1, column=1, sticky="w", padx=10, pady=10)

caja_textocorreo = CTkEntry(
    master=frame_medio,
    width=100,
    height=30,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_textocorreo.grid(row=2, column=1, sticky="w", padx=10, pady=10)

caja_textotelefono = CTkEntry(
    master=frame_medio,
    width=100,
    height=30,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_textotelefono.grid(row=3, column=1, sticky="w", padx=10, pady=10)

caja_textoedad = CTkEntry(
    master=frame_medio,
    width=100,
    height=30,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_textoedad.grid(row=4, column=1, sticky="w", padx=10, pady=10)

caja_textocontraseña = CTkEntry(
    master=frame_medio,
    width=100,
    height=30,
    corner_radius=0,
    font=("Montserrat", 16),
    show="*"
)
caja_textocontraseña.grid(row=5, column=1, sticky="w", padx=10, pady=10)





def funcion_boton():
    nombre = caja_textonombre.get()
    apellido = caja_textoapellido.get()
    correo = caja_textocorreo.get()
    telefono = caja_textotelefono.get()
    edad = caja_textoedad.get()
    contraseña = caja_textocontraseña.get()
    
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Correo: {correo}")
    print(f"Teléfono: {telefono}")
    print(f"Edad: {edad}")
    print(f"Contraseña: {contraseña}")
    
    



buton_registrar = CTkButton(
    master=frame_inferior,
    width=100,
    height=30,
    hover_color="yellow",
    corner_radius=0,
    text="Registrar",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton,
    
)
buton_registrar.grid(row=0, column=0, padx=10, pady=10)







ventana.mainloop()