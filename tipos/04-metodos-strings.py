animal = "  HurOn FeLiZ  "
# upper, trasforma mi string a mayusculas
print(animal.upper())  # upper es un método
# lower, transforma mi string a minusculas
print(animal.lower())  # lower es un método
# capitalize método para hacer mayuscula la primer letra
print(animal.strip().capitalize())
# title, método para hacer en mayusculas la primer letra de cada palabra
print(animal.title())
# strip, método para eliminar los espacios del string
# lstrip, método para eliminar espacios a mi izquierda
# rstrip, método para eliminar espacios a mi derecha
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())

# find, busca cadena de caracteres que yo le indique
# Si me da -1 indica que no lo encontró o.o que cool
print(animal.find("Hu"))
# Va a remplazar los caracteres que yo le indique por otros nuevos, necesita 2 argumentos
print(animal.replace("Hu", "jun"))
# de esta forma me devuelve un boolean si es que se encuentra dentro de una variable
# in devuelve true
# not in devuel un false
print("nCH" in animal)
print("nCH" not in animal)
