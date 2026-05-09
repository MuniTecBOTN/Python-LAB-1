from customtkinter import *
import string
import secrets
import random

set_default_color_theme("dark-blue")
set_appearance_mode("light")

ventana = CTk()
ventana.title("Generador de Contraseñas")
ventana.geometry("600x600")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

# FRAME PRINCIPAL------------------------------------------------------------------------------
frame_principal= CTkFrame(master=ventana,
                          fg_color="#f6bdf8",
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)
frame_principal.grid_rowconfigure(3, weight=1)
frame_principal.grid_rowconfigure(4, weight=1)

#FRAME TITULO-------------------------------------------------------------------------------------------------------------------------------------------------------------------
frame_titulo=CTkFrame(master= frame_principal,
                      corner_radius=0,
                      fg_color="transparent")
frame_titulo.grid(row=0, column=0, sticky="senw")
frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(0, weight=1)
titulo = CTkLabel(
    master=frame_titulo,
    fg_color="transparent",
    text="🔐 Generador de contraseñas",
    anchor="center",
    font=("Montserrat", 20, "bold"))

titulo.grid(row=0,column=0, padx=4, pady=0)

#DEFINICIONES---------------------------------------------------------------
def porcentaje_longitud(valor):
    longitud_text.configure(text=f"Longitud: {int(valor)}")
    
def generar_contra():
    longitud=int(slider.get())
    caracteres=""
    contraseña=""
    
    if min_checkbox.get():
        caracteres+= string.ascii_lowercase
        contraseña+= secrets.choice(string.ascii_lowercase)
    
    if may_checkbox.get():
        caracteres+= string.ascii_uppercase
        contraseña+= secrets.choice(string.ascii_uppercase)
    
    if num_checkbox.get():
        caracteres+= string.digits
        contraseña+=secrets.choice(string.digits)
    
    if simb_checkbox.get():
        caracteres+= string.punctuation
        contraseña+= secrets.choice(string.punctuation)
        
    if not caracteres:
        contra_text.delete(0, "end")
        contra_text.insert(0,"Selecciona al menos una opción")
        return
        
        
    for i in range(longitud - len(contraseña)):
        contraseña+=secrets.choice(caracteres)
        
    contraseña="".join(random.sample(contraseña, len(contraseña)))
    
    contra_text.delete(0, "end")
    contra_text.insert(0, contraseña)        
    
def copiar_texto():
    texto = contra_text.get()
    
    if texto == "":
        return 
    
    ventana.clipboard_clear()
    ventana.clipboard_append(texto)
    
#FRAME BARRITA-------------------------------------------------------------------------------------------------------------------------------------------------------------------
frame_barrita=CTkFrame(master=frame_principal,
                       corner_radius=0,
                       fg_color="transparent")
frame_barrita.grid(row=1, column=0, sticky="nsew")
frame_barrita.grid_columnconfigure(0, weight=1)
frame_barrita.grid_rowconfigure(0, weight=1)
frame_barrita.grid_rowconfigure(1, weight=1)

valor_slider = IntVar(value=4)
slider = CTkSlider(
    master=frame_barrita,
    from_=4,
    to=32,
    command=porcentaje_longitud,
    variable=valor_slider,
    number_of_steps=100)
slider.grid(row=0, column=0, sticky="ew", padx=40)

longitud_text = CTkLabel(
    master=frame_barrita,
    fg_color="transparent",
    text="Longitud: ",
    anchor="sw",
    font=("Montserrat", 16),
)
longitud_text.grid(row=1,column=0)
#Chequesitos-------------------------------------------------------------------------------------------------------------------------------------------------------------------
frame_chequesitos=CTkFrame(master=frame_principal,
                           corner_radius=0,
                           fg_color="transparent")
frame_chequesitos.grid(row=2, column=0)

