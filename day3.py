texto = input("Ingrese su texto preferido: " )
letra1 = input("Ingrese primera letra: ")
letra2 = input("Ingrese segunda letra: ")
letra3 = input("Ingrese tercera letra: ")

text_list = texto.split(' ')

#1 num de vexes que aparexe xada letra
print(f"1. La letra {letra1},{letra2},{letra3} aparece una cantida de: { texto.lower().count(letra1) },{ texto.lower().count(letra2) },{ texto.lower().count(letra3)} respectivamente")
#2 xuantas palabras hay en total
print(f"2. Las palabras total en el texto son de: {len(text_list)}")
#3 Primera y ultima letra
print(f"3. La primera y ultima letra son: {texto[0]} y {texto[-1]} respectivamente")
#4 palabras en orden inverso
text_list.reverse()
print(f"4. Texto invertido: '{" ".join(text_list)}'")
#5 aparece python ?
print(f"5. ¿Aparece python? {'Sí' if 'python' in texto else 'No'} ")

