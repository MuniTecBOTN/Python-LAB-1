from customtkinter import *
set_default_color_theme("green")
set_appearance_mode("dark")

ventana=CTk()
ventana.geometry("600x600")
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
frameprincipal=CTkFrame(master=ventana,
                        corner_radius=0,
                        fg_color="transparent")
frameprincipal.grid_columnconfigure(0, weight=1)
frameprincipal.grid_rowconfigure(0, weight=1)
frameprincipal.grid(row=0, column=0, sticky="snwe")

pestañas=CTkTabview(
    master=frameprincipal,
    fg_color="#8080FF",
    segmented_button_fg_color="#3E0B42",
    segmented_button_unselected_color="#3E0B42",
    segmented_button_selected_color="#C784CC",
    segmented_button_selected_hover_color="#C784CC",
    segmented_button_unselected_hover_color="#C784CC",
    anchor="se"
)

pestañas.propagate(False)
pestaña1=pestañas.add("Pestaña1")
pestaña1.grid_rowconfigure(0, weight=1)
pestaña1.grid_columnconfigure(0, weight=1)
pestaña1.configure(fg_color="#FFFFFF")

pestaña2=pestañas.add("Pestaña2")
pestaña2.grid_rowconfigure(0, weight=1)
pestaña2.grid_columnconfigure(0, weight=1)
pestaña2.configure(fg_color="#AA5454")

pestaña3=pestañas.add("Pestaña3")
pestaña3.grid_rowconfigure(0, weight=1)
pestaña3.grid_columnconfigure(0, weight=1)
pestaña3.configure(fg_color="#41A5A0")

#pestañas._segmented_button.grid_forget()
pestañas.grid(row=0, column=0, sticky="snew")


ventana.mainloop()