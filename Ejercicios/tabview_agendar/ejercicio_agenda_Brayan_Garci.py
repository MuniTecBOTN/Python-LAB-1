from customtkinter import *
import re
set_default_color_theme("green")
set_appearance_mode("dark")
fondo="#d3ddff"
azul ="#1A0FB1"
blanco ="#FFFFFF"
verde ="#1FC035"
rojo="#FF0000"
regexFecha=r'^[0-3][0-9]\/[0-1][0-9]\/[0-9]{4}' 
tareas=[]
class Tarea:
    Fecha=""
    Nombre=""
    def __init__(self, nombre, fecha):
        self.Nombre = nombre
        self.Fecha=fecha
    def test():
        print("Prueba")
    def imprimir(self):
        print(f"Nombre: {self.Nombre} Fecha: {self.Fecha}")
    
    
def agendar():
    pestañas.set("Agendar")
    return
def verAgenda():
    pestañas.set("Ver Agenda")
    return
def accionAgendar():
    nombre=entryName.get()
    date=entryFecha.get()
    if not nombre.isalpha():
        entryName.configure(border_color=rojo)
        entryName.after(3000, lambda: entryName.configure(border_color=blanco))
        return
    if not re.match(regexFecha, date):
        entryFecha.configure(border_color=rojo)
        entryFecha.after(3000, lambda: entryFecha.configure(border_color=blanco))
        return    
    tarea=Tarea(nombre, date)
    tarea.imprimir()
    tareas.append(tarea)
    return
def limpiar():
    entryName.delete(0, END)
    entryFecha.delete(0, END)
    return
ventana=CTk()
ventana.geometry("800x600")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.configure(fg_color=fondo)
ventana.resizable(False, False)
########### Inicio Frame lateral Botones
frameLateral=CTkFrame(
    master=ventana,
    corner_radius=0,
    fg_color="transparent"
)
frameLateral.grid_columnconfigure(0, weight=1)
frameLateral.grid_rowconfigure(0, weight=1)
frameLateral.grid_rowconfigure(1, weight=1)
frameLateral.grid(column=0, row=0)

btnAgendar=CTkButton(
    master=frameLateral,
    text="Agendar Tareas",
    width=100,
    command=agendar,
    fg_color=azul,
    text_color=blanco,
    corner_radius=0
)
btnVerAgenda=CTkButton(
    master=frameLateral,
    text="Ver agenda",
    width=100,
    command=verAgenda,
    fg_color=azul,
    text_color=blanco,
    corner_radius=0
)
btnAgendar.grid(row=0, column=0, sticky="s", pady=10)
btnVerAgenda.grid(row=1, column=0, sticky="n", pady=10)
########### fin Frame lateral Botones

########### Inicio Frame principal
framePrincipal=CTkFrame(master=ventana,
                        fg_color="transparent",
                        corner_radius=0,
)
framePrincipal.rowconfigure(0, weight=1)
framePrincipal.rowconfigure(1, weight=3)
framePrincipal.columnconfigure(0, weight=1)

titulo=CTkLabel(
    master=framePrincipal,
    text="Agenda de Tareas",
    font=("Montserrat", 20, "bold"),
    text_color=azul
)
titulo.grid(row=0, column=0)
framePrincipal.grid(row=0, column=1, sticky="snew", padx=10, pady=10)
## Pestañas
pestañas=CTkTabview(
    master=framePrincipal,
    corner_radius=0,
    fg_color="transparent"
)
agendarView=pestañas.add("Agendar")
verAgendaView=pestañas.add("Ver Agenda")
pestañas.grid(row=1, column=0,sticky="snew")
agendarView.grid_rowconfigure(0, weight=1)
agendarView.grid_rowconfigure(1, weight=1)
agendarView.grid_rowconfigure(2, weight=1)
agendarView.grid_rowconfigure(3, weight=1)
agendarView.grid_columnconfigure(0, weight=1)
pestañas._segmented_button.grid_forget()
pestañas.grid_propagate(False)
frameNombre=CTkFrame(master=agendarView, 
                     fg_color="transparent",
                     corner_radius=0
)


frameNombre.grid_rowconfigure(0, weight=1)
frameNombre.grid_columnconfigure(0, weight=1)
frameNombre.grid_columnconfigure(1, weight=1)
frameNombre.grid_columnconfigure(2, weight=1)
frameNombre.grid_columnconfigure(3, weight=1)
labelNombre=CTkLabel(
    master=frameNombre,
    text="Nombre",
    width=100,
    height=30,
    fg_color=verde,
    text_color=blanco,
)
labelFecha=CTkLabel(
    master=frameNombre,
    text="Fecha",
    width=100,
    height=30,
    fg_color=verde,
    text_color=blanco,
)
entryName=CTkEntry(
    master=frameNombre,
    fg_color=blanco,
    border_color=blanco,
    text_color=azul,
    corner_radius=0,
    height=30
)
entryFecha=CTkEntry(
    master=frameNombre,
    fg_color=blanco,
    border_color=blanco,
    text_color=azul,
    corner_radius=0,
    height=30,
    placeholder_text="DD/MM/YYYY"
)
labelNombre.grid(row=0, column=0, sticky="e", padx=4)
entryName.grid(row=0, column=1, sticky="w")
labelFecha.grid(row=0, column=2, sticky="e", padx=4)
entryFecha.grid(row=0, column=3, sticky="we")
frameNombre.grid(row=0, column=0, sticky="w", pady=0)

labelDesripcion=CTkLabel(
    master=agendarView,
    fg_color=verde,
    text="Descripcion",
    font=("Montserrat", 20, "bold"),
    text_color=blanco
)
labelDesripcion.grid(row=1, column=0, sticky="snew")
frameTareas=CTkFrame(
    master=agendarView,
    fg_color=blanco,
    corner_radius=0
)
frameTareas.grid(row=2, column=0, sticky="snew")

frameBotones=CTkFrame(master=framePrincipal,
                      fg_color="transparent",
                      corner_radius=0)
frameBotones.grid_columnconfigure(0, weight=1)
frameBotones.grid_columnconfigure(1, weight=1)
frameBotones.grid_rowconfigure(0, weight=1)
btnAgendarAction= CTkButton(master=frameBotones,
                            text="Agendar",
                            command=accionAgendar,
                            height=30,
                            fg_color=azul,
                            text_color=blanco,
                            border_color=azul,
                            corner_radius=0
                            )
btnLimpiar= CTkButton(master=frameBotones,
                            text="limpiar",
                            command=limpiar,
                            height=30,
                            fg_color=azul,
                            text_color=blanco,
                            border_color=azul,
                            corner_radius=0
                            )
frameBotones.grid(row=3, column=0, sticky="snew")
btnLimpiar.grid(row=0, column=0, sticky="e", padx=10)
btnAgendarAction.grid(row=0, column=1, sticky="w", padx=10)
ventana.mainloop()