from customtkinter import *
set_appearance_mode("dark")
set_default_color_theme("green")

ventana = CTk()
ventana.title("Titulo de la Ventana")
ventana.geometry("800x600")


ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           corner_radius=0)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10,pady=10)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)

frame_superior = CTkFrame(master=frame_principal,
                           corner_radius=0)

frame_superior.grid(row=0, column=0, sticky="snew", padx=10,pady=10)

frame_inferior = CTkFrame(master=frame_principal,
                           corner_radius=0)

frame_inferior.grid(row=1, column=0, sticky="snew", padx=10,pady=10)

frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)

frame_inferior_izquierdo = CTkFrame(master=frame_inferior,
                           corner_radius= 0
                           )
frame_inferior_izquierdo.grid(row=0, column=0, sticky="snew", padx=10,pady=10)

frame_inferior_derecho = CTkFrame(master=frame_inferior,
                           corner_radius=0
                           )

frame_inferior_derecho.grid(row=0, column=1, sticky="snew", padx=10,pady=10)

ventana.mainloop()