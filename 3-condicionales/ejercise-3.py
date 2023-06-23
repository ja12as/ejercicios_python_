"""Escribir un programa que pida al usuario dos números 
y muestre por pantalla su división. Si el divisor es cero
el programa debe mostrar un error."""

from datetime import date
hoy = date.today()
print(" hoy es: ", hoy)
print()
dividendo = int(input("ingresa el primer numero: "))
divisor = int(input("ingresa el segundo numero: "))

if divisor == 0:
    print("no se pude dividir por  cero")
else:
    print("El resultado de la division es: ",str(dividendo // divisor))
    