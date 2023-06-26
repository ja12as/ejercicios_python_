"""Escribir un programa que pida al usuario dos números enteros 
y muestre por pantalla la <n> entre <m> da un cociente <c> y un 
resto <r> donde <n> y <m> son los números introducidos por el usuario, 
y <c> y <r> son el cociente y el resto de la división entera respectivamente."""
dividendo = int(input("Ingrese el dividendo de la division: "))
divisor = int(input("Ingrese el divisor de la division; "))
resto = dividendo % divisor
cociente = dividendo // divisor
print("el cociente de la division es ",cociente, " y el resto es ",resto)