"""Para tributar un determinado impuesto se debe ser mayor de 16
años y tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos
mensuales y muestre por pantalla si el usuario tiene que tributar o no."""
from datetime import date
hoy = date.today()
print(" hoy es ", hoy)


edad =  int(input("Ingresa tu edad: "))
salario= int(input("Ingresa tu salario mensual: "))
if edad >= 16 and salario >= 1000:
    print("tiene que tributar")
else:
    print("¡NO! tiene que tributar")