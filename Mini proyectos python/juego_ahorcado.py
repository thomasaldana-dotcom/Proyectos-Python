import random

palabras = ["python","programa","ahorcado","computador","marica","clave","juego","variable"]
def nueva_palabra():
    return random.choice(palabras).lower()

def jugar():
    palabra = nueva_palabra()
    letras = set(palabra)
    intentos = 6
    usadas = set()
    while intentos > 0 and letras:
        estado = " ".join([c if c in usadas else "_" for c in palabra])
        print(f"\nPalabra: {estado}")
        print(f"Intentos restantes: {intentos}  Letras usadas: {' '.join(sorted(usadas))}")
        intento = input("Adivina una letra: ").strip().lower()
        if not intento or len(intento) != 1 or not intento.isalpha():
            print("Ingresa una sola letra válida.")
            continue
        if intento in usadas:
            print("Ya usaste esa letra.")
            continue
        usadas.add(intento)
        if intento in letras:
            letras.remove(intento)
            print("Bien!")
        else:
            intentos -= 1
            print("Nope.")
    if not letras:
        print(f"\nGanaste! La palabra era: {palabra}")
    else:
        print(f"\nPerdiste. La palabra era: {palabra}")

if __name__ == "__main__":
    while True:
        jugar()
        if input("\nJugar otra vez? (s/n): ").strip().lower() != "s":
            print("Chao.")
            break
