from customtkinter import *

def funcion_boton_sumar():
    numero_a= suma.get().strip()
    numero_b=suma_2.get().strip()
    
    if not numero_a:
        suma.configure(border_color="red")
        return
    else:
        suma.configure(border_color="#D0BFE6")
        
    if not numero_b:
        suma_2.configure(border_color="red")
        return
    else:
        suma_2.configure(border_color="#D0BFE6")
    

set_default_color_theme("blue")
set_appearance_mode("light")

ventana = CTk()
ventana.title("SUMAS")
ventana.geometry("800x600")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

#FRAME PRINCIPAL------------------------------------------------------------------------------
frame_principal= CTkFrame(master=ventana,
                          fg_color="#D0BFE6",
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_columnconfigure(2, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)

#SUMAS------------------------------------------------------------------------------
suma = CTkEntry(
    master=frame_principal,
    width=170,
    height=100,
    corner_radius=0,
    justify="center",
    placeholder_text="NÚMERO",
    placeholder_text_color="#D0B7EC",
    font=("Montserrat", 16, "bold"),
    border_color="#D0BFE6")
suma.grid(
    row=0,
    column=0)

suma_2 = CTkEntry(
    master=frame_principal,
    width=170,
    height=100,
    justify="center",
    corner_radius=0,
    placeholder_text="NÚMERO",
    placeholder_text_color="#D0B7EC",
    font=("Montserrat", 16,"bold"),
    border_color="#D0BFE6")
suma_2.grid(
    row=0,
    column=1,)

#RESULTADO------------------------------------------------------------------------------
resultado = CTkLabel(
    master=frame_principal,
    fg_color="transparent",
    text="Resultado",
    text_color="#732FAA",
    font=("Montserrat", 30, "bold")
)
resultado.grid(
    row=0,
    column=2,)

#BOTON SUMAR------------------------------------------------------------------------------
boton_sumar= CTkButton(
    master=frame_principal,
    width=150,
    height=60,
    corner_radius=0,
    text="SUMAR",
    anchor="center",
    fg_color="#792eac",
    hover_color="#8643b3",
    font=("Normal", 20,"bold"),
    command=funcion_boton_sumar
)

boton_sumar.grid(
    row=1,
    column=1,
    pady=10,
    padx=10
)

ventana.mainloop()  