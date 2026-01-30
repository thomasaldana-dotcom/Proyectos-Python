from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ""
# Precios en Pesos Colombianos (COP)

precios_comidas = [
    28000,  # Pollo
    55000,  # Cordero
    48000,  # Salmon
    42000,  # Calamar
    95000,  # Langosta
    32000,  # Chuleta Valluna
    45000,  # Lomo
    25000,  # Pizza1
    28000,  # Pizza2
    32000,  # Pizza3
    22000,  # Hamburguesa1
    28000,  # Hamburguesa2
    35000,  # Hamburguesa3
    26000,  # Pasta
]

precios_bebidas = [
    4000,   # Agua
    6000,   # limonada
    9000,   # limonada de hierbabuena
    12000,  # limonada de coco
    10000,  # limonada de cereza
    5000,   # Postobon Manzana
    5000,   # Coca cola
    18000,  # Vino1 (Copa)
    25000,  # Vino2 (Copa Premium)
    7000,   # Cerveza1 (Nacional)
    12000,  # Cerveza2 (Importada/Artesanal)
    7000,   # Jugo Natural1
    8500,   # Jugo Natural2
    9000,   # Jugo Natural3
]

precios_postres = [
    6000,   # Helado1
    10000,  # Helado2
    14000,  # Helado3
    8000,   # Fruta
    10000,  # Brownie
    12000,  # Torta
    11000,  # Mil hojas
    9000,   # Flan
    13000,  # Mousse
    4000,   # Galleta1
    5000,   # Galleta2
    15000,  # Torta de chocolate
    4500,   # Gelatina
    11000,  # Postre de limon
]

#funciones
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)

def resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)
    operador = ""

def revisar_check():
    x = 0
    y = 0
    z = 0

    for check in cuadros_comidas:
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state="normal")
            if cuadros_comidas[x].get() == "0":
                cuadros_comidas[x].delete(0, END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state="disabled")
            texto_comidas[x].set("0")
        x += 1
    
    
    for check in cuadros_bebidas:
        if variables_bebidas[y].get() == 1:
            cuadros_bebidas[y].config(state="normal")
            if cuadros_bebidas[y].get() == "0":
                cuadros_bebidas[y].delete(0, END)
            cuadros_bebidas[y].focus()
        else:
            cuadros_bebidas[y].config(state="disabled")
            texto_bebidas[y].set("0")
        y += 1
    
    
    for check in cuadros_postres:
        if variables_postres[z].get() == 1:
            cuadros_postres[z].config(state="normal")
            if cuadros_postres[z].get() == "0":
                cuadros_postres[z].delete(0, END)
            cuadros_postres[z].focus()
        else:
            cuadros_postres[z].config(state="disabled")
            texto_postres[z].set("0")
        z += 1
    



