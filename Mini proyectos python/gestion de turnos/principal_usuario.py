import gestion_turnos

def inicio():
    perfumaria = turnos_perfumaria()
    cosmetica = turnos_cosmetica()
    farmacia = turnos_farmacia()

    # DECORADOR A MANO (SIN @)
    mostrar_turno_decorado = decorar_turnos(mostrar_turno)

    system("cls")

    while True:

        print("Bienvenido al sistema de turnos \n")
        input("Presione Enter para continuar...")
        system("cls")

        print("""
        1. Turnos Perfumaria
        2. Turnos Cosmetica
        3. Turnos Farmacia
        4. Salir
        \n""")

        op = int(input("Digite la opcion que desea: "))

        if op == 1:
            system("cls")
            mostrar_turno_decorado(next(perfumaria))

        elif op == 2:
            system("cls")
            mostrar_turno_decorado(next(cosmetica))

        elif op == 3:
            system("cls")
            mostrar_turno_decorado(next(farmacia))

        elif op == 4:
            system("cls")
            print("Todo ok, no olvide calificarnos donde sea")
            break

        else:
            system("cls")
            print("Opcion no valida intente otra vez...")


inicio()
