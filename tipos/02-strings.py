nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Pyton, 
este curso contenpla todos los contenidos
que necesitas aprender para conseguir
trabajo
"""
print(nombre_curso, descripcion_curso)
print(len(nombre_curso))  # permite conocer la longitud de un string
print(nombre_curso[0])  # indice cero
# indice de inicio : cuantos caracteres quiero recortar
# indice comienza en el 0 y termina en el 8 (en los indices)
print(nombre_curso[0:8])
print(nombre_curso[9:])  # Indice nueve hasta donde termine
print(nombre_curso[:8])  # el valor por defecto será cero
print(nombre_curso[:])  # asume valor izquierda y asume valor derecha
