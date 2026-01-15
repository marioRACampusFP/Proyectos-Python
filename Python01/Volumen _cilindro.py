"""Escribe una funcion para calcular el volumen de un cilindro"""
import math

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

radio_u = float(input("Introduce el radio del cilindro: "))
altura_u = float(input("Introduce la altura del cilindro: "))

resultado = volumen_cilindro(radio_u, altura_u)
print("El volumen del cilindro es:", resultado)