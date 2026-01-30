from pathlib import Path
from os import *
import shutil

ruta_recetario = Path("C:/Users/thomas.aldana/Documents/prueba PY/Recetas")



print("-------------------------\n Bienvenido Chef Thomas\n-------------------------")
print("\n")
print("Estas en la carpeta de recetas:",ruta_recetario)
print("Recetas que estan en su inventario:")
print("\n")

def mostrar_recetas(ruta_recetario):
    for indice, archivo in enumerate(ruta_recetario.rglob("*.txt"),start=1):
        print(indice,"-",archivo.name)
    print("\n")


def mostrar_categorias(ruta_recetario):
    categorias = [c.name for c in ruta_recetario.iterdir() if c.is_dir()]

    for indice, nombre in enumerate(categorias, start=1):
        print(indice, "-", nombre)

    return categorias




#Cuestionario de opciones


def opciones(ruta_recetario):

    mostrar_recetas(ruta_recetario)
    print("¿Que accion desea realizar? Por favor digite una de las opciones siguientes: \n")
    print("1. - Mostrar Recetas.\n2. - Crear Receta.\n3. - Crear Categoria.\n4. - Eliminar Receta.\n5. - Eliminar Categoria.\n6. - Finalizar el programa\n")

    opcion = int(input("Opcion: "))

    while(opcion != 6):
        if(opcion not in [1,2,3,4,5]):
            opcion = int(input("Intente de nuevo opcion no valida:  "))
        
        match (opcion):
            case 1:
                leer_recetas(ruta_recetario)
                print("\nDesea hacer algo mas? \n")
                print("1. - Mostrar Recetas.\n2. - Crear Receta.\n3. - Crear Categoria.\n4. - Eliminar Receta.\n5. - Eliminar Categoria.\n6. - Finalizar el programa\n")
                opcion = int(input("Opcion: "))
            case 2:
                crear_receta(ruta_recetario)
                print("\nDesea hacer algo mas? \n")
                print("1. - Mostrar Recetas.\n2. - Crear Receta.\n3. - Crear Categoria.\n4. - Eliminar Receta.\n5. - Eliminar Categoria.\n6. - Finalizar el programa\n")
                opcion = int(input("Opcion: "))
                
            case 3:
                crear_categoria(ruta_recetario)
                print("\nDesea hacer algo mas? \n")
                print("1. - Mostrar Recetas.\n2. - Crear Receta.\n3. - Crear Categoria.\n4. - Eliminar Receta.\n5. - Eliminar Categoria.\n6. - Finalizar el programa\n")
                opcion = int(input("Opcion: "))
                
            case 4:
                eliminar_receta(ruta_recetario)
                print("\nDesea hacer algo mas? \n")
                print("1. - Mostrar Recetas.\n2. - Crear Receta.\n3. - Crear Categoria.\n4. - Eliminar Receta.\n5. - Eliminar Categoria.\n6. - Finalizar el programa\n")
                opcion = int(input("Opcion: "))
                
            case 5:
                eliminar_categoria(ruta_recetario)
                print("\nDesea hacer algo mas? \n")
                print("1. - Mostrar Recetas.\n2. - Crear Receta.\n3. - Crear Categoria.\n4. - Eliminar Receta.\n5. - Eliminar Categoria.\n6. - Finalizar el programa\n")
                opcion = int(input("Opcion: "))
                
    print("\n Muchas gracias... Adios \n")

    return opcion


def seleccionar_categoria(ruta_recetario):
    print("\n")

    categorias = mostrar_categorias(ruta_recetario)
    print("\n")
    categoria_seleccionada = int(input("Digite el indice de la categoria (1/2/3..): "))

    while (categoria_seleccionada < 1 or categoria_seleccionada > len(categorias)):
        print("Ese indice de categoria no es valido, por favor ingrese ede nuevo: ")
        categoria_seleccionada = int(input("(1/2/3..): "))
    
    categoria_nombre = categorias[categoria_seleccionada - 1]
    ruta_categoria = ruta_recetario / categoria_nombre

    return ruta_categoria


def seleccionar_receta(ruta_recetario):
    ruta_categoria = seleccionar_categoria(ruta_recetario)

    if not any(ruta_categoria.iterdir()):
        return None
    
    recetas_categoria = []

    print("\n")
    print("Recteas:\n")

    for indice , receta in enumerate(ruta_categoria.glob("*.txt"),start=1):
        recetas_categoria.append(receta.name)
        print(indice,"-",receta.name)
    
    print("\n")
    receta_seleccionada = int(input("Digite el indice de la receta (1/2/3...): "))

    while(receta_seleccionada < 1 or receta_seleccionada > len(recetas_categoria)):
        receta_seleccionada = int(input("Intente de nuevo opcion no valida: "))
    
    receta_nombre = recetas_categoria[receta_seleccionada - 1]
    ruta_receta = ruta_categoria / receta_nombre

    return ruta_receta
    



# Funcion 1 leer o mostrar recetas


def leer_recetas(ruta_recetario):
    ruta_receta = seleccionar_receta(ruta_recetario)

    if(ruta_receta is None):
        print("Esta carpeta no tiene recetas por favor cree una en la opcion 4 o seleccione otra categoria...")
        return

    contenido_ruta = ruta_receta.read_text(encoding="utf-8")

    print("\n")
    print("------------Receta------------\n")
    print(contenido_ruta)


# Funcion 2 crear una nueva receta


def crear_receta(ruta_recetario):
    ruta_categoria = seleccionar_categoria(ruta_recetario)
    print("\n")

    nombre_receta_nueva = input("Digite el nombre de la nueva receta: ")
    contenido_receta_nueva = input("Digite el texto que quiera agregarle a su nueva receta: ")

    nueva_receta = ruta_categoria / f"{nombre_receta_nueva}.txt"
    nueva_receta.write_text(contenido_receta_nueva)

    print("\nReceta creada exitosamente en: ",nueva_receta)


#Funcion 3 Crear categoria


def crear_categoria(ruta_recetario):
    nombre_nueva_categoria = input("Digite el nombre de su nueva categoria: ")

    nueva_categoria = ruta_recetario / nombre_nueva_categoria
    nueva_categoria.mkdir(parents=True, exist_ok = True)

    print("Categoria creada exitosamente en: ",nueva_categoria)

    


#Funcion 4 Eliminar Receta


def eliminar_receta(ruta_recetario):
    ruta_receta = seleccionar_receta(ruta_recetario)
    ruta_receta.unlink()
    print("\nReceta eliminada exitosamente de: ",ruta_receta)
    



#funcion 5 Eliminar categoria


def eliminar_categoria(ruta_recetario):
    ruta_categoria = seleccionar_categoria(ruta_recetario)

    shutil.rmtree(ruta_categoria)

    print("\nCategoria borradda exitosamente de: ",ruta_categoria)


opciones(ruta_recetario)








