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
                        fg_color="#e67e7e",
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10,pady=10)

frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_columnconfigure([0,1], weight=1,minsize=350)
frame_principal.grid_propagate(False)


frame_izquierda=CTkFrame(master=frame_principal,
                         fg_color="#242424",
                         corner_radius=0,
                         width=300)
frame_izquierda.grid(row=0,column=0,sticky="nsew",padx=0,pady=0)


frame_derecho=CTkFrame(master=frame_principal,
                       fg_color="#333333",
                       height=800,
                       width=300,
                       corner_radius=0)
frame_derecho.grid(row=0,column=1,sticky="nswe",padx=0,pady=0)
frame_derecho.grid_rowconfigure(0,weight=1)
frame_derecho.grid_columnconfigure(0,weight=1)

frame_centro=CTkFrame(master=frame_derecho,
                      fg_color="#aa954e",
                      corner_radius=0,
                      width=200,
                      height=400)
frame_centro.grid(row=0,column=0,sticky="ew",padx=2,pady=2)

ventana.mainloop()