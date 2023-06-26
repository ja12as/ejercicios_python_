"""Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
primeros enteros positivos puede ser calculada de la siguiente forma:
   suma= n(n+1)/2"""

numero= int(input("Ingrese un numero: "))
print("la suma de los numeros de1 al ", numero, " es: ",str(round(numero*(numero+1)/2)))