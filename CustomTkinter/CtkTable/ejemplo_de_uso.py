from customtkinter import *
from tabla_customtkinter import CTkTable


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

estilo_boton = {
    "width": 200,
    "height": ALTURA_ESTANDAR_CAMPO,
    "fg_color": COLOR_AZUL,
    "hover_color": COLOR_AMARILLO,
    "text_color": COLOR_BLANCO,
    "font": ("Montserrat", TAMAÑO_LETRA_NORMAL, "bold"),
    "corner_radius": 0,
}


def fila_seleccionada(fila):
    print("Fila seleccionada:")
    print(fila)

def mostrar_fila():
    print(tabla["obtener_fila"]())
    
    
def actualizar_tabla(lista_de_datos):
    tabla["actualizar"](lista_de_datos)
    
    
ventana = CTk()
ventana.geometry("1200x800")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)


frame_principal = CTkFrame(
    master=ventana,
    fg_color=COLOR_FONDO)

frame_principal.grid(row=0, column=0, sticky="nsew")

frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)


datos = [
    [1, "Laptop Lenovo IdeaPad", "Computadoras", 4500.00],
    [2, "Mouse Logitech M185", "Accesorios", 120.00],
    [3, "Teclado Mecánico Redragon", "Accesorios", 350.00],
    [4, "Monitor Samsung 24\"", "Monitores", 1200.00],
    [5, "Memoria USB 64GB", "Almacenamiento", 85.00],
    [6, "Disco SSD 512GB", "Almacenamiento", 420.00],
    [7, "Disco HDD 1TB", "Almacenamiento", 390.00],
    [8, "Audífonos Bluetooth", "Audio", 280.00],
    [9, "Bocina JBL Go", "Audio", 450.00],
    [10, "Webcam Logitech HD", "Accesorios", 300.00],
    [11, "Tablet Samsung A9", "Tablets", 1800.00],
    [12, "Smartphone Galaxy A56", "Telefonía", 3200.00],
    [13, "iPhone 14", "Telefonía", 6800.00],
    [14, "Cargador USB-C", "Accesorios", 95.00],
    [15, "Cable HDMI", "Accesorios", 60.00],
    [16, "Router TP-Link", "Redes", 350.00],
    [17, "Switch de Red 8 Puertos", "Redes", 480.00],
    [18, "Impresora Epson EcoTank", "Impresoras", 2100.00],
    [19, "Tinta Epson Negra", "Impresoras", 125.00],
    [20, "Memoria RAM 16GB", "Componentes", 520.00],
    [21, "Tarjeta Gráfica RTX 4060", "Componentes", 3200.00],
    [22, "Procesador Ryzen 5", "Componentes", 1450.00],
    [23, "Placa Madre ASUS B550", "Componentes", 980.00],
    [24, "Fuente de Poder 650W", "Componentes", 580.00],
    [25, "Gabinete Gamer", "Componentes", 720.00],
    [26, "Ventilador RGB", "Componentes", 95.00],
    [27, "Laptop HP Pavilion", "Computadoras", 5200.00],
    [28, "Monitor LG 27\"", "Monitores", 1550.00],
    [29, "Mouse Pad XL", "Accesorios", 110.00],
    [30, "Cámara de Seguridad WiFi", "Seguridad", 480.00],
    [31, "UPS Forza 1000VA", "Energía", 750.00],
    [32, "Regleta Eléctrica", "Energía", 85.00],
    [33, "Teclado Inalámbrico", "Accesorios", 240.00],
    [34, "Smartwatch Xiaomi", "Wearables", 650.00],
    [35, "Pulsera Inteligente", "Wearables", 240.00],
    [36, "Cargador Inalámbrico", "Accesorios", 180.00],
    [37, "Hub USB 4 Puertos", "Accesorios", 140.00],
    [38, "Micrófono USB", "Audio", 320.00],
    [39, "Silla Gamer", "Muebles", 1800.00],
    [40, "Escritorio Gamer", "Muebles", 2400.00],
    [41, "Lámpara LED Escritorio", "Iluminación", 190.00],
    [42, "Proyector Mini", "Proyectores", 950.00],
    [43, "Control Xbox", "Gaming", 650.00],
    [44, "Control PS5", "Gaming", 780.00],
    [45, "Nintendo Switch", "Gaming", 3200.00],
    [46, "SSD NVMe 1TB", "Almacenamiento", 720.00],
    [47, "Disco Externo 2TB", "Almacenamiento", 850.00],
    [48, "Parlantes Genius", "Audio", 250.00],
    [49, "Cable VGA", "Accesorios", 45.00],
    [50, "Mouse Gamer RGB", "Gaming", 320.00],
    [51, "Laptop Dell Inspiron", "Computadoras", 4900.00],
    [52, "Monitor Acer 22\"", "Monitores", 990.00],
    [53, "Memoria USB 128GB", "Almacenamiento", 135.00],
    [54, "Auriculares Gamer", "Gaming", 420.00],
    [55, "Adaptador Bluetooth", "Accesorios", 90.00],
    [56, "Cámara Web Full HD", "Accesorios", 420.00],
    [57, "Mini Teclado Bluetooth", "Accesorios", 180.00],
    [58, "Tablet Lenovo M10", "Tablets", 2100.00],
    [59, "iPad 10ª Gen", "Tablets", 4200.00],
    [60, "Smartphone Redmi Note 14", "Telefonía", 2400.00],
    [61, "Smartphone iPhone SE", "Telefonía", 3700.00],
    [62, "Protector de Pantalla", "Telefonía", 35.00],
    [63, "Funda para Celular", "Telefonía", 75.00],
    [64, "Power Bank 10000mAh", "Energía", 320.00],
    [65, "Extensor WiFi", "Redes", 290.00],
    [66, "Impresora Canon", "Impresoras", 1850.00],
    [67, "Tinta Canon Color", "Impresoras", 140.00],
    [68, "Procesador Intel i5", "Componentes", 1600.00],
    [69, "Tarjeta Madre MSI", "Componentes", 1100.00],
    [70, "RAM DDR5 32GB", "Componentes", 980.00],
    [71, "Fuente 750W Gold", "Componentes", 890.00],
    [72, "Cooler Líquido RGB", "Componentes", 780.00],
    [73, "Laptop ASUS VivoBook", "Computadoras", 4700.00],
    [74, "Monitor Curvo Samsung", "Monitores", 2100.00],
    [75, "Mouse Ergonómico", "Accesorios", 220.00],
    [76, "Kit Teclado + Mouse", "Accesorios", 280.00],
    [77, "Smart TV Box", "Entretenimiento", 550.00],
    [78, "Chromecast", "Entretenimiento", 480.00],
    [79, "Smart Bulb WiFi", "Hogar Inteligente", 130.00],
    [80, "Enchufe Inteligente", "Hogar Inteligente", 160.00],
    [81, "Sensor de Movimiento", "Seguridad", 220.00],
    [82, "Cerradura Inteligente", "Seguridad", 1800.00],
    [83, "UPS APC 1500VA", "Energía", 1250.00],
    [84, "Regulador de Voltaje", "Energía", 280.00],
    [85, "Bocina Bluetooth Sony", "Audio", 850.00],
    [86, "Micrófono Gamer RGB", "Gaming", 540.00],
    [87, "Webcam 4K", "Accesorios", 850.00],
    [88, "Disco SSD 2TB", "Almacenamiento", 1350.00],
    [89, "Teclado Gamer RGB", "Gaming", 420.00],
    [90, "Router WiFi 6", "Redes", 1200.00],
    [91, "Laptop MacBook Air", "Computadoras", 9200.00],
    [92, "Monitor BenQ 32\"", "Monitores", 2800.00],
    [93, "Proyector Epson", "Proyectores", 3500.00],
    [94, "Nintendo Switch OLED", "Gaming", 4200.00],
    [95, "PS5 Slim", "Gaming", 5600.00],
    [96, "Xbox Series S", "Gaming", 3900.00],
    [97, "Cámara IP Exterior", "Seguridad", 620.00],
    [98, "Batería UPS Repuesto", "Energía", 450.00],
    [99, "Cable USB-C a USB-C", "Accesorios", 55.00],
    [100, "Base Refrigerante Laptop", "Accesorios", 260.00],
]

nuevos_datos = [
    (10, "Pedro", "Teclado", 400),
    (11, "Luis", "Monitor", 1500),
    (12, "Mario", "USB", 80)
    ]


tabla = CTkTable(
    master=frame_principal,
    columnas=["ID", "Producto", "Categoria", "Precio"],
    datos=datos,
    row=0,
    column=0,
    padx=20,
    pady=20,
    command=fila_seleccionada
)

   

boton_obtener_fila = CTkButton(
    frame_principal,
    text="Obtener fila",
    command=mostrar_fila,
    **estilo_boton
)
boton_obtener_fila.grid(row=1, column=0, pady=10)


boton_actulizar_tabla = CTkButton(
    frame_principal,
    text="Actualizar tabla",
    command=lambda:actualizar_tabla(nuevos_datos),
    **estilo_boton
)
boton_actulizar_tabla.grid(row=2, column=0, pady=10)


ventana.mainloop()