from random import *

palitos = ["-", "--", "---", "----"]

def mezclar(lista):
    shuffle(lista)
    return lista

def intento(lista):
    print("Bienvenido. Su objetivo es encontrar el palito más largo ('----').")
    print("Por favor, seleccione una posición entre el 1 y el 4:")

    intentos = 5
    # Buscamos la posición correcta para mostrarla si pierde
    palitoLargo = lista.index("----") + 1 
    
    try:
        num = int(input("Ingrese un número: "))
    except ValueError:
        num = 0 # Si escriben letras, lo convertimos en 0 para que caiga en error
    
    while True:
        # Validación de rango
        if num not in [1, 2, 3, 4]:
            intentos -= 1
            print(f"Entrada inválida. El número debe estar entre 1 y 4. Se ha restado un intento. Intentos restantes: {intentos}")
            
            if intentos > 0:
                try:
                    num = int(input("Intente nuevamente: "))
                except ValueError:
                    num = 0
        else:
            # Lógica del juego
            seleccionado = lista[num-1]
            
            if seleccionado != "----":
                intentos -= 1
                print(f"Incorrecto. Ha seleccionado el palito '{seleccionado}'. Le quedan {intentos} intentos.")
                
                if intentos > 0:
                    try:
                        num = int(input("Seleccione otra posición: "))
                    except ValueError:
                        num = 0
            else:
                return f"¡Felicidades! Ha encontrado el palito más largo '{seleccionado}'. Has ganado."

        # Condición de derrota
        if intentos == 0:
            return f"Juego terminado. Se han agotado sus intentos. El palito largo estaba en la posición: {palitoLargo}"

mezclados = mezclar(palitos)
print(intento(mezclados))