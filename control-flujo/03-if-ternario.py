from PIL import Image
edad = int(input("Ingrese su edad: "))

mensaje = "Es mayor" if edad > 17 else "Es menor"
""" if edad > 17:
    print("Efectivamente, es mayor")
    # Ruta de la imagen
    ruta_imagen = r"E:\noveno\python de nuevo\imagenes\mayorde.webp"
    # Abre la imagen
    imagen = Image.open(ruta_imagen)
    # Muestra la imagen
    imagen.show()
else:
    print("Efectivamente es menor")
    # Ruta de la imagen
    ruta_imagen = r"E:\noveno\python de nuevo\imagenes\bebecito.jpg"
    # Abre la imagen
    imagen = Image.open(ruta_imagen)
    # Muestra la imagen
    imagen.show() """

print(mensaje)
