from customtkinter import *
set_appearance_mode("light")
set_default_color_theme("green")

ventana = CTk()
ventana.title("Ejemplo de Frame en CustomTkinter")
ventana.geometry("800x600")

ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           fg_color="#d72b48", 
                           corner_radius=0)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)

frame_izquierdo = CTkFrame(master=frame_principal,
                           fg_color="#ff790c",
                           corner_radius=0 
                           )

frame_izquierdo.grid_columnconfigure(0, weight=1)
frame_izquierdo.grid_columnconfigure(1, weight=1)

frame_izquierdo.grid_rowconfigure(0, weight=1)
frame_izquierdo.grid_rowconfigure(1, weight=1)

frame_derecho = CTkFrame(master=frame_principal,
                           fg_color="#31f281",
                           corner_radius=0 
                           )

frame_derecho.grid_columnconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(1, weight=1)

frame_interno_izquierdo_0_0 = CTkFrame(master=frame_izquierdo,
                           fg_color="#c03ab5",
                           corner_radius=0 
                           )


frame_interno_izquierdo_1_1 = CTkFrame(master=frame_izquierdo,
                           fg_color="#3c9492",
                           corner_radius=0 
                           )

frame_interno_derecho_0_0 = CTkFrame(master=frame_derecho,
                           fg_color="#3c944c",
                           corner_radius=0
                           )

frame_interno_derecho_1_0 = CTkFrame(master=frame_derecho,
                           fg_color="#19109b",
                           corner_radius=0
                           )

frame_principal.grid(row=0, column=0, sticky="snew", padx=10,pady=10)
frame_derecho.grid(row=0, column=1, sticky="snew", padx=10, pady=10)
frame_izquierdo.grid(row=0, column=0, sticky="snew", padx=10, pady=10)
frame_interno_izquierdo_0_0.grid(row=0, column=0, sticky="snew", padx=10, pady=10)
frame_interno_izquierdo_1_1.grid(row=1, column=1, sticky="snew", padx=10, pady=10)
frame_interno_derecho_0_0.grid(row=0, column=0, sticky="snew", padx=10, pady=10)
frame_interno_derecho_1_0.grid(row=1, column=0, sticky="snew", padx=10, pady=10)




ventana.mainloop()