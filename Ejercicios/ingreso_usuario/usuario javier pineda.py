from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("700x900")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_principal=CTkFrame(master=ventana,
                        fg_color="#e3e5f3",
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=15,pady=15)
frame_principal.grid_columnconfigure(0, weight=1)



frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)


frame_superior=CTkFrame(master=frame_principal,
                        corner_radius=0,
                        height=150,
                        fg_color="#2a00ac")
frame_superior.grid(row=0, column=0,sticky ="ew")
frame_superior.grid_columnconfigure(0, weight=1)
frame_superior.grid_rowconfigure(0, weight=1)


frame_medio=CTkFrame(master=frame_principal,
                        corner_radius=0,)
frame_medio.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
frame_medio.grid_columnconfigure(0, weight=1)
frame_medio.grid_columnconfigure(1, weight=1)
frame_medio.grid_rowconfigure(0, weight=1)
frame_medio.grid_rowconfigure(1, weight=1)
frame_medio.grid_rowconfigure(2, weight=1)
frame_medio.grid_rowconfigure(3, weight=1)
frame_medio.grid_rowconfigure(4, weight=1)
frame_medio.grid_rowconfigure(5, weight=1)






frame_inferior=CTkFrame(master=frame_principal,
                        corner_radius=0,)
frame_inferior.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
frame_inferior.grid_columnconfigure(0, weight=1)
frame_inferior.grid_columnconfigure(1, weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(1, weight=1)



etiqueta_1 = CTkLabel(
    master=frame_superior,
    height=150,
    fg_color="transparent",
    text="REGISTRO DE USUARIO",
    text_color="White",
    font=("Montserrat", 16,"bold")
)
etiqueta_1.grid(row=0, column=0,
)

etiqueta_2 = CTkLabel(
    master=frame_medio,
    width=100,
    height=40,
    fg_color="#81dc00",
    text="NOMBRE:",
    text_color="#FFFFFF",
    font=("Montserrat", 16),
)
etiqueta_2.grid(row=0,
    column=0,
    sticky="e",
)
etiqueta_3 = CTkLabel(
    width=100,
    height=40,
    master=frame_medio,
    fg_color="#81dc00",
    text="CORREO:",
    text_color="#FFFFFF",
    font=("Montserrat", 16),
)
etiqueta_3.grid(row=1,
    column=0,
    sticky="e",
)
etiqueta_4 = CTkLabel(
    width=100,
    height=40,
    master=frame_medio,
    fg_color="#81dc00",
    text="EDAD:",
    text_color="#FFFFFF",
    font=("Montserrat", 16),
)

etiqueta_4.grid(row=2,
    column=0,
    sticky="e",
)

etiqueta_5 = CTkLabel(
    width=100,
    height=40,
    master=frame_medio,
    fg_color="#81dc00",
    text="PAÍS:",
    text_color="#FFFFFF",
    font=("Montserrat", 16),
)

etiqueta_5.grid(row=3,
    column=0,
    sticky="e",
)
etiqueta_6 =CTkLabel(
    width=100,
    height=40,
    master=frame_medio,
    fg_color="#81dc00",
    text="PROFESIÓN:",
    text_color="#FFFFFF",
    font=("Montserrat", 16),
)

etiqueta_6.grid(row=4,
    column=0,
    sticky="e",
)
etiqueta_7 =CTkLabel(
    width=100,
    height=40,
    master=frame_medio,
    fg_color="#81dc00",
    text="GENERO:",
    text_color="#FFFFFF",
    font=("Montserrat", 16),
)

etiqueta_7.grid(row=5,
    column=0,
    sticky="e",
)
caja_textonombre = CTkEntry(
    master=frame_medio,
    width=180,
    height=40,
    border_width=0,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_textonombre.grid(
    row=0,
    column=1,
    sticky="w"
)
caja_textcorreo = CTkEntry(
    master=frame_medio,
    width=180,
    height=40,
    border_width=0,
    corner_radius=0,
    
    font=("Montserrat", 16),
)
caja_textcorreo.grid(
    row=1,
    column=1,
    sticky="w"
)
caja_textoedad = CTkEntry(
    master=frame_medio,
    width=180,
    height=40,
    border_width=0,
    corner_radius=0,
    font=("Montserrat", 16),
)
caja_textoedad.grid(
    row=2,
    column=1,
    sticky="w"
)








lista_opciones = ["GUATEMALA", "PERU", "COLOMBIA","MEXICO"]
país_selecionado = StringVar(value="SELECCIONA")
menu_opciones = CTkOptionMenu(
    master=frame_medio,
    fg_color="#FFFFFF",
    width=180,
    height=40,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_opciones,
    variable=país_selecionado,
    text_color="#2a00ac",
    dropdown_fg_color="#2A00AC",
    dropdown_text_color="#FFFFFF",
    font=("Montserrat", 16),
    button_color="#81dc00"
)
menu_opciones.grid(
    row=3,
    column=1,
    sticky="w")


lista_opciones = ["PROGRAMADOR", "DISEÑADOR", "CHEF","CONTADOR"]
profesion_selecionado = StringVar(value="SELECCIONA")

menu_opciones = CTkOptionMenu(
    fg_color="#ffffff",
    master=frame_medio,
    width=180,
    height=40,
    corner_radius=0,
    dynamic_resizing=False,
    values=lista_opciones,
    variable=profesion_selecionado,
    text_color="#2a00ac",
    font=("Montserrat", 16),
    button_color="#81dc00"

)
menu_opciones.grid(
    row=4,
    column=1,
    sticky="w"
)





frame_mediobajo=CTkFrame(master=frame_medio,
                         fg_color="transparent",
                        
                         )
frame_mediobajo.grid(row=5, column=1,sticky="wn")
frame_mediobajo.columnconfigure(0,weight=1)
frame_mediobajo.rowconfigure(0, weight=1)
frame_mediobajo.rowconfigure(1,weight=1)
frame_mediobajo.rowconfigure(2,weight=1)

genero_selecionado = IntVar(value=0)
radio_femenino = CTkRadioButton(
    master=frame_mediobajo,
    text="FEMENINO",
   
    value=1,
    variable=genero_selecionado,
    font=("Montserrat", 16),
)
radiomasculino = CTkRadioButton(
    master=frame_mediobajo,
    text="MASCULINO",
    value=2,
    variable=genero_selecionado,
    font=("Montserrat", 16),
)
radio_otro =  CTkRadioButton(
    master=frame_mediobajo,
    text="OTRO",
     value=3,
    variable=genero_selecionado,
    font=("Montserrat", 16),
)

radio_femenino.grid(
    row=0,
    column=0,
    sticky="w",
    padx="10",
    pady=8,
)
radiomasculino.grid(
    row=1,
    column=0,
    sticky="w",
    padx="10",
    pady=8,
)
radio_otro.grid(
    row=2,
    column=0,
    sticky="w",
    padx="10",
    pady=8,
)



def capturar_Datos():
    nombre = caja_textonombre.get().strip().lower()
    correo = caja_textcorreo.get().strip().lower()
    edad = caja_textoedad.get().strip().lower()
    país = país_selecionado.get().strip()
    profesion = profesion_selecionado.get().strip()
    genero= genero_selecionado.get()
    if(
        not nombre or not correo or país=="SELECCIONA"or profesion=="SELECCIONA" or genero==0):
        etiqueta_resultado.configure(text="por favor ,completa todos los campos")
    
    print("se guardo correctamente tus datos ")
    print(f"{nombre}")
    print(f"{correo}")
    print(f"{edad}")
    print(f"{país}")
    print(f"{profesion}")
    print(f"{genero}") 
    
       
def limpiar_datos():
    caja_textonombre.delete(0,END)
    caja_textcorreo.delete(0,END)
    caja_textoedad.delete(0,END)
    país_selecionado.set("selecciona una opcion")
    profesion_selecionado.set("selecciona una opcion")
    genero_selecionado.set(0)
    
    
    
    
    
boton_1 = CTkButton(
    master=frame_inferior,
    width=150,
    height=40,
    corner_radius=0,
    text="Guardar datos",
    anchor="center",
    font=("Montserrat", 16),
    command=capturar_Datos,
)
boton_2 = CTkButton(
    master=frame_inferior,
    width=150,
    height=40,
    corner_radius=0,
    text="limpiar",
    anchor="center",
    font=("Montserrat",16),
   command=limpiar_datos,
)

boton_1.grid(
    row=0,
    column=0,
    sticky="e",
   
)
boton_2.grid(
    row=0,
    column=1,
    sticky="w",
     padx=8
)

etiqueta_resultado = CTkLabel(
    master=frame_inferior,
    fg_color="transparent",
    text="Esta es una etiqueta",
    font=("Montserrat", 16),
)
etiqueta_resultado.grid(
    row=1,
    column=0,
    sticky="e",
)













ventana.mainloop()