frame_chequesitos.grid_columnconfigure(0, weight=1)
frame_chequesitos.grid_rowconfigure(0, weight=1)
frame_chequesitos.grid_rowconfigure(1, weight=1)
frame_chequesitos.grid_rowconfigure(2, weight=1)
frame_chequesitos.grid_rowconfigure(3, weight=1)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
min_checkbox = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir minúsculas (a-z)")
checkbox_minusc = CTkCheckBox(
    master=frame_chequesitos,
    checkbox_width=24,
    checkbox_height=24,
    fg_color="#90eb66",
    checkmark_color="#ffffff",
    hover_color="#ffffff",
    corner_radius=4,
    border_width=3,
    text="Incluir minúsculas (a-z)",
    textvariable = texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=min_checkbox,
    font=("Montserrat", 16, "bold"),
)
checkbox_minusc.grid(row=0,column=0,pady=4, sticky="w")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
may_checkbox = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir mayúsculas (A-Z)")
checkbox_minusc = CTkCheckBox(
    master=frame_chequesitos,
    checkbox_width=24,
    checkbox_height=24,
    fg_color="#90eb66",
    checkmark_color="#ffffff",
    hover_color="#ffffff",
    corner_radius=4,
    border_width=3,
    text="Incluir mayúsculas (A-Z)",
    textvariable = texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=may_checkbox,
    font=("Montserrat", 16, "bold"),
)
checkbox_minusc.grid(row=1,column=0, pady=4, sticky="w")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
num_checkbox = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir números (0-9)")
checkbox_minusc = CTkCheckBox(
    master=frame_chequesitos,
    checkbox_width=24,
    checkbox_height=24,
    fg_color="#90eb66",
    hover_color="#ffffff",
    checkmark_color="#ffffff",
    corner_radius=4,
    border_width=3,
    text="Incluir números (0-9)",
    textvariable = texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=num_checkbox,
    font=("Montserrat", 16, "bold"),
)
checkbox_minusc.grid(row=2,column=0,pady=4, sticky="w")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
simb_checkbox = BooleanVar(value=False)
texto_checkbox = StringVar(value="Incluir símbolos (!@#...)")
checkbox_minusc = CTkCheckBox(
    master=frame_chequesitos,
    checkbox_width=24,
    checkbox_height=24,
    fg_color="#90eb66",
    hover_color="#ffffff",
    checkmark_color="#ffffff",
    corner_radius=4,
    border_width=3,
    text="Incluir símbolos (!@#...)",
    textvariable = texto_checkbox,
    onvalue=True,
    offvalue=False,
    variable=simb_checkbox,
    font=("Montserrat", 16, "bold"),
)
checkbox_minusc.grid(row=3,column=0,pady=4, sticky="w")

#TEXTO-------------------------------------------------------------------------------------------------------------------------------------------------------------------
contra_text = CTkEntry(
    master=frame_principal,
    width=14,
    border_color="#c4c4c4",
    border_width=2,
    height=4,
    corner_radius=0,
    font=("Montserrat", 16),
)
contra_text.grid(row=3,column=0,sticky="we", padx=14)

#BOTONES FINALES-------------------------------------------------------------------------------------------------------------------------------------------------------------------
frame_inferior=CTkFrame(master=frame_principal,
                        corner_radius=0,
                        fg_color="transparent")
frame_inferior.grid(row=4, column=0)
 
frame_inferior.grid_columnconfigure(0,weight=1)
frame_inferior.grid_rowconfigure(0, weight=1)
frame_inferior.grid_rowconfigure(0,weight=1)

generar_contraseña = CTkButton (master=frame_inferior,
                    width=300,
                    height=40,
                    corner_radius=0,
                    fg_color="#e768c1",
                    hover_color="#da81c6",
                    text="GENERAR",
                    anchor="center",
                    command=generar_contra,
                    font=("Montserrat", 16, "bold"))
generar_contraseña.grid( row=0, column=0,)
boton_copiar = CTkButton (master=frame_inferior,
                    width=300,
                    height=40,
                    corner_radius=0,
                    fg_color="#e768c1",
                    hover_color="#da81c6",
                    text="COPIAR AL PORTA PAPELES",
                    command= copiar_texto,
                    anchor="center",
                    font=("Montserrat", 16, "bold"))
boton_copiar.grid( row=1, column=0, sticky="snew", pady=4)

ventana.mainloop()