def calcular_total():
    sub_total_comida = 0
    p = 0

    for cantidad in texto_comidas:
        sub_total_comida += (float(cantidad.get()) * precios_comidas[p])
        p += 1
    

    sub_total_bebidas = 0
    p = 0

    for cantidad in texto_bebidas:
        sub_total_bebidas += (float(cantidad.get()) * precios_bebidas[p])
        p += 1
    

    sub_total_postres = 0
    p = 0

    for cantidad in texto_postres:
        sub_total_postres += (float(cantidad.get()) * precios_postres[p])
        p += 1
    
    sub_total = sub_total_comida + sub_total_bebidas + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comidas.set(f"$ {round(sub_total_comida, 1)}")
    var_costo_bebidas.set(f"$ {round(sub_total_bebidas, 1)}")
    var_costo_postres.set(f"$ {round(sub_total_postres, 1)}")
    var_subtotal.set(f"$ {round(sub_total, 1)}")
    var_impuesto.set(f"$ {round(impuestos, 1)}")
    var_total.set(f"$ {round(total, 1)}")
    
    

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(10000,99999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}:{fecha.second}"
    texto_recibo.insert(END, f"-" * 71 + "\n")
    texto_recibo.insert(END, "\t ThomRestaurant\n")
    texto_recibo.insert(END, f"\t Recibo: {num_recibo}\n")
    texto_recibo.insert(END, f"\t Fecha: {fecha_recibo}\n")
    texto_recibo.insert(END, f"-" * 71 + "\n")
    texto_recibo.insert(END, "Items\t\tCantidad\t\tPrecio\n")
    texto_recibo.insert(END, f"-" * 71 + "\n")

    x = 0
    for comida in texto_comidas:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t\t{int(comida.get()) * precios_comidas[x]}\n")
        x += 1
    
    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t\t{int(bebida.get()) * precios_bebidas[x]}\n")
        x += 1
    
    x = 0
    for postre in texto_postres:
        if postre.get() != "0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postre.get()}\t\t{int(postre.get()) * precios_postres[x]}\n")
        x += 1
    
    texto_recibo.insert(END, f"-" * 71 + "\n")
    texto_recibo.insert(END, f"Costo de la comida:\t\t\t{var_costo_comidas.get()}\n")
    texto_recibo.insert(END, f"Costo de las bebidas:\t\t\t{var_costo_bebidas.get()}\n")
    texto_recibo.insert(END, f"Costo de los postres:\t\t\t{var_costo_postres.get()}\n")

    texto_recibo.insert(END, f"-" * 71 + "\n")
    texto_recibo.insert(END, f"Subtotal:\t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuesto:\t\t\t{var_impuesto.get()}\n")

    texto_recibo.insert(END, f"-" * 71 + "\n")
    texto_recibo.insert(END, f"Total:\t\t\t{var_total.get()}\n")


def guardar_recibo():
    info_recibo = texto_recibo.get("1.0", END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("ThomRestaurant", "Recibo guardado correctamente")


def limpiarTodo():
    texto_recibo.delete("0.1", END)

    for texto in texto_comidas:
        texto.set("0")
    for texto in texto_bebidas:
        texto.set("0")
    for texto in texto_postres:
        texto.set("0")

    for cuadro in cuadros_comidas:
        cuadro.config(state="disabled")
    for cuadro in cuadros_bebidas:  
        cuadro.config(state="disabled")
    for cuadro in cuadros_postres:
        cuadro.config(state="disabled")
    
    for variables in variables_comidas:
        variables.set(0)
    for variables in variables_bebidas:
        variables.set(0)
    for variables in variables_postres:
        variables.set(0)

    var_costo_comidas.set("0")
    var_costo_bebidas.set("0")
    var_costo_postres.set("0")
    var_subtotal.set("0")
    var_impuesto.set("0")
    var_total.set("0")

# inicar Tkinter
aplicacion = Tk()

# tamaño ventana
aplicacion.geometry("1420x700")

# evitar agrandar
aplicacion.resizable(0, 0)

# titulo ventana
aplicacion.title("ThomRestaurant - Sistema de Facturacion")

# color de la ventana
aplicacion.config(bg="#1c1c1c")

# colores y fuentes
color_fondo = "#1c1c1c"
color_paneles = "#2a2a2a"
color_texto = "#d1d1d1"
fuente_titulo = ("Copperplate Gothic Bold", 33)
fuente_subtitulo = ("Copperplate Gothic Bold", 16, "bold")
fuente_items = ("Georgia", 11, "bold")

# Barra de navegacion
barra_navegacion = Frame(aplicacion, bd=2, relief=FLAT, bg=color_fondo)
barra_navegacion.pack(side=TOP)

# etiqueta_titulo
etiqueta_titulo = Label(
    barra_navegacion,
    text="ThomRestaurant",
    fg="#ffffff",
    font=fuente_titulo,
    bg=color_fondo,
    width=60,
    highlightthickness=1,
    highlightbackground="white",
)
etiqueta_titulo.grid(row=0, column=0, pady=15)


# paneles izquierdo
panel_izquierdo = Frame(aplicacion, bd=2, relief=FLAT, bg=color_fondo)
panel_izquierdo.pack(side=LEFT)

# Sub-panel para los menus (Comida, Bebida, Postres)
panel_menu = Frame(panel_izquierdo, bd=2, relief=FLAT, bg=color_fondo)
panel_menu.pack(side=TOP)

# panel comidas
panel_comidas = LabelFrame(
    panel_menu,
    text="Comidas",
    font=fuente_subtitulo,
    bd=2,
    relief=FLAT,
    fg=color_texto,
    bg=color_fondo,
    highlightthickness=1,
    highlightbackground="white",
)
panel_comidas.pack(side=LEFT, anchor="n")

# panel bebidas
panel_bebidas = LabelFrame(
    panel_menu,
    text="Bebidas",
    font=fuente_subtitulo,
    bd=2,
    relief=FLAT,
    fg=color_texto,
    bg=color_fondo,
    highlightthickness=1,
    highlightbackground="white",
)
panel_bebidas.pack(side=LEFT, anchor="n")

# panel postres
panel_postres = LabelFrame(
    panel_menu,
    text="Postres",
    font=fuente_subtitulo,
    bd=2,
    relief=FLAT,
    fg=color_texto,
    bg=color_fondo,
    highlightthickness=1,
    highlightbackground="white",
)
panel_postres.pack(side=LEFT, anchor="n")

# panel costos
panel_costos = Frame(
    panel_izquierdo,
    bd=2,
    relief=FLAT,
    bg=color_paneles,
    padx=20,
    pady=10,
    highlightthickness=1,
    highlightbackground="white",
)
panel_costos.pack(side=BOTTOM, fill="x")


# paneles derecha
panel_derecho = Frame(aplicacion, bd=2, relief=FLAT, bg=color_fondo)
panel_derecho.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecho, bd=2, relief=FLAT, bg=color_paneles)
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecho, bd=2, relief=FLAT, bg=color_paneles)
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecho, bd=2, relief=FLAT, bg=color_paneles)
panel_botones.pack(padx=40)

