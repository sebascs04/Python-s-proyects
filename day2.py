nombre = input("Ingrese su nombre : ")
venta = input("Ingrese su ventas: ")

comision = round(float(venta)*0.13,2)

print(f"Ok {nombre}. Este mes ganaste ${comision} ")
