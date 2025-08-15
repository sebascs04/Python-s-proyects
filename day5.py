from random import *

palabras = ["manzana", "perro", "cielo", "python", "luna", "estrella", "libro", "gato"]

def fun1():
    palabra = choice(palabras)
    oculta = []
    for caracter in palabra:
        oculta.append('-')
    print(f"Adivina la palabara oculta: {"".join(oculta)}")
    return oculta,palabra

def fun2():
    return list(input("Adivina la palabra: "))

def fun3(palabra_adivinada,palabra_cifrada,palabra_escogida_sistema):
    acerto = False
    for indice, letra_escogida in enumerate(palabra_escogida_sistema):
        if letra_escogida in palabra_adivinada:
            palabra_cifrada[indice] = letra_escogida
            acerto = True
    return acerto

def fun4(palabra_cifrada,palabra_escogida_sistema):
    return "".join(palabra_cifrada) == "".join(palabra_escogida_sistema)

def fun5():
    palabra_cifrada, palabra_escogida_sistema = fun1()
    cantidad_vidas = 6
    while cantidad_vidas >= 0:
        palabra_adivinada = fun2()
        acerto = fun3(palabra_adivinada,palabra_cifrada,palabra_escogida_sistema)
        if acerto == False:
            print(f"Te equivocaste, no acertaste niguna letra, te quedan {cantidad_vidas} \n")
            cantidad_vidas -= 1
        else:
            print(f"Acertaste!! La palabra queda como: {"".join(palabra_cifrada)} \n")
            if fun4(palabra_cifrada,palabra_escogida_sistema):
                print(f"Ganaste!!! Adivinaste la palabra. \n")
                break
    else:
        print(f"Perdiste, la palabra era {palabra_escogida_sistema}")

fun5()
