from customtkinter import *

set_default_color_theme("dark-blue")
set_appearance_mode("light")

#=========================================================================================================
#VENTANA
#=========================================================================================================
ventana = CTk()
ventana.title("AGENDA DE TAREAS")
ventana.geometry("820x740")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
#=========================================================================================================
#COLORES
#=========================================================================================================
color_fondo= "#e3e5f3"
color_azul= "#563af5"
color_azul_2="#301ecf"
color_verde="#81dc00"
color_verde_2="#93e5a1"
color_blanco="#ffffff"
color_negro="#000000"
#=========================================================================================================
#BOTONES
#=========================================================================================================
estilo_botones={
    "width":220,
    "height":35,
    "fg_color":color_verde,
    "hover_color": color_azul_2,
    "text_color":color_blanco,
    "font":("Monteserrat", 16, "bold")}
#=========================================================================================================
#DEFINIR
#=========================================================================================================
def agendar_boton():
    nombre=campo_nombre.get().lower()
    descripcion=campo_descrip.get("1.0","end").strip()
    fecha=campo_fecha.get()
    etiqueta_informacion.configure(text="DATOS CAPTURADOS CORRECTAMENTE")
    etiqueta_informacion.after(3000,lambda:etiqueta_informacion.configure(text=""))
    
    if (not nombre
        or not descripcion
        or not fecha):
        etiqueta_informacion.configure(text="por favor, completa todos los datos")
        etiqueta_informacion.after(3000,lambda:etiqueta_informacion.configure(text=""))
        return
    if not nombre.isalpha():
        etiqueta_informacion.configure(text="El nombre no puede tener numeros")
        etiqueta_informacion.after(3000,lambda:etiqueta_informacion.configure(text=""))
        campo_nombre.configure(border_color="#b84747")
        campo_nombre.after(3000,lambda:campo_nombre.configure(border_color=color_blanco))
        return
    if not fecha.isdigit():
        etiqueta_informacion.configure(text="La fecha no debe de llevar letras")
        etiqueta_informacion.after(3000,lambda:etiqueta_informacion.configure(text=""))
        campo_fecha.configure(border_color="#b84747")
        campo_fecha.after(3000,lambda:campo_nombre.configure(border_color=color_blanco))

    """if not fecha("/", ""):
        etiqueta_informacion.configure(text="Debe llevar (/). Ejemplo: 13/06/2013")
        etiqueta_informacion.after(3000,lambda:etiqueta_informacion.configure(text=""))"""
           

def click_boton_agendar_tarea():
    pestañas.set("AGENDAR TAREA")

def click_boton_agenda():
    pestañas.set("AGENDA")

def limpiar():
    campo_nombre.delete(0,END)
    campo_descrip.delete("0.0",END)
    campo_fecha.delete(0,END)
    

#=========================================================================================================
#FRAME PRINCIPAL 
#=========================================================================================================
frame_principal= CTkFrame(master=ventana,
                          fg_color=color_fondo,
                          corner_radius=0)
frame_principal.grid(row=0, column=0, sticky= "nsew", padx=10, pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=15)
frame_principal.grid_rowconfigure(0, weight=1)



#=========================================================================================================
#FRAME DERECHO 
#=========================================================================================================
frame_derecho=CTkFrame(master=frame_principal,
                       corner_radius=0,
                       fg_color=color_fondo)
frame_derecho.grid(row=0, column=1,sticky="nsew")
frame_derecho.grid_columnconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(1, weight=10)
frame_derecho.grid_propagate(False)
frame_titulo= CTkFrame(master=frame_derecho,
                       corner_radius=0,
                       fg_color=color_azul)
frame_titulo.grid(row=0, column=0,sticky="nsew")
frame_titulo.grid_columnconfigure(0, weight=1)
frame_titulo.grid_rowconfigure(0, weight=1)

titulo=CTkLabel(
    master=frame_titulo,
    fg_color=color_azul,
    text="AGENDA DE TAREAS",
    text_color=color_blanco,
    font=("Montserrat", 16, "bold"),
    justify="center"
)
titulo.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="nsew"
)

#=========================================================================================================
#FRAME DATOS 
#=========================================================================================================
frame_datos=CTkFrame(master=frame_derecho,
                     corner_radius=0,
                     fg_color=color_fondo)
frame_datos.grid(row=1,column=0,sticky="nswe", padx=50)
frame_datos.grid_columnconfigure(0, weight=1)
frame_datos.grid_rowconfigure(0, weight=1)
frame_datos.grid_propagate(False)
#=========================================================================================================
#Tabview 
#=========================================================================================================
pestañas= CTkTabview(master=frame_datos,
                     corner_radius=0,
                     fg_color=color_fondo)
pestañas.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10
    )
agendar_tab=pestañas.add("AGENDAR TAREA")
agendar_tab.configure(fg_color=color_fondo)
agendar_tab.grid_columnconfigure(0,weight=1)
agendar_tab.grid_rowconfigure(0,weight=1)

frame_interno_tab_agendar = CTkFrame(
    master=agendar_tab,
    fg_color="transparent")
frame_interno_tab_agendar.grid(row=0,column=0,sticky="nswe")

frame_interno_tab_agendar.grid_columnconfigure([0,1], weight=1)
frame_interno_tab_agendar.grid_rowconfigure([0,1,2,3,4], weight=1)

agenda_tab= pestañas.add("AGENDA")
agenda_tab.configure(fg_color= color_verde_2)
agenda_tab.grid_columnconfigure(0, weight=1)
agenda_tab.grid_rowconfigure(0, weight=1)
frame_interno_tab_agenda=CTkFrame(master=agenda_tab,
                                  corner_radius=0,
                                  fg_color=color_verde_2)
