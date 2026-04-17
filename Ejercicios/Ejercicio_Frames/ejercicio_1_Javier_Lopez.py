from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Ejemplo de Frame en customTKinter")
ventana.geometry("1000x800")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           fg_color="#646464",
                           corner_radius=10)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0,weight=1)

frame_principal.grid_rowconfigure(0,weight=1)
frame_principal.grid_rowconfigure(1,weight=1)
frame_principal.grid_rowconfigure(2,weight=1)

frame_arriba = CTkFrame(master=frame_principal,
                           fg_color="#1900ff",
                           corner_radius=10)

frame_arriba.grid(row=0, column=0, sticky="snew", padx=10, pady=10)
frame_arriba.grid_rowconfigure(0,weight=1)

frame_arriba.grid_columnconfigure(0, weight=1)

frame_abajo = CTkFrame(master=frame_principal,
                           fg_color="#ff4a4a",
                           corner_radius=10)

frame_abajo.grid(row=1, column=0, sticky="snew", padx=10, pady=10,rowspan=2)
frame_abajo.grid_rowconfigure(0,weight=1)

frame_abajo.grid_columnconfigure(0, weight=1)
frame_abajo.grid_columnconfigure(1, weight=1)

frame_abajo_0_0 = CTkFrame(master=frame_abajo,
                           fg_color="#cde92f",
                           corner_radius=10)

frame_abajo_0_0.grid(row=0, column=0, sticky="snew", padx=10, pady=10)
frame_abajo_0_0.grid_rowconfigure(0,weight=1)

frame_abajo_1_0 = CTkFrame(master=frame_abajo,
                           fg_color="#e9a82f",
                           corner_radius=10)

frame_abajo_1_0.grid(row=0, column=1, sticky="snew", padx=10, pady=10)
frame_abajo_1_0.grid_rowconfigure(0,weight=1)


ventana.mainloop()