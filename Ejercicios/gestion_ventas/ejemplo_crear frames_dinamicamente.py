from customtkinter import *

        
productos = {
    "Xiaomi Redmi 15 C": {"codigo": "X001", "precio": 15000, "stock": 100},
    "Samsung Galaxy S25 ULTRA": {"codigo": "S001", "precio": 20000, "stock": 50},
    "Apple iPhone 15 Pro Max": {"codigo": "A001", "precio": 15000, "stock": 75},
    "Huawei P60 Pro": {"codigo": "H001", "precio": 12000, "stock": 80},
    "Laptop Asus ROG Strix G16": {"codigo": "L001", "precio": 25000, "stock": 30},
    "Tablet Samsung Galaxy Tab S8": {"codigo": "T001", "precio": 8000, "stock": 60},
    "aplewhatch series 9": {"codigo": "W001", "precio": 5000, "stock": 40},
    "Audífonos Sony WH-1000XM4": {"codigo": "A002", "precio": 3000, "stock": 90},
    "Sony xperia 1 V": {"codigo": "S002", "precio": 18000, "stock": 70},
}
carrito = []      
# =========================================================
# COLORES
# =========================================================
COLOR_FONDO = "#f0f2f5"
COLOR_AZUL = "#143a81"
COLOR_AMARILLO = "#ffcf03"
COLOR_BLANCO = "#ffffff"
COLOR_ROJO = "#190404"
COLOR_VERDE = "#2ce429"
TRANSPARENTE = "transparent"
ALTURA_ESTANDAR_CAMPO = 50
TAMAÑO_LETRA_NORMAL = 18
TAMAÑO_LETRA_TITULO = 28 
# =========================================================
# ESTILOS
# =========================================================
estilo_etiqueta_titulo = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_TITULO),
    "text_color": COLOR_BLANCO,
    "fg_color": TRANSPARENTE,
}

estilo_etiqueta_normal = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "text_color": COLOR_BLANCO,
    "fg_color": COLOR_AMARILLO,
}

estilo_etiqueta_normal_blanco = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "text_color": COLOR_AZUL,
    "fg_color": COLOR_BLANCO,
}

estilo_etiqueta_normal_azul = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "text_color": COLOR_BLANCO,
    "fg_color": COLOR_AZUL,
}

estilo_campo = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "border_color": COLOR_BLANCO,
    "text_color": COLOR_AZUL,
    "justify": "center",
    "corner_radius": 0,
    "placeholder_text": "...",
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
}

estilo_lista = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "text_color": COLOR_AZUL,
    "button_color": COLOR_AMARILLO,
    "dropdown_fg_color": COLOR_AZUL,
    "dropdown_text_color": COLOR_BLANCO,
    "dropdown_font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "anchor": "center",
    "corner_radius": 0,
    "dynamic_resizing": False,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
}

estilo_boton = {
    "width": 120,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_AZUL,
    "hover_color": COLOR_AMARILLO,
    "text_color": COLOR_BLANCO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL, "bold"),
    "corner_radius": 0,
}

estilo_boton_spinbox = {
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_AZUL,
    "hover_color": COLOR_AMARILLO,
    "text_color": COLOR_BLANCO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL, "bold"),
    "corner_radius": 0,
}

estilo_boton_segmentado = {
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_BLANCO,
    "selected_color": COLOR_AMARILLO,
    "selected_hover_color": COLOR_AMARILLO,
    "unselected_color": COLOR_AZUL,
    "unselected_hover_color": COLOR_AMARILLO,
    "text_color": COLOR_BLANCO,
    "text_color_disabled": COLOR_BLANCO,
    "corner_radius": 0,
    "border_width": 2,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL),
    "dynamic_resizing": False,
}



# =========================================================
# CONFIGURACIÓN GLOBAL
# =========================================================
set_appearance_mode("light")
set_default_color_theme("dark-blue")

# =========================================================
# APP PRINCIPAL
# =========================================================
ventana = CTk()

ventana.title("Sistema de Registro")
ventana.geometry("1600x920")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# =========================================================
# DECLARACIÓN DE FRAMES
# =========================================================
# =========================================================
# FRAME PRINCIPAL
# =========================================================
frame_principal = CTkFrame(
    master=ventana,
    fg_color=COLOR_FONDO,
    corner_radius=0,
)
frame_principal.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10,
)

columna = 0
fila = 0
for producto in productos:
   
    frame_principal.grid_rowconfigure(fila, weight=1)
    frame_principal.grid_columnconfigure(columna, weight=1)
    
    frame_producto = CTkFrame(
        master=frame_principal,
        fg_color=COLOR_BLANCO,
        corner_radius=0,
    )
    frame_producto.grid_rowconfigure(0, weight=10)
    frame_producto.grid_rowconfigure(1, weight=2)
    frame_producto.grid_columnconfigure(0, weight=1)
    
    frame_producto.grid(
        row=fila,
        column=columna,
        sticky="ew",
        padx=10,
        pady=10,
    )
    
    
    etiqueta_producto = CTkLabel(
        master=frame_producto,
        text=producto,
        **estilo_etiqueta_normal_azul
    )
    etiqueta_producto.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=10,
        pady=10,
    )
    etiqueta_precio = CTkLabel(
        master=frame_producto,
        text=f"Q{productos[producto]['precio']}",
        **estilo_etiqueta_normal_azul
    )
    etiqueta_precio.grid(
        row=1,
        column=0,
        sticky="nsew",
        padx=10,
        pady=10,
    )
    columna += 1
    if columna >=2:
        columna = 0
        fila += 1
        

    




# =========================================================
# MAIN LOOP
# =========================================================
ventana.mainloop()