# lista de productos
lista_comidas = [
    "Pollo",
    "Cordero",
    "Salmon",
    "Calamar",
    "Langosta",
    "Chuleta Valluna",
    "Lomo",
    "Pizza1",
    "Pizza2",
    "Pizza3",
    "Hamburguesa1",
    "Hamburguesa2",
    "Hamburguesa3",
    "Pasta",
]

lista_bebidas = [
    "Agua",
    "limonada",
    "limonada de hierbabuena",
    "limonada de coco",
    "limonada de cereza",
    "Postobon Manzana",
    "Coca cola",
    "Vino1",
    "Vino2",
    "Cerveza1",
    "Cerveza2",
    "Jugo Natural1",
    "Jugo Natural2",
    "Jugo Natural3",
]

lista_postres = [
    "Helado1",
    "Helado2",
    "Helado3",
    "Fruta",
    "Brownie",
    "Torta",
    "Mil hojas",
    "Flan",
    "Mousse",
    "Galleta1",
    "Galleta2",
    "Torta de chocolate",
    "Gelatina",
    "Postre de limon",
]


# loop para generar botones de comidas
cuadros_comidas = []
texto_comidas = []
variables_comidas = []
contador = 0

for comida in lista_comidas:

    # crear checkbuttoons
    variables_comidas.append("")
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=fuente_items,
        onvalue=1,
        offvalue=0,
        variable=variables_comidas[contador],
        bg=color_fondo,
        fg=color_texto,
        selectcolor=color_paneles,
        activebackground=color_paneles,
        activeforeground=color_texto,
        command=revisar_check
    )
    comida.grid(row=contador, column=0, sticky="w", padx=(0, 15))

    # cuadros de entrada
    cuadros_comidas.append("")
    texto_comidas.append("")
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set("0")
    cuadros_comidas[contador] = Entry(
        panel_comidas,
        font=fuente_items,
        bd=1,
        width=6,
        state="disabled",
        textvariable=texto_comidas[contador],
        bg="#3a3a3a",
        fg="#ffffff",
        disabledbackground="#2a2a2a",
        disabledforeground="#777777",
    )
    cuadros_comidas[contador].grid(row=contador, column=1, padx=(0, 10))

    contador += 1

# loop para generar botones de bebidas
cuadros_bebidas = []
texto_bebidas = []
variables_bebidas = []
contador = 0

