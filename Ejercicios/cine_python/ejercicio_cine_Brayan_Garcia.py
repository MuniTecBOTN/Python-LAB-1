from customtkinter import *
set_default_color_theme("green")
set_appearance_mode("dark")
azul="#143a81"
amarillo="#ffcf03"
blanco="#FFFFFF"
rojo="#FF0000"

peliculas={"Pelicula1":["10:00-12:00", "12:00-14:00", "14:00-16:00","15:00-19:00"], 
           "Pelicula2":["9:00-11:00", "11:00-13:00", "13:00-15:00"],
           "Pelicula3":["11:00-12:00", "13:00-14:00"],
           "Pelicula4":["11:00-16:00", "12:00-14:00", "14:00-16:00","22:00-24:00"],
           "Pelicula5":["8:00-12:00", "12:00-16:00", "16:00-18:00"]}

boletos={"NIÑO": 38,
          "VIP": 68,
          "ADULTO": 48,
          #"4DX":100
          }

labels=["PELICULA", "HORARIO", "TIPO BOLETO", "CANTIDAD", "PRECIO UNITARIO", "TOTAL"]

def aumentarCantidad():
    cantidad.set(cantidad.get()+1)
    total.set(cantidad.get()*precioUnitario.get())
    return

def restarCantidad():
    cantidad.set(cantidad.get()-1)
    if cantidad.get()<0:
        cantidad.set(0)
    total.set(cantidad.get()*precioUnitario.get())
    return

def precioPorBoton(self):
    precioUnitario.set(boletos[tipoBoleto.get()])    
    total.set(cantidad.get()*precioUnitario.get())
    return

def setHorarios(self):
    peli=comboPeliculas.get()
    comboHorarios.configure(values=peliculas[peli])
    comboHorarios.set("Seleccione Horario")
    return

def funcComprar():
    horario=comboHorarios.get()
    peli=comboPeliculas.get()
    cant=cantidad.get()
    boleto=tipoBlt.get()
    tot=total.get()
    
    if not peli:
        comboPeliculas.configure(border_color=rojo)
        comboPeliculas.after(1000, lambda: comboPeliculas.configure(border_color=blanco))
        return
        
    if not horario or horario.lower()=="seleccione horario":
        comboHorarios.configure(border_color=rojo)
        comboHorarios.after(1000, lambda: comboHorarios.configure(border_color=blanco))
        return
    
    if not boleto:
        tipoBlt.configure(fg_color=rojo)
        tipoBlt.after(1000, lambda: tipoBlt.configure(fg_color=azul))
        return
     
    if not cant:
        entrycantidad.configure(border_color=rojo)
        entrycantidad.after(1000, lambda: entrycantidad.configure(border_color=blanco))
        return   
    print(f"{peli} {horario} {cant} {boleto} {tot}")
    return

def funcLimpiar():
    comboHorarios.set("")
    comboPeliculas.set("")
    cantidad.set(0)
    tipoBlt.set("")
    precioUnitario.set(0)
    total.set(0)
    return
ventana=CTk()
ventana.geometry("600x600")
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
frameprincipal=CTkFrame(master=ventana,
                        corner_radius=0,
                        fg_color=azul)
cantidad=IntVar(value=0)
frameprincipal.grid_columnconfigure(0, weight=1)
frameprincipal.grid_rowconfigure(0, weight=1)
frameprincipal.grid_rowconfigure(1, weight=3)
frameprincipal.grid_rowconfigure(2, weight=1)


titulo=CTkLabel(master=frameprincipal,
                text="CINE _NOMBRE_",
                font=("Montserrat", 20, "bold"),
                text_color=blanco)
titulo.grid(row=0, column=0)

frameForm=CTkFrame(master=frameprincipal,
                   fg_color="#E0EAFF",
                   corner_radius=0,
                   border_color="#E0EAFF",)

frameForm.grid_columnconfigure(0, weight=1)
frameForm.grid_columnconfigure(1, weight=1)


for i, lbl in enumerate(labels):
    frameForm.grid_rowconfigure(i, weight=1)
    label=CTkLabel(
        master=frameForm,
        fg_color=amarillo,
        text_color=blanco,
        width=130,
        height=30,
        text=lbl,
        font=("Montserrat", 12)
    )
    label.grid(row=i, column=0, sticky="e",padx=5)
frameForm.grid_rowconfigure(len(labels), weight=1)
    
comboPeliculas=CTkComboBox(master=frameForm,
                           values=list(peliculas.keys()),
                           width=150,
                           height=30,
                           fg_color=blanco,
                           corner_radius=0,
                           border_color=blanco,
                           button_color=amarillo,
                           text_color=azul,
                           dropdown_fg_color=blanco,
                           dropdown_hover_color=amarillo,
                           button_hover_color=amarillo,
                           dropdown_text_color=azul,
                           command=setHorarios,
                           state="readonly"
                           )
