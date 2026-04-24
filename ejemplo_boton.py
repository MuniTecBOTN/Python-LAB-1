from customtkinter import *
set_appearance_mode("light")
set_default_color_theme("green")

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
frame_principal.grid_rowconfigure(1, weight=1)


def funcion_boton_1():
    nombre = campo_texto.get()
    print(f"Hola {nombre}, has hecho tu primera interfaz gráfica con CustomTkinter")


boton_1 = CTkButton(
    master=frame_principal,
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

boton_1.grid(row=1, column=0)

campo_texto = CTkEntry(
    master=frame_principal,
    width=180,
    corner_radius=0,
    placeholder_text="TU NOMBRE",
    font=("Montserrat", 16),
)

campo_texto.grid(row=0, column=0)

ventana.mainloop()