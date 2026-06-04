from customtkinter import *
import string
import secrets
import random
set_default_color_theme("green")
set_appearance_mode("dark")
def generar():
    longitud=int(sliceSize.get())-1
    caracteres=""
    contraseña=""
    if checks[0].get():
        caracteres+= string.ascii_lowercase
        contraseña+=secrets.choice(string.ascii_lowercase)
    if checks[1].get():
        caracteres+= string.ascii_uppercase
        contraseña+=secrets.choice(string.ascii_uppercase)
    if checks[2].get():
        caracteres+= string.digits
        contraseña+=secrets.choice(string.digits)
    if checks[3].get():
        caracteres+= string.punctuation
        contraseña+=secrets.choice(string.punctuation)
    if not checks[1] and not checks[2] and not checks[3] and not checks[0]:
        return
    while len(contraseña)<=longitud:
        contraseña+=secrets.choice(caracteres)
    contraseña="".join(random.sample(contraseña, len(contraseña)))
    contraseñaResultante.configure(text=f"contraseña: {contraseña}")
    print(contraseña)
    return

def copiar():
    window.clipboard_append(contraseñaResultante.getvar())
    return
def actualizarSlider(value):
    labelLongitud.configure(text=f"Longitud: {value}")
    
window = CTk()
for i in range(9):
    window.grid_rowconfigure(i, weight=1)
window.grid_columnconfigure(0, weight=1)
window.geometry("600x400")
window.title("Generador")
title = CTkLabel(
    master=window,
    text="Generador de contraseñas",
    font=("Montserrat", 16, "bold"),
    fg_color="transparent"
)
title.grid(column=0, row=0)
slider=IntVar()
sliceSize=CTkSlider(
    master=window,
    height=10,
    fg_color="#000000",
    corner_radius=10,
    border_width=0,
    button_corner_radius=10,
    button_hover_color="#60BFD9",
    variable=slider,
    from_=4,
    to=30,
    progress_color="transparent",
    number_of_steps=26,
    command=actualizarSlider
)
sliceSize.grid(column=0, row=1)

labelLongitud=CTkLabel(
    master=window,
    text=f"Longitud: {sliceSize.get()}",
    text_color="#FFFFFF",
    font=("Montserrat", 12)
)
labelLongitud.grid(column=0, row=2)

checkLabels=["Incluir Minusculas (a-z)", "Incluir Mayusculas (A-Z)", "Incluir numeros (0-9)", "Incluir simbolos (@.-)"]
checks=[]


valor_checkbox = BooleanVar(value=False)
valor_checkbox1 = BooleanVar(value=False)
valor_checkbox2 = BooleanVar(value=False)
valor_checkbox3 = BooleanVar(value=False)
valores=[]
valores.append(valor_checkbox)
valores.append(valor_checkbox1)
valores.append(valor_checkbox2)
valores.append(valor_checkbox3)
print(valores)
texto_checkbox = StringVar()
for i, check in enumerate(checkLabels):
    checkbox = CTkCheckBox(
        master=window,
        checkbox_width=20,
        checkbox_height=20,
        corner_radius=5,
        border_width=1,
        text=checkLabels[i],
        textvariable=checkLabels[i],
        onvalue=True,
        offvalue=False,
        variable=valores[i],
        # command=funcion_checkbox,
        font=("Montserrat", 12),
    )
    checks.append(checkbox)
    checks[i].grid(row=3+i, column=0)
    
contraseñaResultante=CTkLabel(
    master=window,
    height=40,
    width=500,
    text="",
    fg_color="transparent",
    text_color="#FFFFFF",
    font=("Montserrar", 16, "bold")
)
contraseñaResultante.grid(column=0, row=7)

button1=CTkButton(
    master=window,
    text="Generar",
    height=30,
    width=140,
    command=generar
)

button1.grid(row=8, column=0)

button2=CTkButton(
    master=window,
    text="Copiar al Portapapeles",
    height=30,
    width=130,
    command=copiar
)

button2.grid(row=9, column=0)
window.mainloop()

