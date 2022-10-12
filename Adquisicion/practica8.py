# ==============================================================================
# Práctica 8. Extraer los datos de la tabla de población estimada por continente
# ==============================================================================

import requests
from bs4 import BeautifulSoup
import json

# Vamos a replicar los pasos que hemos visto para la práctica 7.

# En primer lugar vamos a descargarnos el HTML de la página con requests.

url = "https://en.wikipedia.org/wiki/World_population"
response = requests.get(url)
#print(response)


# Ahora vamos a parsear el HTML que acabamos de descargar con bs4.

soup = BeautifulSoup(response.content, "html.parser")


# Por otro lado en la página de la Wikipedia que estamos usando, vamos a analizar 
# el código HTML hasta encontrar el elemento que buscamos(la tabla de la poblacion).

target_tables = soup.find_all("table", class_="wikitable sortable")
#print(len(target_tables))
target_table = target_tables[0]
#print(target_table.get_text())


# Nos vamos a centrar primero en las cabeceras, para ello vamos a seleccionar unicamente
# el primer tr que encontremos.

headers = target_table.find("tr")
#print(headers)

cabecera = []
for th in headers.find_all("th"):
    cabecera.append(th.get_text().strip())
#print(cabecera)
  
  
# Una vez que ya hemos conseguido recopilar la información de las cabeceras, 
# vamos a proceder a realizar lo mismo con la informacion de cada continente.

# Se omite el primer tr, ya que es el que tiene la información de la cabecera.

continents = target_table.find_all("tr")
del continents[0]
#print(continents)

# A continuación, se va a crear un diccionario con el valor de la cabecera como clave
# y el valor que extraemos de cada td, para cada continente, como valor.

tabla= {}

for tr in continents: 
    for td, th in zip(tr.find_all("td"), cabecera):       
        tabla[th] = td.get_text().strip()
    diccionario = json.dumps(tabla, ensure_ascii=False)   
    print(diccionario)

# El resultado que se muestra es, el json creado a partir del diccionario guardado 
# en la variable tabla, con toda la información obtenida.