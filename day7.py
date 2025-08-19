from os import system

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self,nombre,apellido,num_cuenta,balance):
        super().__init__(nombre,apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return (f"Información del cliente:\nNombre: {self.nombre}\nApellido: {self.apellido}\n"
                f"Numero de cuenta: {self.num_cuenta}\nBalance: ${self.balance}")

    def depositar(self,monto):
        self.balance +=  monto
        return f"Usted ahora tiene ${self.balance}"

    def retirar(self,monto):
        if self.balance - monto < 0:
            return (f"Usted no cuenta con el saldo suficiente para hacer esta operación. "
                    f"Usted tiene ${self.balance}")
        else:
            self.balance -= monto
            return f"Usted ahora tiene ${self.balance}"


def crear_cliente():
    nombre = input("Ingrese su nombre de cliente: ")
    apellido = input("Ingrese su apellido: ")
    num = input("Ingrese su num de cuenta: ")
    saldo = int(input("Ingrese su saldo: "))
    nuevo_cliente = Cliente(nombre,apellido,num,saldo)
    return nuevo_cliente

def mostrar_menu():
    opciones = ['1. Depositar', '2. Retirar', '3. Información', '4. Salir']
    for op in opciones:
        print(op)

def inicio():
    opcion = ''
    cliente = crear_cliente()
    mostrar_menu()

    while opcion != '4':
        opcion = input("Escoga una opción: ")

        while opcion not in ['1', '2', '3', '4']:
            opcion = input("Opcion invalida. Escoga una opción: ")

        if opcion == '1':
            monto = int(input("Ingrese el monto a depositar: "))
            system('cls')
            print(cliente.depositar(monto))
            mostrar_menu()
        elif opcion == '2':
            monto = int(input("Ingrese el monto a retirar: "))
            system('cls')
            print(cliente.retirar(monto))
            mostrar_menu()
        elif opcion == '3':
            system('cls')
            print(str(cliente))
            mostrar_menu()
    else:
        print(f"Nos vemos pronto {cliente.nombre}, te queda de saldo ${cliente.balance}")

inicio()
