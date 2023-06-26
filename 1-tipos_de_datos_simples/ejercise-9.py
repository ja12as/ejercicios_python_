"""Escribir un programa que pregunte al usuario una cantidad 
a invertir, el interés anual y el número de años, y muestre 
por pantalla el capital obtenido en la inversión."""
cantidad_invertir=int(input("Ingrese la cantidad a invertir: "))
interes_anual = int(input("Ingrese el interes anual: "))
anos_inversion = int(input("Ingrese los años de la inversion: "))

print("Capital final: " + str(round(cantidad_invertir * (interes_anual / 100 + 1) ** anos_inversion, 2)))