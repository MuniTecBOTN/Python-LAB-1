import customtkinter as ctk
from tkinter import ttk


# =========================================================
# COLORES
# =========================================================
COLOR_AZUL = "#143a81"
COLOR_AMARILLO = "#ffcf03"
COLOR_BLANCO = "#ffffff"

TAMAÑO_LETRA_NORMAL = 18


# =========================================================
# CREAR TABLA
# =========================================================
def CTkTable(
        master,
        columnas,
        datos=None,
        row=0,
        column=0,
        padx=0,
        pady=0,
        sticky="nsew",
        height=12,
        command=None
):

    if datos is None:
        datos = []

    # =====================================================
    # FRAME CONTENEDOR
    # =====================================================
    frame_tabla = ctk.CTkFrame(
        master,
        fg_color=COLOR_BLANCO,
        corner_radius=0
    )

    frame_tabla.grid(
        row=row,
        column=column,
        padx=padx,
        pady=pady,
        sticky=sticky
    )

    frame_tabla.grid_columnconfigure(0, weight=1)
    frame_tabla.grid_rowconfigure(0, weight=1)

    # =====================================================
    # ESTILO
    # =====================================================
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Custom.Treeview",
        background=COLOR_BLANCO,
        foreground=COLOR_AZUL,
        fieldbackground=COLOR_BLANCO,
        rowheight=42,
        borderwidth=0,
        font=("Montserrat", 14)
    )

    style.configure(
        "Custom.Treeview.Heading",
        background=COLOR_AZUL,
        foreground=COLOR_BLANCO,
        font=("Montserrat", 14, "bold"),
        relief="flat"
    )

    style.map(
        "Custom.Treeview",
        background=[("selected", COLOR_AMARILLO)],
        foreground=[("selected", COLOR_AZUL)]
    )

    # =====================================================
    # TREEVIEW
    # =====================================================
    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        style="Custom.Treeview",
        height=height
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(
            col,
            width=150,
            anchor="center"
        )

    tabla.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    # =====================================================
    # SCROLLBAR
    # =====================================================
    scrollbar = ttk.Scrollbar(
        frame_tabla,
        orient="vertical",
        command=tabla.yview
    )

    scrollbar.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    tabla.configure(
        yscrollcommand=scrollbar.set
    )

    # =====================================================
    # INSERTAR DATOS
    # =====================================================
    for fila in datos:
        tabla.insert(
            "",
            "end",
            values=fila
        )

    # =====================================================
    # OBTENER FILA
    # =====================================================
    def obtener_fila():

        seleccion = tabla.selection()

        if seleccion:
            item = tabla.item(seleccion[0])
            return tuple(item["values"])

        return None

    # =====================================================
    # EVENTO DE SELECCIÓN
    # =====================================================
    def al_seleccionar(event=None):

        fila = obtener_fila()

        # Ejecutar callback
        if fila and command:
            command(fila)

    tabla.bind(
        "<<TreeviewSelect>>",
        al_seleccionar
    )

    # =====================================================
    # ACTUALIZAR
    # =====================================================
    def actualizar(nuevos_datos):

        tabla.delete(*tabla.get_children())

        for fila in nuevos_datos:
            tabla.insert(
                "",
                "end",
                values=fila
            )

    # =====================================================
    # INSERTAR FILA
    # =====================================================
    def insertar(fila):

        tabla.insert(
            "",
            "end",
            values=fila
        )

    # =====================================================
    # ELIMINAR FILA
    # =====================================================
    def eliminar_seleccion():

        seleccion = tabla.selection()

        if seleccion:
            tabla.delete(seleccion[0])

    # =====================================================
    # RETORNO
    # =====================================================
    return {
        "treeview": tabla,
        "frame": frame_tabla,
        "obtener_fila": obtener_fila,
        "actualizar": actualizar,
        "insertar": insertar,
        "eliminar_seleccion": eliminar_seleccion
    }