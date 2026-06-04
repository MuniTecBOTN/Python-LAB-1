from customtkinter import *
set_appearance_mode("light")
set_default_color_theme("blue")
####### Ventana

def sumar():
    n1= primer_numero.get()
    n2= segundo_numero.get()
    
    if not n1.isdigit(): 
        primer_numero.configure(border_color="#F04E4E")
        return
    elif not n2.isdigit(): 
        segundo_numero.configure(border_color="#F04E4E")
        return
    else: 
        primer_numero.configure(border_color="#FFFFFF")
        segundo_numero.configure(border_color="#FFFFFF")
    n1 = int(n1)
    n2 = int(n2)
    print(f"Resultado = {n1+n2}")
    label_resultado.configure(text=f"{n1+n2}") 
    
ventana = CTk()
ventana.title("Sumador")
ventana.geometry("800x600")
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)

####### Frame Principal

f_principal = CTkFrame(
    master=ventana,
    corner_radius=4,
)
f_principal.columnconfigure(0, weight=1)
f_principal.rowconfigure(0, weight=1)
f_principal.rowconfigure(1, weight=1)
f_principal.grid(row=0, column=0, sticky="snew")

####### Frame Superior

f_superior = CTkFrame(
    master=f_principal,
    fg_color="transparent",
    corner_radius=4
)

f_superior.columnconfigure(0, weight=1)
f_superior.columnconfigure(1, weight=1)
f_superior.columnconfigure(2, weight=1)
    
f_superior.rowconfigure(0, weight=1)
f_superior.grid(row=0, column=0, sticky="snew")

primer_numero = CTkEntry(
    master = f_superior,
    placeholder_text= "NUMERO",
    width=120,
    height=80,
    font=("Montserrat", 16),
    justify="center",
    border_color="#FFFFFF",
    placeholder_text_color="#2C07FF",
)
primer_numero.grid(row=0, column=0)
segundo_numero = CTkEntry(
    master = f_superior,
    placeholder_text= "NUMERO",
    width=120,
    height=80,
    font=("Montserrat", 16),
    justify="center",
    border_color="#FFFFFF",
    placeholder_text_color="#2C07FF",
)
segundo_numero.grid(row=0, column=1)


label_resultado = CTkLabel(
    master=f_superior,
    fg_color="transparent",
    text="Resultado",
    anchor="center",
    font=("Montserrat", 16, "bold"),
    height=80,
    width=120,
    text_color="#2C07FF"
)
label_resultado.grid(column=2, row=0)
##### Frame Inferior
f_inferior = CTkFrame(
    master=f_principal,
    corner_radius=5
)
f_inferior.columnconfigure(0, weight=1)
f_inferior.rowconfigure(0, weight=1)
f_inferior.grid(column=0, row=1)
btn_sumar= CTkButton(
    master=f_inferior,
    width=80,
    height=40,
    corner_radius=0,
    text="SUMAR",
    anchor="center",
    font=("Montserrat", 16, "bold"),
    command=sumar,
    fg_color="#2C07FF"
)

btn_sumar.grid(row=0, column=1)

ventana.mainloop()