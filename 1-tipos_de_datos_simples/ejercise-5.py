"""Escribir un programa que pregunte al usuario por el número
de horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde."""

hora_trabajad= int(input("ingresa las horas trabajadas: "))
coste_hora= int(input("ingresa el valor por hora: "))
print("La paga que le corresponde es de ",str(hora_trabajad * coste_hora))