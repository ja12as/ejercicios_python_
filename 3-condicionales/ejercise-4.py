"""Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es par o impar."""

from datetime import date
hoy = date.today()
print("Hoy es: ", hoy)
print()
numero= int(input("Ingresa uun numero par averificar si es par o impar: "))

if numero % 2 == 0:
    print("es par")
else:
    print("es impar")