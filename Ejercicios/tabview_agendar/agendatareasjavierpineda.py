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
frame_principal.grid_columnconfigure(0, weight=1, minsize=140)
frame_principal.grid_columnconfigure(1, weight=2, minsize=360)
frame_principal.grid_propagate(False)


frame_izquierda=CTkFrame(master=frame_principal,
                         fg_color="#333333",
                         corner_radius=0,
                         width=140)
frame_izquierda.grid(row=0,column=0,sticky="nsew",padx=0,pady=0)


frame_derecho=CTkFrame(master=frame_principal,
                       fg_color="#333333",
                       height=420,
                       width=340,
                       corner_radius=0)

frame_derecho.grid(row=0,column=1,sticky="nswe",padx=0,pady=0)
frame_derecho.grid_rowconfigure(0,weight=1)
frame_derecho.grid_rowconfigure(1,weight=20)
frame_derecho.grid_columnconfigure(0,weight=1)
frame_derecho.grid_propagate(False) 



frame_arriba=CTkFrame(master=frame_derecho,
                     fg_color="#303030",
                     height=100,
                     corner_radius=0)
frame_arriba.grid(row=0,column=0,sticky="new",padx=0)


pestañas=CTkTabview(
    master=frame_derecho,
    corner_radius=0,
    fg_color="#aa954e",
    segmented_button_fg_color="#1519db",
    segmented_button_selected_color="#1519db",
    segmented_button_selected_hover_color="#ffffff",
    text_color="#ffffff"
)

pestañas.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=8,
)

formulario= pestañas.add("formulario")
registro= pestañas.add("Registro")

formulario.configure(fg_color="#3f3f42")
formulario.configure(fg_color="#ffffff")

formulario.grid_columnconfigure(0,weight=1)
formulario.grid_columnconfigure(1,weight=1)
formulario.grid_rowconfigure(0,weight=1)
formulario.grid_rowconfigure(1,weight=1)
pestañas._segmented_button.grid_forget()


def click_boton_formulario():
    pestañas.set("formulario")
    
    
def click_boton_registro():
    pestañas.set("Registro")

boton_formulario=CTkButton(
    master=frame_izquierda,
    text="ingresar tareas",
    fg_color="#1519DB",
    command=click_boton_formulario
)

boton_formulario.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

boton_registro=CTkButton(
    master=frame_izquierda,
    text="ver tareas",
    fg_color="#1519db",
    command=click_boton_registro
)
boton_registro.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
)


etiqueta_1 = CTkLabel(
    master=formulario,
    width=100,
    fg_color="transparent",
    text="Nombre de la tarea",
    font=("Montserrat", 16),
)
etiqueta_1.grid(
    row=0,
    column=0,
    sticky="ewn",
    pady=20
)

#   Caja de texto - CTkTextBox
caja_texto = CTkEntry(
    master=formulario,
    width=200,
    height=20,
    corner_radius=0,
    fg_color="#B90A8E",
    font=("Montserrat", 16),
)
caja_texto.grid(
    row=0,
    column=1,
    sticky="wn",
    pady=20
)

descripcion=CTkTextbox(
    master=formulario,
    width=800,
    height=90,
    corner_radius=0,
    fg_color="#DD2222",
    font=("Montserrat", 16),
)
descripcion.grid(
    row=1,
    column=0,
    sticky="nsew",
    columnspan=2
    
)





ventana.mainloop()