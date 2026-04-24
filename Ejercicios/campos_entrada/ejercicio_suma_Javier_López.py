from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("800x600")

#configuración de columnas en la ventana
ventana.grid_columnconfigure(0, weight=1)

#configuración de filas en la ventana
ventana.grid_rowconfigure(0, weight=1)

#configuración de Frames
frame_principal = CTkFrame(master=ventana,
                           fg_color="#d6e2f8",
                           corner_radius=0)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10, pady=10)

frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_columnconfigure(1,weight=1)
frame_principal.grid_columnconfigure(2,weight=1)


frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_rowconfigure(1,weight=1)
frame_principal.grid_rowconfigure(2,weight=1)

#configuración del texto 1

campo_texto_1 = CTkEntry(
    master=frame_principal,
    width=180,
    height=100,
    corner_radius=0,
    text_color="#000000",
    placeholder_text="NUMERO",
    justify="center",
    border_color="#d6e2f8",
    font=("Montserrat", 18),
    
)
campo_texto_1.grid(
    row=0,
    column=0,
)
#configuración del texto 2

campo_texto_2 = CTkEntry(
    master=frame_principal,
    width=180,
    height=100,
    corner_radius=0,
    text_color="#000000",
    justify="center",
    border_color="#d6e2f8",
    placeholder_text="NUMERO",
    
    font=("Montserrat", 18),
)
campo_texto_2.grid(
    row=0,
    column=1,
)

#configuración de la tiqueta

etiqueta_1 = CTkLabel(
    master=frame_principal,
    fg_color="transparent",
    text="RESULTADO",
    text_color="#8c00ff",
    anchor="center",
    font=("Montserrat", 25,"bold"),
)
etiqueta_1.grid(
    row=0,
    column=2,
)

#configuración del boton

def boton_Sumar():
    numero_a = campo_texto_1.get().strip()
    numero_b = campo_texto_2.get().strip()
    
    if not numero_a:
        campo_texto_1.configure(border_color="red")
        return
    else:
        campo_texto_1.configure(border_color="#d6e2f8")

    if not numero_b:
        campo_texto_2.configure(border_color="red")
        return
    else:
        campo_texto_2.configure(border_color="#d6e2f8")
    
    
boton_Sumar = CTkButton(
    master=frame_principal,
    width=140,
    height=60,
    corner_radius=0,
    text="SUMAR",
    anchor="center",
    fg_color="#8c00ff",
    font=("Montserrat", 20, "bold"),
    command=boton_Sumar,
)

boton_Sumar.grid(
    row=2,
    column=1,
)

ventana.mainloop()