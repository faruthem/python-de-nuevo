# numero = 1
# while numero < 100:  # Evalua si es verdadero o falso
#     print(numero)  # Si número es menor que 100 pasa
#     numero *= 2

comando = ""

# while comando.lower() != "salir":
#     comando = input("$Faruthem ")
#     print(comando)

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
