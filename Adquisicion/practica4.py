# =============================================================================
# Práctica 4. Kobe Stats.
# =============================================================================

import json

def load_json(path):
    """
    Loads JSON file in given path into a dictionary that will
    be returned.
    Params
    -------
    path : str
    The path to the target JSON file.
    Return
    -------
    d : dic
    The dictionary with the JSON content loaded.
    """
    with open(path, "r") as input_file:
        d = json.load(input_file)
    return d

# Cargamos el json que hemos obtenido con Postman, para trabajar con la información
# obtenida desde python.

d = load_json("./kobe.json")
#print(d)
datos = d["resultSets"][0]
#print(datos)

columnas = ["headers", "rowSet"]
datos_kobe = {key:value for key, value in datos.items() if key in columnas}
#print(type(datos_kobe))
#print(datos_kobe)


# Vamos a crear una lista con las cabeceras de los valores que nos va a interesar
# tener en una lista más reducida, con dicho valor para cada temporada.

headers =["AÑO DE LA TEMPORADA", "EDAD DEL JUGADOR", "PARTIDOS DISPUTADOS", "MEDIA DE PUNTOS ANOTADOS", "MEDIA DE ASISTENCIAS REPARTIDAS", "MEDIA DE REBOTES RECOGIDOS"]
#print(headers)


def cargar_resultados(datos, cabecera):
    """
    
    Introducir los valores de cada temporada del jugador elegido, 
    temporada a temporada,en una lista que se devolverá con los 
    valores más importantes.
    
    Params
    -------
    datos: diccionario 
        diccionario con los valores obtenidos de la pagina de 
        la NBA del jugador elegido.
    
    cabecera : lista
        lista con las cabeceras de los valores que interesan.
    
    Return
    -------
    reultados : lista
        Lista final añadiendo a la inicial los valores de cada temporada 
        regular jugada por el jugador elegido.
   
    """
    
    resultados = []
    resultados.append(cabecera)
    
    for year in datos["rowSet"]:
        temporada = []        
        temporada.append(year[1])
        temporada.append(year[5])
        temporada.append(year[6])
        temporada.append(year[26])
        temporada.append(year[21])
        temporada.append(year[20])
        resultados.append(temporada)
        #print(temporada)
        
    #print(resultados)
    return(resultados)
    
# Una vez se ha definido la función con la que se va a poder obtener una lista 
# con las estadísticas más relevantes de la carreara de cualquier jugador, vamos 
# a obtener los valores para nuestros datos de Kobe.

regular_season_stats = cargar_resultados(datos_kobe, headers)
print(regular_season_stats)

temporadas = regular_season_stats[1:]
#print(temporadas)


# Bucle para buscar de entre todas las temporadas en cual se han anotado más puntos totales
# (puntos por partido * partidos jugados)
for year in temporadas:
    valor = 0
    if year == 0:
        valor = year[3]*year[2]
        resultado = year[0]
    elif year[3]*year[2] >= valor:
        valor = year[3]*year[2]
        resultado = year[0]
season_max_points = resultado
puntos_max = valor
print("La temporada con mayor número de puntos anotados fue la", season_max_points, "con" , round(puntos_max, 2))
# El resultado obtenido es 1161.6

# Bucle identico, pero para buscar la temporada con menor cantidad de puntos totales
for year in temporadas:
    if year == 0:
        valor = year[3]*year[2]
        resultado = year[0]
    elif year[3]*year[2] <= valor:
        valor = year[3]*year[2]
        resultado = year[0]
season_min_points = resultado
puntos_min = round(valor, 2)
print("La temporada con menor número de puntos anotados fue la", season_min_points, "con", puntos_min)
# El resultado obtenido es 82.8

def avg_career(datos, estadistica):
    """
    
    Parameters
    ----------
    datos : lista
        Lista con los valores las estadisticas personales de cada temporada 
        para el jugador elegido.
        
    estadistica : int
        Valor del 1 al 3 donde:
            - 3 es el valor usado para obtener los puntos.
            - 4 es el valor usado para obtener las asistencias.
            - 5 es el valor usado para obtener los rebotes.
            

    Returns
    -------
    resultado : float
        El valor devuelto es la media total, en la carrera del jugador, para la 
        estadistica que se indique.

    """
    partidos = 0
    stat = 0
    for year in datos:
        partidos += year[2]
        stat += year[2]*year[estadistica]
    
    resultado = stat / partidos
    return resultado


# Con la función anterior se va a poder calcular la media de puntos, rebotes y
# asistencias para cada cualquier jugador en su regular season.

avg_career_points = avg_career(temporadas, 3)
print("La media de puntos anotados en su carrera fue: ", round(avg_career_points, 2))
# El resultado obtenido es 24.99

avg_career_rebounds = avg_career(temporadas, 5)
print("La media de rebotes capturados en su carrera fue: ", round(avg_career_rebounds, 2))
# El resultado obtenido es 5.24

avg_career_assists = avg_career(temporadas, 4)
print("La media de asistencias dadas en su carrera fue: ", round(avg_career_assists, 2))
# El resultado obtenido es 4.69
    