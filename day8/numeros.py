def decorador(funcion):

    def decodar_turno():
        print(f"Su turno es {next(funcion())}")
        print("Aguarde y será atendido")
    return decodar_turno

# Generadores para cada área
def gen_farmacia():
    n = 0
    while True:
        n += 1
        yield f"F-{n}"

def gen_cosmetica():
    n = 0
    while True:
        n += 1
        yield f"C-{n}"

def gen_perfumeria():
    n = 0
    while True:
        n += 1
        yield f"P-{n}"

farmacia = gen_farmacia()
cosmetica = gen_cosmetica()
perfumeria = gen_perfumeria()

@decorador
def turno_cosmetica():
    return cosmetica

@decorador
def turno_farmacia():
    return farmacia

@decorador
def turno_perfumeria():
    return perfumeria