comboPeliculas.grid(row=0, column=1, sticky="w", padx=5)

comboHorarios=CTkComboBox(master=frameForm,
                           values=[],
                           width=150,
                           height=30,
                           fg_color=blanco,
                           corner_radius=0,
                           border_color=blanco,
                           button_color=amarillo,
                           text_color=azul,
                           dropdown_fg_color=blanco,
                           dropdown_hover_color=amarillo,
                           button_hover_color=amarillo,
                           dropdown_text_color=azul,
                           state="readonly"
                           )
comboHorarios.grid(row=1, column=1, sticky="w", padx=5)

tipoBoleto=StringVar()
tipoBlt=CTkSegmentedButton(master=frameForm,
                        values=list(boletos.keys()),
                        fg_color=azul,
                        text_color=blanco,
                        variable=tipoBoleto,
                        height=30,
                        width=150,
                        corner_radius=0,
                        selected_color=amarillo,
                        selected_hover_color=amarillo,
                        unselected_color=azul,
                        command=precioPorBoton
                        )

frameCantidad=CTkFrame(master=frameForm,
                       fg_color="transparent",
                       corner_radius=0)

frameCantidad.grid_rowconfigure(0, weight=1)
frameCantidad.grid_columnconfigure(0, weight=1)
frameCantidad.grid_columnconfigure(1, weight=1)
frameCantidad.grid_columnconfigure(2, weight=1)

btnmas=CTkButton(master=frameCantidad, 
                 fg_color=azul, 
                 text="+",
                 font=("Montserrat", 16, "bold"),
                 height=30,
                 width=30,
                 command=aumentarCantidad, 
                 corner_radius=0)

btnmenos=CTkButton(master=frameCantidad, 
                 fg_color=azul, 
                 text="-",
                 font=("Montserrat", 16, "bold"),
                 height=30,
                 width=30,
                 command=restarCantidad,
                 corner_radius=0)

entrycantidad=CTkEntry(master=frameCantidad,
                       fg_color="transparent",
                       text_color=azul,
                       border_color="#E0EAFF",
                       height=30,
                       width=40,
                       font=("Montserrat", 16, "bold"),
                       state="readonly",
                       textvariable=cantidad,
                       justify="center")

entrycantidad.grid(row=0, column=1, sticky="w", padx=5)
btnmas.grid(row=0, column=2, sticky="w", padx=5)
btnmenos.grid(row=0, column=0, sticky="w", padx=5)
frameCantidad.grid(row=3, column=1, sticky="w", padx=5)
tipoBlt.grid(row=2, column=1, sticky="w", padx=5)

precioUnitario=IntVar(value=0)
precioUn=CTkEntry(master=frameForm,
                       fg_color="transparent",
                       text_color=azul,
                       border_color="#E0EAFF",
                       height=30,
                       width=40,
                       font=("Montserrat", 16, "bold"),
                       state="readonly",
                       textvariable=precioUnitario,
                       justify="left",
                       )


precioUn.grid(row=4, column=1, sticky="w", padx=5)
total=IntVar(value=0)
totalEntry=CTkEntry(master=frameForm,
                       fg_color="transparent",
                       text_color=azul,
                       border_color="#E0EAFF",
                       height=30,
                       width=60,
                       font=("Montserrat", 16, "bold"),
                       state="readonly",
                       textvariable=total,
                       justify="left",
                       )

totalEntry.grid(row=5, column=1, sticky="w", padx=5)
frameForm.grid(row=1, column=0, sticky="snew")

frameBotones=CTkFrame(
    master=frameForm,
    corner_radius=0,
    fg_color="#E0EAFF",
    border_color="#E0EAFF",
)
frameBotones.grid_columnconfigure(0, weight=1)
frameBotones.grid_columnconfigure(1, weight=1)
frameBotones.grid_rowconfigure(0, weight=1)
btnLimpiar=CTkButton(master=frameBotones,
                     fg_color=azul,
                     text="Limpiar",
                     width=100,
                     height=30,
                     font=("Montserrat", 16),
                     text_color=blanco,
                     corner_radius=0,
                     command=funcLimpiar)

btnComprar=CTkButton(master=frameBotones,
                     fg_color=azul,
                     text="comprar",
                     width=100,
                     height=30,
                     font=("Montserrat", 16),
                     text_color=blanco,
                     corner_radius=0,
                     command=funcComprar)

btnComprar.grid(row=0, column=1, sticky="w", padx=10)
btnLimpiar.grid(row=0, column=0, sticky="e", padx=10)

frameBotones.grid(row=6, column=0, sticky="snwe", columnspan=2)
frameprincipal.grid(row=0, column=0, sticky="snwe")

ventana.mainloop()