for bebida in lista_bebidas:
    variables_bebidas.append("")
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(
        panel_bebidas,
        text=bebida.title(),
        font=fuente_items,
        onvalue=1,
        offvalue=0,
        variable=variables_bebidas[contador],
        bg=color_fondo,
        fg=color_texto,
        selectcolor=color_paneles,
        activebackground=color_paneles,
        activeforeground=color_texto,
        command=revisar_check
    )
    bebida.grid(row=contador, column=0, sticky="w", padx=(0, 15))

    # cuadros de entrada
    cuadros_bebidas.append("")
    texto_bebidas.append("")
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set("0")
    cuadros_bebidas[contador] = Entry(
        panel_bebidas,
        font=fuente_items,
        bd=1,
        width=6,
        state="disabled",
        textvariable=texto_bebidas[contador],
        bg="#3a3a3a",
        fg="#ffffff",
        disabledbackground="#2a2a2a",
        disabledforeground="#777777",
    )
    cuadros_bebidas[contador].grid(row=contador, column=1, padx=(0, 10))

    contador += 1

# loop para generar botones de postres
cuadros_postres = []
texto_postres = []
variables_postres = []
contador = 0

for postre in lista_postres:

    variables_postres.append("")
    variables_postres[contador] = IntVar()
    postre = Checkbutton(
        panel_postres,
        text=postre.title(),
        font=fuente_items,
        onvalue=1,
        offvalue=0,
        variable=variables_postres[contador],
        bg=color_fondo,
        fg=color_texto,
        selectcolor=color_paneles,
        activebackground=color_paneles,
        activeforeground=color_texto,
        command=revisar_check
    )
    postre.grid(row=contador, column=0, sticky="w", padx=(0, 15))

    # cuadros de entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[contador] = StringVar()
    texto_postres[contador].set("0")
    cuadros_postres[contador] = Entry(
        panel_postres,
        font=fuente_items,
        bd=1,
        width=6,
        state="disabled",
        textvariable=texto_postres[contador],
        bg="#3a3a3a",
        fg="#ffffff",
        disabledbackground="#2a2a2a",
        disabledforeground="#777777",
    )
    cuadros_postres[contador].grid(row=contador, column=1, padx=(0, 10))

    contador += 1


# variables
var_costo_comidas = StringVar()
var_costo_comidas.set("0")

var_costo_bebidas = StringVar()
var_costo_bebidas.set("0")

var_costo_postres = StringVar()
var_costo_postres.set("0")

var_costo_total = StringVar()
var_costo_total.set("0")

var_subtotal = StringVar()
var_subtotal.set("0")

var_impuesto = StringVar()
var_impuesto.set("0")

var_total = StringVar()
var_total.set("0")

# etiqeutas de costo y campos de entrada Comidas
etiqueta_costo_comidas = Label(
    panel_costos,
    text="Costo de Comidas",
    font=fuente_items,
    bg=color_paneles,
    fg=color_texto,
)
etiqueta_costo_comidas.grid(row=0, column=0)
texto_costo_comidas = Entry(
    panel_costos,
    font=fuente_items,
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_comidas,
    readonlybackground="#ffffff",
    fg="#000000",
)
texto_costo_comidas.grid(row=0, column=1, padx=20)

# etiquetas de costo y campos de entrada Bebidas
etiqueta_costo_bebidas = Label(
    panel_costos,
    text="Costo de Bebidas",
    font=fuente_items,
    bg=color_paneles,
    fg=color_texto,
)
etiqueta_costo_bebidas.grid(row=1, column=0)
texto_costo_bebidas = Entry(
    panel_costos,
    font=fuente_items,
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_bebidas,
    readonlybackground="#ffffff",
    fg="#000000",
)
texto_costo_bebidas.grid(row=1, column=1, padx=20)

# etiquetas de costo y campos de entrada Postres
etiqueta_costo_postres = Label(
    panel_costos,
    text="Costo de Postres",
    font=fuente_items,
    bg=color_paneles,
    fg=color_texto,
)
etiqueta_costo_postres.grid(row=2, column=0)
texto_costo_postres = Entry(
    panel_costos,
    font=fuente_items,
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_costo_postres,
    readonlybackground="#ffffff",
    fg="#000000",
)
texto_costo_postres.grid(row=2, column=1, padx=20)

