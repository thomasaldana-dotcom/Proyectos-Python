from os import system

def decorar_turnos(funcion):
    def envoltorio(turno):
        print("\nTurno recibido\n")
        funcion(turno)
        print("\nPor favor siéntese mientras lo llamamos\n")
    return envoltorio


def mostrar_turno(turno):
    print(turno)


def turnos_perfumaria():
    turno_p = 1
    while True:
        yield f"P - {turno_p}"
        turno_p += 1


def turnos_cosmetica():
    turno_c = 1
    while True:
        yield f"C - {turno_c}"
        turno_c += 1


def turnos_farmacia():
    turno_f = 1
    while True:
        yield f"F - {turno_f}"
        turno_f += 1


