# vamos a importar un modulo para matematicas
import math
# devuelve el número al cual se encuentre más cercano
# ¿1.3 se encuentra más cerca del 1 que del 2 ? pues si, del 1
print(round(1.3))
print(round(1.8))
print(round(1.5))
# entrega valor abosluto que yo le pase
numero = -1345
print(abs(numero))
# Vamos a ver algunas funciones del modulo math
# toma el número y lo lleva al entero superior más cercano
print(math.ceil(1.1)) # Sube el número decial al antero más cercano.

print(math.floor(1.999999)) #baja el número decimal al antero más cercano

print(math.isnan(numero)) # verifica si el valor que le estoy pasando a la función es un entero

print(math.pow(10, 3)) #el número 10 elevado al cubo
print(math.sqrt(2)) #Raíz cuadrada de un número 
