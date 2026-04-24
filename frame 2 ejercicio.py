from customtkinter import *

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


frame_principal = CTkFrame(
    master=ventana,
    fg_color="#D14B2E"
)
frame_principal.grid(row = 0 , column = 0,sticky="nsew",padx=15,pady=15)
frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_rowconfigure(1,weight=1)
frame_principal.grid_rowconfigure(2,weight=1)


frame_principal = CTkFrame(frame_principal,
                           corner_radius=0)
master = ventana,
    fg_color="#E3D4D1"
)
frame_principal.grid(row = 0 , column = 0,sticky="nsew",padx=15,pady=15)
frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_columnconfigure(1,weight=1)
frame_principal.grid_columnconfigure(2,weight=1)


ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=2)
ventana.grid_columnconfigure(2, weight=3)

ventana = CTkButton(
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



ventana.mainloop()