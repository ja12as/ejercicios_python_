"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""

edad= int(input("Ingresa tu edad: "))
if edad <18:
    print("Eres Menor de edad")
elif edad >= 18:
    print("Eres Mayor de edad")