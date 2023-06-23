"""Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:

1 Generar un DataFrame con los datos de los cuatro ficheros.
2 Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
3 Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
4 Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
5 Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.
6 Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
7 Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
8 Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
9 Mostrar un resumen descriptivo para cada contaminante por distritos.
10 Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
11 Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
12 Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes."""