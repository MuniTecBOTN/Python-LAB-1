from customtkinter import *


def funcion_boton_1():
    numero_a = campo_numero_a.get().strip()
    numero_b = campo_numero_b.get().strip()
    
    if not numero_a:
        campo_numero_a.configure(border_color="red")
        return
    else:
        campo_numero_a.configure(border_color="#e3e5f3")
        
        
    if not numero_b:
        campo_numero_b.configure(border_color="red")
        return
    else:        
        campo_numero_b.configure(border_color="#e3e5f3")

set_appearance_mode("light")
set_default_color_theme("green")

ventana = CTk()
ventana.title("Titulo de la Ventana")
ventana.geometry("800x600")


ventana.grid_columnconfigure(0, weight=1)

ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
frame_principal = CTkFrame(master=ventana,
                           fg_color="#e3e5f3", 
                           corner_radius=0)

frame_principal.grid(row=0, column=0, sticky="snew", padx=10,pady=10)

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_columnconfigure(2, weight=1)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)




campo_numero_a = CTkEntry(
    master=frame_principal,
    width=100,
    height=70,  
    corner_radius=0,
    placeholder_text="A",
    font=("Montserrat", 24, "bold"),
    border_color="#e3e5f3",
    justify = "center"
)
campo_numero_a.grid(row=0, column=0)


campo_numero_b = CTkEntry(
    master=frame_principal,
    width=100,
    height=70,  
    corner_radius=0,
    placeholder_text="B",
    font=("Montserrat", 24, "bold"),
    border_color="#e3e5f3",
    justify = "center"
)
campo_numero_b.grid(row=0, column=1)

etiqueta_resultado = CTkLabel(
    master=frame_principal,
    width=100,
    height=70,  
    corner_radius=0,
    text="RESULTADO",
    font=("Montserrat", 24, "bold"),
    text_color="#2a00ac",
    justify = "center"
)
etiqueta_resultado.grid(row=0, column=2)

boton_1 = CTkButton(
    master=frame_principal,
    width=100,
    height=50,
    fg_color="#2a00ac",
    hover_color= "#2751B3",
    corner_radius=0,
    text="SUMAR",
    anchor="center",
    font=("Montserrat", 20),
    command=funcion_boton_1,
)
boton_1.grid(row=1, column=1)

ventana.mainloop()