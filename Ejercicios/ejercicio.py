from customtkinter import *
def sumar_1():
     if not numero_1:
         numero_1.configure(border_color="red")
    
    
set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("800x600")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_principal = CTkFrame(
    master=ventana,
    fg_color="#00FFFF"
)
frame_principal.grid(row = 0, column = 0, sticky="nsew",padx = 15, pady = 15)
frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_columnconfigure(1,weight=1)
frame_principal.grid_columnconfigure(2,weight=1)
frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_rowconfigure(1,weight=1)

numero_1 = CTkEntry(
    master=frame_principal,
    width=100,
    height=100,
    corner_radius=0,
    placeholder_text="NÚMERO",
    text_color="#94F001",
    placeholder_text_color="#000000",
    justify = "center",
    font=("Montserrat", 16, "bold"),
    border_color="#00FFFF"
)
numero_1.grid(
    row=0,
    column=0,
)

numero_2 = CTkEntry(
    master=frame_principal,
    width=100,
    height=100,
    corner_radius=0,
    placeholder_text="NÚMERO",
    text_color="#94F001",
    placeholder_text_color="#000000",
    justify = "center",
    font=("Montserrat", 16, "bold"),
    border_color="#00FFFF"
)
numero_2.grid(
    row=0,
    column=1,
)

resultado_1 = CTkLabel(
    master=frame_principal,
    fg_color="transparent",
    text="RESULTADO",
    text_color="#000000",
    font=("Montserrat", 16,"bold"),
)
resultado_1.grid(
    row=0,
    column=2,
)

sumar_1 = CTkButton(
    master=frame_principal,
    width=80,
    height=60,
    corner_radius=0,
    text="SUMAR",
    anchor="center",
    text_color="#FFFFFE",
    fg_color="#FF3300",
    font=("Montserrat", 16,"bold"),
    
    command=sumar
)

sumar_1.grid(
    row=1,
    column=1,
)

ventana.mainloop()