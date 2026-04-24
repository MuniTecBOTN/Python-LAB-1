from customtkinter import *

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
frame_principal=CTkFrame(master=ventana,
                        
                        corner_radius=0,
                        border_color="#000000",
                        border_width=16)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=100,pady=100)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_columnconfigure(2,weight=1)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)








caja_textonum1 = CTkEntry(
    master=frame_principal,
    width=100,
    height=80,
    corner_radius=0,
    border_width=0,
    placeholder_text="NUMERO 1",
    justify="center",
    font=("Montserrat", 16),
)
caja_textonum1.grid(row=0, column=0,sticky="e", padx=10, pady=10)

caja_textonum2 = CTkEntry(
    master=frame_principal,
    width=100,
    height=80,
    corner_radius=0,
    border_width=0,
    placeholder_text="NUMERO 2",
    justify="center",
    font=("Montserrat", 16),
)
caja_textonum2.grid(row=0, column=1, padx=10, pady=10)  

etiqueta_1 = CTkLabel(
    master=frame_principal,
    text_color="#34067e",
    text="RESULTADO",
    font=("Montserrat", 20),
)
etiqueta_1.grid(row=0, column=2,sticky="w", padx=10, pady=10)




def funcion_boton_1():
    num1 = int(caja_textonum1.get())
    num2 = int(caja_textonum2.get())
    resultado = num1 + num2
   

boton_1 = CTkButton(
    master=frame_principal,
    width=100,
    height=50,
    corner_radius=0,
    fg_color="#5115b3",
    text="SUMAR",
    text_color="white",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_1,
)
boton_1.grid(row=1, column=1,sticky="n", padx=10, pady=10)


ventana.mainloop()