from customtkinter import *

set_default_color_theme("green")
set_appearance_mode("dark")

ventana = CTk()
ventana.title("Ejercicio Frames")
ventana.geometry("800x600")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

#PRINCIPAL----------------------------------------------------------------------------
frame_principal= CTkFrame(master=ventana,
                          fg_color="#F0F0F0",
                          corner_radius=0)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)

#FRAME SUPERIOR----------------------------------------------------------------------------
frame_Superior= CTkFrame(master=frame_principal,
                       fg_color="#6E378D",
                       corner_radius=0)
frame_Superior.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_Superior.grid_columnconfigure(0, weight=1)
frame_Superior.grid_rowconfigure(0, weight=1)

#FRAME INFERIOR----------------------------------------------------------------------------
frame_inferior= CTkFrame(master=frame_principal,
                      fg_color="#2EE74D",
                      corner_radius=0)
frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
frame_infe_izquierdo= CTkFrame(master=frame_inferior,
                                fg_color="#B37ADA",
                                corner_radius=0)
frame_infe_derecho= CTkFrame(master=frame_inferior,
                                fg_color="#853EB4",
                                corner_radius=0)

#FRAMES----------------------------------------------------------------------------
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_inferior.grid(row=1, column=0, sticky= "nsew", padx=10, pady=10)
frame_infe_izquierdo.grid(row=0, column=0, sticky= "nsew", padx=15, pady=15)
frame_infe_derecho.grid(row=0, column=1, sticky= "nsew", padx=15, pady=15)


ventana.mainloop()