# and, or, not
# and, or, not
gas = True
encendido = False
edad = 18

if gas and encendido:
    print("Puedes avanzar")

if gas or encendido:
    print("Puedes seguir avanzando")

if gas or encendido:
    print("Hoy no avanzas")

if gas and (encendido or edad > 17):
    print("Tienes ", edad, " de edad")
# Operaciones de corto circuito

if not gas and encendido or edad > 17:
    print("Date chato")
