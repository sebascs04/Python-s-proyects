import numeros
from os import system

def mostrar_menu():
    opciones = ["0. Sacar turno en Perfumeria",
                "1. Sacar turno en Farmacia",
                "2. Sacar turno en Cosmetica",
                "3. Finalizar programa"]
    for op in opciones:
        print(op)


def inicio():
    opcion = ''
    print("Bienvenido")
    mostrar_menu()

    while opcion != '3':
        opcion = input("¿Que desea hacer? ")

        while opcion not in ['0', '1', '2', '3']:
            opcion = input("Opción invalida. Escoga nuevamente: ")

        system('cls')

        if opcion == '2':
            numeros.turno_perfumeria()
        elif opcion == '1':
            numeros.turno_farmacia()
        else:
            numeros.turno_cosmetica()

        print("Desea sacar otro turno?")
        mostrar_menu()

    else:
        system('cls')
        print("Gracias por su visita. Vuelva pronto.")

inicio()