# Define funciones
def hola(nombre, apellido="Feliz"):  # parametros
    print("Hola hurones")
    print("Ultimate ferret")
    print(f"Bienvenido {nombre} {apellido}")


# Argumento, valor que le estoy pasando
# Parametro, nombre de la variable dentro de la función
# Llamo función
hola("Fausto Rubén", "Themar")  # Argumentos
hola("Chanchito")

# aquí defino qué valores se identifican con el parametro de mi función
hola(apellido="Themar", nombre="Fausto Rubén")