frame_interno_tab_agenda.grid(row=0, column=0)
frame_interno_tab_agenda.grid_columnconfigure(0, weight=1)
frame_interno_tab_agenda.grid_rowconfigure(0, weight=1)


pestañas._segmented_button.grid_forget()

#=========================================================================================================
#NOMBRE 
#========================================================================================================
etiqueta_nombre= CTkLabel(master=frame_interno_tab_agendar,
                          width=150,
                          height=40,
                          text="NOMBRE:",
                          justify="center",
                          font=("Montserrat", 16, "bold"),
                          text_color=color_blanco,
                          fg_color=color_verde
                          )

etiqueta_nombre.grid(row=0, 
                     column=0,
                     sticky="we"
                     )
campo_nombre = CTkEntry(
    master=frame_interno_tab_agendar,
    width=250,
    height=40,
    border_color=color_blanco,
    fg_color=color_blanco,
    text_color=color_negro,
    corner_radius=0,
    justify="center",
    placeholder_text="...",
    font=("Montserrat", 16),
)
campo_nombre.grid(row=0,
                  column=1, 
                  sticky="ew",
                  )

#=========================================================================================================
#DESCRIPCION 
#=========================================================================================================
etiqueta_descripcion= CTkLabel(master=frame_interno_tab_agendar,
                               width=155,
                               height=40,
                               text="DESCRIPCION:",
                               font=("Montserrat", 16, "bold"),
                               justify="center",
                               text_color=color_blanco,
                               fg_color=color_verde
                               )

etiqueta_descripcion.grid(row=1, 
                          columnspan=2,
                          sticky="ews"
                          )

campo_descrip = CTkTextbox(master=frame_interno_tab_agendar,
                         width=155,
                         height=155,
                         fg_color=color_blanco,
                         border_color=color_blanco,
                         text_color=color_negro,
                         corner_radius=0,
                         font=("Montserrat", 16)
                         )

campo_descrip.grid(columnspan=2,
                   rowspan=2,
                   sticky="ewn"
                   )

#=========================================================================================================
#FRAME FECHA 
#=========================================================================================================
etiqueta_fecha= CTkLabel(master=frame_interno_tab_agendar,
                          width=150,
                          height=40,
                          text="FECHA:",
                          font=("Montserrat", 16, "bold"),
                          text_color=color_blanco,
                          fg_color=color_verde
                          )

etiqueta_fecha.grid(row=3, 
                    column=0, 
                    sticky="ew",
                    pady=10
                    )

campo_fecha = CTkEntry(master=frame_interno_tab_agendar,
                       width=250,
                       height=40,
                       corner_radius=0,
                       fg_color=color_blanco,
                       border_color=color_blanco,
                       text_color=color_negro,
                       justify="center",
                       placeholder_text="DD/MM/AA",
                       font=("Montserrat", 16))

campo_fecha.grid(row=3,
                 column=1,
                 sticky="we",
                 pady=10
                 )

#=========================================================================================================
#BOTONES 
#=========================================================================================================
boton_agendar = CTkButton(
    master=frame_interno_tab_agendar,
    width=120,
    height=60,
    corner_radius=5,
    text="AGENDAR",
    fg_color=color_azul,
    hover_color=color_azul_2,
    font=("Montserrat", 16),
    command=agendar_boton
    )

boton_agendar.grid(row=4,
             column=0,
             sticky="we",
             padx=20
             )

boton_limpiar = CTkButton(
    master=frame_interno_tab_agendar,
    width=120,
    height=60,
    corner_radius=5,
    text="LIMPIAR",
    fg_color=color_azul,
    hover_color=color_azul_2,
    font=("Montserrat", 16),
    command=limpiar
    )

boton_limpiar.grid(row=4,
             column=1,
             sticky="we",
             padx=20
             )


#=========================================================================================================
#FRAME IZQUIERDO 
#=========================================================================================================
frame_izquierdo= CTkFrame(master=frame_principal,
                          fg_color=color_azul,
                          corner_radius=0)
frame_izquierdo.grid(row=0, column=0, sticky= "nsew")
frame_izquierdo.grid_propagate(False)

#=========================================================================================================
#BOTONES NAVEGACION
#=========================================================================================================
frame_botones=CTkFrame(master=frame_izquierdo,
                       corner_radius=0,
                       fg_color="transparent")
frame_botones.grid(row=1, column=0, pady=90)

frame_botones.grid_columnconfigure(0, weight=1)
frame_botones.grid_rowconfigure(0, weight=1)
frame_botones.grid_rowconfigure(1, weight=1)

boton_agendar_tarea= CTkButton(
    master=frame_botones,
    width=150,
    height=60,
    text="AGENDAR TAREA",
    anchor="center",
    font=("Montserrat", 16, "bold"),
    fg_color=color_verde,
    hover_color=color_azul_2,
    command=click_boton_agendar_tarea
)

boton_agendar_tarea.grid(
    row=0,
    column=0,
    pady=10,
    padx=20,
)

boton_ver_agenda= CTkButton(
    master=frame_botones,
    width=150,
    height=60,
    text="AGENDA",
    anchor="center",
    font=("Montserrat", 16,"bold"),
    fg_color=color_verde,
    hover_color=color_azul_2,
    command=click_boton_agenda
)

boton_ver_agenda.grid(
    row=1,
    column=0,
    pady=10,
    padx=20
)

etiqueta_informacion = CTkLabel(
    master=frame_datos,
    fg_color="transparent",
    text="",
    anchor = "center",
    font=("Montserrat", 16),)
etiqueta_informacion.grid(row=3,columnspan=2,sticky="nswe")


ventana.mainloop()
