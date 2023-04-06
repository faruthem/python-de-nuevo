print("Bienvenido a la calculadora del niño hurón")
print("escribe salir en lugar de la operación que deseas realizar para salir")
print("Las operaciones son suma, multi, div y resta")

oper = ""
numero = 0
while oper.lower() != "salir":
    numero = int(input("Ingresa un número: "))
    oper = input(
        "Ingresa la operación: ")

    if oper.lower() == "suma":
        numero_2 = int(input("Ingresa el otro número: "))
        resultado = numero + numero_2
        print(resultado)
        numero = 0
        numero_2 = 0

    elif oper.lower() == "resta":
        numero_2 = int(input("Ingresa el otro número: "))
        resultado = numero - numero_2
        print(resultado)
        numero = 0
        numero_2 = 0

    elif oper.lower() == "multi":
        numero_2 = int(input("Ingresa el otro número: "))
        resultado = numero * numero_2
        print(resultado)
        numero = 0
        numero_2 = 0

    elif oper.lower() == "div":
        numero_2 = int(input("Ingresa el otro número: "))
        resultado = numero / numero_2
        print(resultado)
        numero = 0
        numero_2 = 0

    else:
        if oper.lower() == "salir":
            print("Nos vemos ")
        else:
            print("Opción invalida")
