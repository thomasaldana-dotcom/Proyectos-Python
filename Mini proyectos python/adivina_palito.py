from random import *

palitos = ["-","--","---","----"]

def mezclar(lista):
    shuffle(lista)
    return lista

def intento(lista):
    print("Adivina el palito mas largo.... ¡'----'! Escoja un numero del 1 al 4:")

    intentos = 5
    palitoLargo = lista.index("----") + 1  # usar la lista mezclada
    num = int(input("Numero: "))

    while True:
        if num not in [1,2,3,4]:
            intentos -= 1
            print("Es que acaso no sabe leer, huevon? dice 1 a 4... le voy a quitar un intento, intentos:", intentos)
            num = int(input("Numero: "))
        else:
            seleccionado = lista[num-1]   # usar la lista mezclada
            if seleccionado != "----":
                intentos -= 1
                print(f"Paila marica '{seleccionado}' no era, le quedan {intentos} intentos")
                num = int(input("Numero: "))
            else:
                return f"Muy bien marica lo encontró '{seleccionado}' ese era... 😏"

        if intentos == 0:
            return f"Paila, se quedó sin intentos. El palo largo estaba en el número: {palitoLargo}"

mezclados = mezclar(palitos)
print(intento(mezclados))