# etiquetas de costo y campos de entrada Subtotal
etiqueta_subtotal = Label(
    panel_costos, text="Subtotal", font=fuente_items, bg=color_paneles, fg=color_texto
)
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(
    panel_costos,
    font=fuente_items,
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_subtotal,
    readonlybackground="#ffffff",
    fg="#000000",
)
texto_subtotal.grid(row=0, column=3, padx=20)

# etiquetas de costo y campos de entrada Impuesto
etiqueta_impuesto = Label(
    panel_costos, text="Impuesto", font=fuente_items, bg=color_paneles, fg=color_texto
)
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(
    panel_costos,
    font=fuente_items,
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_impuesto,
    readonlybackground="#ffffff",
    fg="#000000",
)
texto_impuesto.grid(row=1, column=3, padx=20)

# etiquetas de costo y campos de entrada Total
etiqueta_total = Label(
    panel_costos, text="Total", font=fuente_items, bg=color_paneles, fg=color_texto
)
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(
    panel_costos,
    font=fuente_items,
    bd=1,
    width=10,
    state="readonly",
    textvariable=var_total,
    readonlybackground="#ffffff",
    fg="#000000",
)
texto_total.grid(row=2, column=3, padx=20)



# botones
botones = ["Total", "Recibo", "Guardar", "Limpiar"]
botones_guardados = []
columnas = 0

for boton in botones:
    boton = Button(
        panel_botones,
        text=boton.title(),
        font=fuente_items,
        fg=color_texto,
        bg=color_paneles,
        bd=1,
        width=9,
        highlightthickness=1,
        highlightbackground="white",
        activebackground=color_texto,
        activeforeground=color_fondo,
    )
    botones_guardados.append(boton)
    boton.grid(row=0, column=columnas, padx=8, pady=10)
    columnas += 1

botones_guardados[0].config(command=calcular_total)
botones_guardados[1].config(command=recibo)
botones_guardados[2].config(command=guardar_recibo)
botones_guardados[3].config(command=limpiarTodo)






#area recibo
texto_recibo = Text(panel_recibo, font=fuente_items, bd=1, width=43, height=10)
texto_recibo.grid(row=0, column=0, padx=10, pady=10)

#Calculadora

visor_calculadora = Entry(panel_calculadora, font=fuente_items, bd=1, width=43)
visor_calculadora.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#botones calculadora
botones_calculadora = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "x",
    "0", "Borrar", "=", "/",
]

bototnes_guardados = []

filas = 1
columnas = 0

for boton in botones_calculadora:
    boton = Button(
        panel_calculadora,
        text=boton.title(),
        font=fuente_items,
        fg=color_texto,
        bg=color_paneles,
        bd=1,
        width=8,
        highlightthickness=1,
        highlightbackground="white",
        activebackground=color_texto,
        activeforeground=color_fondo,
    )
    bototnes_guardados.append(boton)

    boton.grid(row=filas, column=columnas, padx=8, pady=10)

    if columnas == 3:
        filas += 1

    columnas += 1

    if columnas == 4:
        columnas = 0

bototnes_guardados[0].config(command=lambda: click_boton("7"))
bototnes_guardados[1].config(command=lambda: click_boton("8"))
bototnes_guardados[2].config(command=lambda: click_boton("9"))
bototnes_guardados[3].config(command=lambda: click_boton("+"))

bototnes_guardados[4].config(command=lambda: click_boton("4"))
bototnes_guardados[5].config(command=lambda: click_boton("5"))
bototnes_guardados[6].config(command=lambda: click_boton("6"))
bototnes_guardados[7].config(command=lambda: click_boton("-"))

bototnes_guardados[8].config(command=lambda: click_boton("1"))
bototnes_guardados[9].config(command=lambda: click_boton("2"))
bototnes_guardados[10].config(command=lambda: click_boton("3"))
bototnes_guardados[11].config(command=lambda: click_boton("*"))

bototnes_guardados[12].config(command=lambda: click_boton("0"))
bototnes_guardados[13].config(command=borrar)
bototnes_guardados[14].config(command=resultado)
bototnes_guardados[15].config(command=lambda: click_boton("/"))

# mantener ventana abierta
aplicacion.mainloop()
