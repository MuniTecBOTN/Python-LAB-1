from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("PRUEBA EJERCICIO 1")
ventana.geometry("800x600")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_principal = CTkFrame(master=ventana,
                           fg_color= "#2182a6",
                           corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10)

frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_columnconfigure(1, weight=1)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)


ventana.mainloop()