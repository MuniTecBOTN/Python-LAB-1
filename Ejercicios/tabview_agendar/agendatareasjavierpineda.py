from customtkinter import *

estilo_etiqueta = {
    "width":90,
    "height":30,
    "fg_color":"#24b400",
    "text_color":"#ffffff",
    "font":("Montserrat", 16),
  
}

estilo_ctkentry = {
    "width":200,
    "height":30,
    "fg_color":"#f0f8f6",
    "corner_radius":0,
    "text_color":"#000000",
    "font":("Montserrat", 16),
   
}






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
formulario.grid_rowconfigure([0,1,2,3,4,5],weight=1)
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


etiqueta_nombre = CTkLabel(
    master=formulario,
    text="NOMBRE",
    **estilo_etiqueta
)
etiqueta_nombre.grid(
    row=0,
    column=0,
    sticky="ew",
    pady=20
)

campo_nombre = CTkEntry(
    master=formulario,
    placeholder_text="---",
    **estilo_ctkentry

)
campo_nombre.grid(
    row=0,
    column=1,
    sticky="ew",
    pady=20
)

campo_descripcion=CTkTextbox(
    master=formulario,
    width=800,
    height=300,
    corner_radius=0,
    fg_color="#F0EFEF",
    font=("Montserrat", 16),
)
campo_descripcion.grid(
    row=2,
    column=0,
    sticky="nsew",
    columnspan=2,
    padx=10,
    pady=10
    
)

#   Etiqueta - CTkLabel
etiqueta_descripcion = CTkLabel(
    master=formulario,
    text="DESCRIPCIÓN", 
    **estilo_etiqueta
)
etiqueta_descripcion.grid(
    row=1,
    column=0,
    columnspan=2,
    sticky="ew"
)


etiqueta_fecha = CTkLabel(
    master=formulario,
    text="FECHA",
    **estilo_etiqueta
)
etiqueta_fecha.grid(
    row=3,
    column=0,
    sticky="ew"
)
campo_fecha = CTkEntry(
    master=formulario,
    placeholder_text="---",
    **estilo_ctkentry

)
campo_fecha.grid(
    row=3,
    column=1,
    sticky="ew",
   
)
def agendar ():
    
    

    

    nombre = campo_nombre.get()
    fecha= campo_fecha.get()
    descripcion=campo_descripcion.get("0.0",END)
    if not nombre:
        campo_nombre.configure(border_color="red", border_width=2)
        return
    else:
        campo_nombre.configure(border_color="green", border_width=2)
    if not fecha:
        campo_fecha.configure(border_color="red",border_width=2)
        return
    
    else:
        campo_fecha.configure(border_color="green",border_width=2)
        
    if not descripcion:
        campo_descripcion.configure(border_color="red",border_width=2)
    else:
        campo_descripcion.configure(border_color="green",border_width=2)
    if not fecha.isdigit():
        campo_fecha.configure(border_color="orange",border_width=2)

        return
     
      
        




def limpiar ():
    campo_descripcion.delete("0.0",END),
    campo_fecha.delete("0",END)
    campo_nombre.delete("0",END)
    
boton_agendar = CTkButton(
    master=formulario,
    width=80,
    height=30,
    corner_radius=0,
    text="AGENDA",
    anchor="center",
    font=("Montserrat", 16),
    command=agendar
)

boton_agendar.grid(
    row=4,
    column=0,
)
boton_limpiar = CTkButton(
    master=formulario,
    width=80,
    height=30,
    corner_radius=0,
    text="LIMPIAR",
    anchor="center",
    font=("Montserrat", 16),
    command=limpiar
)

boton_limpiar.grid(
    row=4,
    column=1,
)


ventana.mainloop()