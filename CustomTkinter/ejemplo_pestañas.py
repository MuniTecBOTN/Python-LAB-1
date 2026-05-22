from customtkinter import *

# =========================================================
# CONFIGURACIÓN GLOBAL
# =========================================================
set_appearance_mode("light")
set_default_color_theme("green")

# =========================================================
# APP PRINCIPAL
# =========================================================
ventana = CTk()

ventana.title("Sistema de Registro")
ventana.geometry("800x620")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# =========================================================
# COLORES
# =========================================================
COLOR_FONDO = "#e3e5f3"
COLOR_FONDO_TENUE = "#E4E7f9"
COLOR_AZUL = "#2a00ac"
COLOR_AZUL_TENUE = "#2a00a2"
COLOR_VERDE = "#81dc00"
COLOR_BLANCO = "#ffffff"
COLOR_ROSADO = "#ea4f9f"

estilo_botones = {
    "width": 200,
    "height": 55,
    "corner_radius": 0,
    "fg_color": COLOR_AZUL,
    "hover_color": COLOR_VERDE,
    "text_color": COLOR_BLANCO,
    "font": ("Montserrat", 16, "bold")
}

estilo_campos_texto = {
    "width":200,
    "height":55,
    "border_color":COLOR_BLANCO,
    "fg_color":COLOR_BLANCO,
    "text_color":COLOR_AZUL,
    "corner_radius":0,
    "justify":"center",
    "font":("Montserrat", 16),  
}

estilo_etiqueta = {
     "height":55,
     "justify":"center",
     "font":("Montserrat", 16, "bold"),
     "text_color":COLOR_BLANCO,
     "fg_color":COLOR_VERDE
}


# =========================================================
# ÁREA PRINCIPAL
# =========================================================
frame_principal = CTkFrame(
    master=ventana,
    corner_radius=0
)

frame_principal.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=10,
    pady=10
)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)

# =========================================================
# TABVIEW
# =========================================================
pestañas = CTkTabview(
    master=frame_principal,
    segmented_button_fg_color="#c9247c",
    segmented_button_unselected_color = "#00ff51",
    segmented_button_selected_color= "#a600ff",
    anchor="sw"
)

pestañas.grid(row = 0, 
              column=0,
              sticky = "nswe")


pestaña_1 = pestañas.add("PESTAÑA 1")
pestaña_1.grid_columnconfigure(0,weight=1)
pestaña_1.grid_rowconfigure(0,weight=1)
pestaña_1.configure(
    fg_color ="#ffffff",
    corner_radius = 0
)


pestaña_2 = pestañas.add("PESTAÑA 2")
pestaña_3 = pestañas.add("PESTAÑA 3")

















# =========================================================
# MAIN LOOP
# =========================================================
ventana.mainloop()