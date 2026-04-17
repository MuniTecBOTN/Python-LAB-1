from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("ejercicio")
ventana.geometry("800x600")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           fg_color="#1edc2e",
                           corner_radius=0,)
                           
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)


frame_superior = CTkFrame(master=frame_principal,
                           fg_color="#ffffff",
                           corner_radius=0,)

frame_superior.grid(row=0, column=0, sticky="snew", padx=10,pady=10)

frame_inferior = CTkFrame(master=frame_principal,
                           fg_color="#00b7ff",
                           corner_radius=0,)

frame_inferior.grid(row=1, column=0, sticky="snew", padx=10,pady=10)

frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)

frame_inferior_izquierdo = CTkFrame(master=frame_inferior,
                           fg_color="#cd2727",
                           corner_radius=0,)
frame_inferior_izquierdo.grid(row=0, column=0, sticky="snew", padx=10,pady=10)

frame_inferior_derecho = CTkFrame(master=frame_inferior,
                           fg_color="#d9d0d0",
                           corner_radius=0,)
frame_inferior_derecho.grid(row=0, column=1, sticky="snew", padx=10,pady=10)

ventana.mainloop()