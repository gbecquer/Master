import requests

from bs4 import BeautifulSoup


# =============================================================================
#  Práctica 7a. Encontrar elementos HTML con BS4
# =============================================================================

url = "https://en.wikipedia.org/wiki/Comillas_Pontifical_University"
response = requests.get(url)

#print(response)

# Loads HTML into soup.
soup = BeautifulSoup(response.content, "html.parser")

# Locates target table with usefull info.
target_tables = soup.find_all("table", class_="infobox vcard")

#print(len(target_tables))
target_table = target_tables[0]
#print(target_table.get_text())


# =============================================================================
#  Práctica 7b. Extraer datos útiles de los elementos de HTML
# =============================================================================


# Para esta parte hay que inspeccionar el código de HTML de la tabla que hemos 
# obtenido en el apartado anterior. El esquema de los distintos elementos que se
# pueden ver es el siguiente:
# Todos los elementos empiezan con un tr.
# Luego observamos dos patrones distintos. Los que ya tienen un título y una descripción,
# que tienen un th para el título y td para la descripción. Estos se podrán extraer de 
# forma sencilla con un zip y guardar en un diccionario como parejas clave-valor.
# Por otro lado tenemos otros elementos que solo tienen td, son aquellos que solo 
# tienen una parte de texto o las imagenes.

# Los elementos que nos van a dar problemas son la primera imagen, el motto de latin
# que no tiene título, aparece todo el texto en td y la última imágen que tampoco tiene 
# título


# Para eliminar 130 year ago en Established
for span in soup.find('span'):
    span.replace_with('')
    
# Para eliminar [1] en Students
for sup in soup.find('sup'): 
    sup.replace_with('')


# Comienzo buscando todos los elementos tr que es donde esta toda la información
# de la tabla que nos interesa

item_comillas = target_table.find_all("tr")
#print(len(item_comillas))

# Voy a utilizar la variable tabla, que será un diccionario donde iré guardando 
# toda la información obtenida de la tabla de la Wikipedia.

tabla = {}

# Los dos primeros elementos que nos vamos a encontrar los vamos a tratar por separado,
# ya que el primero es una imagen y el segundo viene con el titulo dentro de td
# y habrá que adjudicarle uno (Motto in Latin)

tabla[item_comillas[1].find("div").get_text()] = item_comillas[1].find("a")['href']

tabla["Motto in Latin:"] = item_comillas[2].find("i").get_text()

# Para todos los elementos con th y td.

for tr in item_comillas: 
    for th, td in zip(tr.find_all("th"), tr.find_all("td")): 
                tabla[th.get_text()] = td.get_text().strip()


# Por último, la imagen del final, la introduciré dando la clave "logo" como se
# especifica en las diapositivas y utilizando href para coger direccion de la imagen.

tabla["logo"] = item_comillas[16].find("a")['href']

print(tabla)


# =============================================================================
#  Práctica 7c. Extraer datos útiles de los elementos de HTML
# =============================================================================

# En esta última parte, el objetivo es guardar los datos extraidos con bs4
# en un json.

import json

diccionario = json.dumps(tabla, ensure_ascii=False)   
print(diccionario)

