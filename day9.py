import os
import time
import datetime
import re
import pathlib
import math


def buscador():
    ruta = 'C:\\Users\\SEBASTIAN\\Desktop\\Python TOTAL - Programador Avanzado en 16 días\\day9\\Extraxxion terminada\\Mi_gran_directorio'
    patron = r'N[a-zA-Z]{3}-\d{5}'
    i = 0
    inicio = time.time()
    fecha = datetime.date.today().strftime("%d/%m/%Y")
    print('----------------------------------------------------')
    print(f'Fecha de búsqueda: {fecha}')
    print(f'ARCHIVO\t\t\t\tNRO. SERIE')
    print(f'-------\t\t\t\t----------')
    for carpeta,subcarpeta,archivo in os.walk(ruta):
        for arch in archivo:
            texto = pathlib.Path(carpeta,arch).read_text()
            busqueda = re.search(patron,texto)
            if busqueda:
                i+=1
                print(f'{arch}\t\t{busqueda.group()}')
    final = time.time()
    print(f'Números encontrados {i}')
    print(f'Duración de la búsqueda {math.ceil(final-inicio)} segundos')
    print('----------------------------------------------------')


buscador()


