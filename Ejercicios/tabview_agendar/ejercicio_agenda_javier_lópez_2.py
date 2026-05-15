from customtkinter import *

set_default_color_theme("dark-blue")

#=================================================
# FUNCIONES
#=================================================
def click_boton_dashboard():
    pestañas.set("DASHBOARD")

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
ventana.title("AGENDA")
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

frame_principal.grid_columnconfigure(0,weight=1)
frame_principal.grid_columnconfigure(1,weight=20)

frame_principal.grid_rowconfigure(0,weight=1)

frame_principal.grid_propagate(False)


#=================================================
# FRAME MENU
#=================================================

frame_menu = CTkFrame(master=frame_principal,
                      fg_color=color_azul,
                      corner_radius=0)

frame_menu.grid(row=0, column=0, sticky="nsew", padx=10)

frame_menu.grid_columnconfigure(0,weight=1)

frame_menu.grid_rowconfigure([0,4],weight=1)

titulo = CTkLabel(
    frame_menu,
    text="AGENDA",
    font=("Montserrat", 20, "bold"),
    text_color=color_blanco
)

titulo.grid(row=0, column=0)


#BOTONES

boton_dashboard = CTkButton(
    master=frame_menu,
    text="DASHBOARD",
    **estilo_botones,
    command=click_boton_dashboard
    )

boton_dashboard.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


boton_agendar = CTkButton(
    master=frame_menu,
    text="AGENDAR TAREAS",
    **estilo_botones,
    command=click_boton_agendar_tareas
    )

boton_agendar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

boton_ver_agenda = CTkButton(
    master=frame_menu,
    text="VER AGENDA",
    **estilo_botones,
    command=click_boton_agenda
    )

boton_ver_agenda.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

#=================================================
# FRAME PANEL
#=================================================

frame_panel = CTkFrame(master=frame_principal,
                           fg_color=color_fondo,
                           corner_radius=0)

frame_panel.grid(row=0, column=1, sticky="snew")

frame_panel.grid_columnconfigure(0,weight=1)

frame_panel.grid_rowconfigure(0,weight=1)
frame_panel.grid_rowconfigure(1,weight=10)

#ETIQETA

etiqueta_informacion= CTkLabel(
    master=frame_panel,
    width=300,
    height=80,
    text="SISTEMA DE AGENDA",
    font=("Montserrat", 16,"bold"),
    text_color=color_blanco,
    fg_color=color_azul
    
)
etiqueta_informacion.grid(row = 0, column = 0, sticky="nsew")


#PESTAÑAS

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
    row=1,
    column=0,
    sticky="nsew",
    
)

dashboard = pestañas.add("DASHBOARD")
agendar = pestañas.add("AGENDAR TAREAS")
ver_agenda = pestañas.add("VER AGENDA")

dashboard.configure(fg_color=color_verde)
dashboard.grid_columnconfigure(0,weight=1)
dashboard.grid_rowconfigure(0,weight=1)


agendar.configure(fg_color=color_azul)
agendar.grid_columnconfigure(0, weight=1)
agendar.grid_rowconfigure(0, weight=1)

ver_agenda.configure(fg_color=color_verde)
ver_agenda.grid_columnconfigure(0, weight=1)
ver_agenda.grid_rowconfigure(0, weight=1)


pestañas._segmented_button.grid_forget()

#=================================================
# FRAME DASHBOARD
#=================================================

frame_dashboard = CTkFrame(master=dashboard,
                           fg_color=color_fondo,
                           corner_radius=0)

frame_dashboard.grid_columnconfigure(0,weight=1)

frame_dashboard.grid_rowconfigure(0,weight=1)

frame_dashboard.grid(row=0, column=0, sticky="nsew", padx=80, pady=10)

#=================================================
# FRAME AGENDAR
#=================================================

frame_agendar = CTkFrame(master=agendar,
                           fg_color=color_fondo,
                           corner_radius=0)

frame_agendar.grid_columnconfigure(0,weight=1)
frame_agendar.grid_columnconfigure(1,weight=1)

frame_agendar.grid_rowconfigure(0,weight=1)
frame_agendar.grid_rowconfigure(1,weight=1)
frame_agendar.grid_rowconfigure(2,weight=1)
frame_agendar.grid_rowconfigure(3,weight=1)
frame_agendar.grid_rowconfigure(4,weight=1)

frame_agendar.grid(row=0, column=0, sticky="nsew", padx=80, pady=10)

#NOMBRE etiqueta y campo

etiqueta_nombre= CTkLabel(
    master=frame_agendar,
    width=400,
    text="Nombre:",
    font=("Montserrat", 16,"bold"),
    text_color=color_blanco,
    fg_color=color_verde,
    corner_radius=0
    
)
etiqueta_nombre.grid(row = 0, column = 0, sticky="e", padx=10)



texto_nombre = CTkEntry(
    master=frame_agendar,
    width=400,
    border_width=2,
    corner_radius=0,
    placeholder_text="Escribe tu nombre completo",
    justify="center",
    font=("Montserrat", 16, "bold"),
)
texto_nombre.grid(row=0,column=1, sticky="w", padx=10)

#DESCRIPCION

etiqueta_descripcion = CTkLabel(
    master=frame_agendar,
    width=400,
    text="DESCRIPCION:",
    font=("Montserrat", 22, "bold"),
    text_color=color_blanco,
    fg_color=color_verde
)

etiqueta_descripcion.grid(columnspan=2)

#=================================================
# FRAME VER AGENDA
#=================================================

frame_ver_agenda = CTkFrame(master=ver_agenda,
                           fg_color=color_fondo,
                           corner_radius=0)

frame_ver_agenda.grid_columnconfigure(0,weight=1)

frame_ver_agenda.grid_rowconfigure(0,weight=1)

frame_ver_agenda.grid(row=0, column=0, sticky="nsew", padx=80, pady=10)


ventana.mainloop()

