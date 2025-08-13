from random import *

nombre = input("¿Cual es tu nombre? ")
print(nombre + ", he pensando un numero secreto del 1 al 100. "
      "Tienes 8 intentos para adivinarlo.")
numero_adivinado = int(input("¿Cual es el numero? "))
numero_secreto = randint(1,100)
n = 8
i = 0

while n != 0:
    n -= 1
    i += 1

    if (n == 0):
        print(f"\nQuerido {nombre}, te has quedado sin intentos, el numero secreto era {numero_secreto}")
        break

    if numero_adivinado <1 or numero_adivinado > 100:
        print(f"\nEl numero {numero_adivinado} no es permitido. Tiene que ser mayor que 1 y menor que 100, te quedan {n} intentos")
        numero_adivinado = int(input("Ingresa el numero nuevamente:  "))
    elif numero_adivinado < numero_secreto:
        print(f"\nRespuesta incorrecta. El numero secreto es mayor al que ingresaste, te quedan {n} intentos")
        numero_adivinado = int(input("Ingresa el numero nuevamente: "))
    elif numero_adivinado == numero_secreto:
        print(f"\nFelicidades, has adivinado el numero secreto {numero_secreto} en {i} intentos")
        break
    else:
        print(f"\nRespuesta incorrecta. El numero secreto es menor al que ingresaste, te quedan {n} intentos")
        numero_adivinado = int(input("Ingresa el numero nuevamente:  "))

