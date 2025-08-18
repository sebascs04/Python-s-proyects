from pathlib import Path
from os import system
import shutil

def opxion1():
    ruta_base = Path('C:/Users/SEBASTIAN/Desktop/Recetas')
    conjunto_categorias = [cat.name for cat in ruta_base.iterdir() if cat.is_dir()]
    categoria = input("¿Qué categoría escoge? ")

    while categoria not in conjunto_categorias:
        categoria = input("No existe esa categoría, ¿Qué categoría escoge? ")
    dir_categoria = Path(ruta_base, categoria)

    conjunto_recetas = [rec.stem for rec in dir_categoria.iterdir() if rec.is_file()]

    if len(conjunto_recetas) == 0:
        print("No existe ninguna receta en esta categoría")
    else:
        receta = input("¿Qué receta quiere leer? ").strip()
        while receta not in conjunto_recetas:
            receta = input("No existe esa receta, ¿Qué receta quiere leer? ").strip()
        dir_archivo = Path(dir_categoria, receta).with_suffix('.txt')
        print(f"{dir_archivo.read_text()}\n")

    input("Presione cualquier letra para volver al inicio: ")
    system('cls')
    bienvenida()


def opxion2():
    ruta_base = Path('C:/Users/SEBASTIAN/Desktop/Recetas')
    conjunto_categorias = [cat.name for cat in ruta_base.iterdir() if cat.is_dir()]
    categoria = input("¿Qué categoría escoge? ")

    while categoria not in conjunto_categorias:
        categoria = input("No existe esa categoría, ¿Qué categoría escoge? ")
    dir_categoria = Path(ruta_base, categoria)

    conjunto_recetas = [rec.stem for rec in dir_categoria.iterdir() if rec.is_file()]
    nombre_receta = input("Ingrese el nombre de la receta: ").strip()

    while nombre_receta in conjunto_recetas or nombre_receta == "":
        if nombre_receta == "":
            nombre_receta = input("No puede ser vacío, vuelva a ingresar otro nombre: ").strip()
        else:
            nombre_receta = input("Esta receta ya existe, vuelva a ingresar otro nombre: ").strip()

    receta = Path(dir_categoria,nombre_receta).with_suffix('.txt')

    contenido_receta = input("Ahora ingrese el contenido de la receta: ")
    receta.write_text(contenido_receta)
    input("Se creó la receta con exito. Presione cualquier letra para volver al inicio: ")
    system('cls')
    bienvenida()


def opxion3():
    ruta_base = Path('C:/Users/SEBASTIAN/Desktop/Recetas')
    conjunto_categorias = [cat.name for cat in ruta_base.iterdir() if cat.is_dir()]
    nombre_categoria = input("¿Qué categoría nueva quiere agregar? ")

    while nombre_categoria in conjunto_categorias or nombre_categoria == "":
        if nombre_categoria == "":
            nombre_categoria = input("No puede ser vacío, vuelva a ingresar otro nombre: ")
        else:
            nombre_categoria = input("Esta categoría ya existe, vuelva a ingresar otro nombre: ")

    nueva_categoria = Path(ruta_base, nombre_categoria.strip())
    nueva_categoria.mkdir()

    input("Se creó la categoría con exito. Presione cualquier letra para volver al inicio: ")
    system('cls')
    bienvenida()


def opxion4():
    ruta_base = Path('C:/Users/SEBASTIAN/Desktop/Recetas')
    conjunto_categorias = [cat.name for cat in ruta_base.iterdir() if cat.is_dir()]
    categoria = input("¿Qué categoría escoge? ")

    while categoria not in conjunto_categorias:
        categoria = input("No existe esa categoría, ¿Qué categoría escoge? ")
    dir_categoria = Path(ruta_base, categoria)

    conjunto_recetas = [rec.stem for rec in dir_categoria.iterdir() if rec.is_file()]

    if len(conjunto_recetas) == 0:
        print("No existe ninguna receta en esta categoría")
    else:
        receta = input("¿Qué receta quiere eliminar? ").strip()
        while receta not in conjunto_recetas:
            receta = input("No existe esa receta, ¿Qué receta quiere eliminar? ").strip()
        dir_archivo = Path(dir_categoria, receta).with_suffix('.txt')
        dir_archivo.unlink()
        print(f"La receta {receta} eliminada\n")

    input("Presione cualquier letra para volver al inicio: ")
    system('cls')
    bienvenida()

def opxion5():
    ruta_base = Path('C:/Users/SEBASTIAN/Desktop/Recetas')
    conjunto_categorias = [cat.name for cat in ruta_base.iterdir() if cat.is_dir()]
    nombre_categoria = input("¿Qué categoría quiere eliminar? ")

    while nombre_categoria not in conjunto_categorias:
        nombre_categoria = input("Esa categoría no existe para ser eliminada, vuelva a ingresar otro nombre: ")

    nueva_categoria = Path(ruta_base, nombre_categoria.strip())
    shutil.rmtree(nueva_categoria)

    input("Se eliminó la categoría con exito. Presione cualquier letra para volver al inicio: ")
    system('cls')
    bienvenida()

def opxion6():
    print("Gracias por su visita!!! Nos vemos.")

def contador_recetas():
    cantidad_recetas = 0
    ruta_recetas = Path('C:/Users/SEBASTIAN/Desktop/Recetas')
    for txt in ruta_recetas.glob('**/*.txt'):
        cantidad_recetas += 1
    return cantidad_recetas

def escoger_opcion():
    opcion = ''
    opciones = ['1. Leer receta','2. Nueva receta','3. Nueva categoria','4. Eliminar receta','5. Eliminar categoría','6. Finalizar']
    for o in opciones:
        print(o)
    while opcion not in ['1','2','3','4','5','6']:
        opcion = input(f"Escoga una opcion: ")
    return opcion

def opciones(opcion):
    if opcion == '1':
        opxion1()
    elif opcion == '2':
        opxion2()
    elif opcion == '3':
        opxion3()
    elif opcion == '4':
        opxion4()
    elif opcion == '5':
        opxion5()
    else:
        opxion6()

def bienvenida():
    ruta_recetas = Path('C:/Users/SEBASTIAN/Desktop/Recetas')
    print(f"Bienvenido! La carpeta de recetas se encuentra en {ruta_recetas} y hay "
          f"{contador_recetas()} recetas en total.\nEstas son la opciones que usted puede hacer:")
    opciones(escoger_opcion())

bienvenida()

