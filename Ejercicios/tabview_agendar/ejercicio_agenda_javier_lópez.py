from customtkinter import *

set_default_color_theme("dark-blue")

#=================================================
# FUNCIONES
#=================================================

def click_boton_agendar_tareas():
    pestañas.set("AGENDAR TAREAS")
    
def click_boton_agenda():
    pestañas.set("VER AGENDA")

#=================================================
#COLORES
#=================================================

color_fondo = "#e3e5f3"
color_azul = "#2a00ac"
color_verde = "#81dc00"
color_blanco = "#ffffff"
color_pruebas = "#ff0000"

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("800x600")

estilo_botones = {
    "width": 120,
    "height": 35,
    "corner_radius": 0,
    "fg_color": color_azul,
    "hover_color": color_verde,
    "text_color": color_blanco,
    "font": ("Montserrat", 16, "bold")
}


# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)

# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

#=================================================
# FRAME PRINCIPAL
#=================================================

frame_principal = CTkFrame(master=ventana,
                           fg_color=color_fondo,
                           corner_radius=0)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10, pady=10)

frame_principal.grid_columnconfigure([0,1],weight=1)

frame_principal.grid_rowconfigure(0,weight=1)

#=================================================
# FRAME MENU
#=================================================

frame_menu = CTkFrame(master=frame_principal,
                           fg_color=color_azul,
                           corner_radius=0)

frame_menu.grid(row=0, column=0, sticky="snw", padx=10, pady=10)

frame_menu.grid_columnconfigure(0,weight=1)

frame_menu.grid_rowconfigure([0,1],weight=1)

#BOTONES

boton_agendar = CTkButton(
    master=frame_menu,
    text="AGENDAR TAREAS",
    **estilo_botones,
    command=click_boton_agendar_tareas
    )

boton_agendar.grid(row=0, column=0)

boton_ver_agenda = CTkButton(
    master=frame_menu,
    text="VER AGENDA",
    **estilo_botones,
    command=click_boton_agenda
    )

boton_ver_agenda.grid(row=1, column=0)

#=================================================
# FRAME PANEL
#=================================================

frame_panel = CTkFrame(master=frame_principal,
                           fg_color=color_fondo,
                           corner_radius=0)

frame_panel.grid(row=0, column=1, sticky="snew", padx=10, pady=10)

frame_panel.grid_columnconfigure([0],weight=1)

frame_panel.grid_rowconfigure([0],weight=1)

pestañas = CTkTabview(
    master=frame_panel,
    corner_radius=0,
    fg_color=color_azul,
    segmented_button_fg_color=color_azul,
    segmented_button_selected_color=color_azul,
    segmented_button_selected_hover_color=color_verde,
    segmented_button_unselected_color=color_azul,
    segmented_button_unselected_hover_color=color_verde,
    text_color=color_blanco,
    
)


pestañas.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10,
)

#pestañas

agendar = pestañas.add("AGENDAR TAREAS")
ver_agenda = pestañas.add("VER AGENDA")

agendar.configure(fg_color=color_azul)
ver_agenda.configure(fg_color=color_verde)



ventana.mainloop()