"""Escribe una funcion que pida por teclado la distancia y 
la velocidad de un móvimiento MRU y determina el tiempo de viaje"""

def calcular_tiempo_viaje():
    distancia = float(input("Introduce la distancia del viaje (en km): "))
    velocidad = float(input("Introduce la velocidad constante (en km/h): "))
    
    if velocidad <= 0:
        print("¡Error! La velocidad debe ser mayor que 0")
        return
    
    tiempo = distancia / velocidad
    print(f"El tiempo de viaje será: {tiempo:.2f} horas")