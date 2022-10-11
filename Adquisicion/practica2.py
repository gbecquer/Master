# =============================================================================
# Práctica 2. API AEMET.
# =============================================================================

# 1. Llamar al endpoint del inventario de estaciones.

import requests

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones"

# La api_key de AEMET la he sustituido para no mostrarla, pero iré mostrando los distintos 
# resultados obtenidos en cada paso.

query_string = {"api_key":"{aemet_api_key}"}

response = requests.get(url, params = query_string)

print(response)
print(response.text)
print(response.headers)


# 2. Buscar entre los resultados la estación llamada "MADRID, CIUDAD UNIVERSITARIA". 

# El resultado obtenido con el anterior get realizado con requests es el mismo 
# que obtenemos con postman, el siguiente:

respuesta_postman = {
    "descripcion": "exito",
    "estado": 200,
    "datos": "https://opendata.aemet.es/opendata/sh/dfadbc77",
    "metadatos": "https://opendata.aemet.es/opendata/sh/0556af7a"
}

# En el siguiente enlace obtenido podemos encontrar todas las estaciones y en 
# particular nos centramos en la de Ciudad Universitaria.

datos_ciu = {
  "latitud" : "402706N",
  "provincia" : "MADRID",
  "altitud" : "664",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "indsinop" : "08220",
  "longitud" : "034327W"
}

# De estos datos el que nos va a servir para realizar el siguiente apartado es
# el indicativo de la estación.


# 3. Llamar al endpoint de las climatologías diarias 

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2019-10-01T00%3A00%3A00UTC/fechafin/2019-10-30T23%3A59%3A59UTC/estacion/3194U"

query_string = {"api_key":"{aemet_api_key}"}

response = requests.get(url, params = query_string)

print(response)
print(response.text)

# Se adjunta a continuación el contenido de la respuesta obtenida

resultado = [ {
  "fecha" : "2019-10-01",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "19,0",
  "prec" : "0,0",
  "tmin" : "10,0",
  "horatmin" : "06:00",
  "tmax" : "28,1",
  "horatmax" : "14:20"
}, {
  "fecha" : "2019-10-02",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "18,0",
  "prec" : "0,0",
  "tmin" : "11,5",
  "horatmin" : "06:50",
  "tmax" : "24,5",
  "horatmax" : "14:30"
}, {
  "fecha" : "2019-10-03",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "16,9",
  "prec" : "0,0",
  "tmin" : "7,9",
  "horatmin" : "06:40",
  "tmax" : "25,9",
  "horatmax" : "15:20"
}, {
  "fecha" : "2019-10-04",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "18,8",
  "prec" : "0,0",
  "tmin" : "8,8",
  "horatmin" : "06:00",
  "tmax" : "28,8",
  "horatmax" : "15:40"
}, {
  "fecha" : "2019-10-05",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "18,7",
  "prec" : "0,0",
  "tmin" : "10,0",
  "horatmin" : "06:00",
  "tmax" : "27,4",
  "horatmax" : "16:10"
}, {
  "fecha" : "2019-10-06",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "19,1",
  "prec" : "0,0",
  "tmin" : "9,5",
  "horatmin" : "06:40",
  "tmax" : "28,7",
  "horatmax" : "15:10"
}, {
  "fecha" : "2019-10-07",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "19,8",
  "prec" : "0,0",
  "tmin" : "11,0",
  "horatmin" : "06:40",
  "tmax" : "28,7",
  "horatmax" : "15:50"
}, {
  "fecha" : "2019-10-08",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "20,6",
  "prec" : "0,0",
  "tmin" : "11,4",
  "horatmin" : "05:30",
  "tmax" : "29,8",
  "horatmax" : "16:00"
}, {
  "fecha" : "2019-10-09",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "20,8",
  "prec" : "0,0",
  "tmin" : "12,5",
  "horatmin" : "06:30",
  "tmax" : "29,1",
  "horatmax" : "15:20"
}, {
  "fecha" : "2019-10-10",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "20,4",
  "prec" : "0,0",
  "tmin" : "14,3",
  "horatmin" : "05:20",
  "tmax" : "26,6",
  "horatmax" : "15:40"
}, {
  "fecha" : "2019-10-11",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "19,8",
  "prec" : "0,0",
  "tmin" : "12,6",
  "horatmin" : "06:40",
  "tmax" : "27,0",
  "horatmax" : "15:40"
}, {
  "fecha" : "2019-10-12",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "20,7",
  "prec" : "6,0",
  "tmin" : "15,3",
  "horatmin" : "06:40",
  "tmax" : "26,1",
  "horatmax" : "Varias"
}, {
  "fecha" : "2019-10-13",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "18,7",
  "prec" : "0,0",
  "tmin" : "12,6",
  "horatmin" : "06:50",
  "tmax" : "24,8",
  "horatmax" : "15:50"
}, {
  "fecha" : "2019-10-14",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "13,6",
  "prec" : "2,1",
  "tmin" : "7,1",
  "horatmin" : "23:59",
  "tmax" : "20,2",
  "horatmax" : "13:40"
}, {
  "fecha" : "2019-10-15",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "11,8",
  "prec" : "0,0",
  "tmin" : "5,9",
  "horatmin" : "06:40",
  "tmax" : "17,7",
  "horatmax" : "15:00"
}, {
  "fecha" : "2019-10-16",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "12,7",
  "prec" : "1,3",
  "tmin" : "5,7",
  "horatmin" : "07:00",
  "tmax" : "19,7",
  "horatmax" : "15:20"
}, {
  "fecha" : "2019-10-17",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "11,6",
  "prec" : "1,7",
  "tmin" : "7,5",
  "horatmin" : "04:00",
  "tmax" : "15,7",
  "horatmax" : "17:00"
}, {
  "fecha" : "2019-10-18",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "16,6",
  "prec" : "0,1",
  "tmin" : "12,9",
  "horatmin" : "23:59",
  "tmax" : "20,2",
  "horatmax" : "13:10"
}, {
  "fecha" : "2019-10-19",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "14,3",
  "prec" : "15,0",
  "tmin" : "10,7",
  "horatmin" : "07:00",
  "tmax" : "17,9",
  "horatmax" : "12:40"
}, {
  "fecha" : "2019-10-20",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "9,2",
  "prec" : "0,2",
  "tmin" : "5,2",
  "horatmin" : "23:59",
  "tmax" : "13,2",
  "horatmax" : "13:20"
}, {
  "fecha" : "2019-10-21",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "8,8",
  "prec" : "0,0",
  "tmin" : "2,1",
  "horatmin" : "06:40",
  "tmax" : "15,6",
  "horatmax" : "15:00"
}, {
  "fecha" : "2019-10-22",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "8,9",
  "prec" : "9,5",
  "tmin" : "6,5",
  "horatmin" : "00:10",
  "tmax" : "11,3",
  "horatmax" : "11:00"
}, {
  "fecha" : "2019-10-23",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "8,4",
  "prec" : "1,0",
  "tmin" : "6,8",
  "horatmin" : "06:00",
  "tmax" : "10,0",
  "horatmax" : "16:00"
}, {
  "fecha" : "2019-10-24",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "11,8",
  "prec" : "0,0",
  "tmin" : "5,5",
  "horatmin" : "07:10",
  "tmax" : "18,2",
  "horatmax" : "16:00"
}, {
  "fecha" : "2019-10-25",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "13,6",
  "prec" : "0,0",
  "tmin" : "6,1",
  "horatmin" : "07:00",
  "tmax" : "21,1",
  "horatmax" : "15:40"
}, {
  "fecha" : "2019-10-26",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "14,2",
  "prec" : "0,0",
  "tmin" : "5,3",
  "horatmin" : "06:40",
  "tmax" : "23,1",
  "horatmax" : "15:40"
}, {
  "fecha" : "2019-10-27",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "14,0",
  "prec" : "0,0",
  "tmin" : "6,2",
  "horatmin" : "07:00",
  "tmax" : "21,9",
  "horatmax" : "13:40"
}, {
  "fecha" : "2019-10-28",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "16,4",
  "prec" : "0,0",
  "tmin" : "10,8",
  "horatmin" : "05:00",
  "tmax" : "22,0",
  "horatmax" : "15:00"
}, {
  "fecha" : "2019-10-29",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "14,1",
  "prec" : "0,0",
  "tmin" : "8,4",
  "horatmin" : "05:30",
  "tmax" : "19,8",
  "horatmax" : "14:40"
}, {
  "fecha" : "2019-10-30",
  "indicativo" : "3194U",
  "nombre" : "MADRID, CIUDAD UNIVERSITARIA",
  "provincia" : "MADRID",
  "altitud" : "664",
  "tmed" : "13,7",
  "prec" : "0,0",
  "tmin" : "9,0",
  "horatmin" : "07:00",
  "tmax" : "18,4",
  "horatmax" : "13:40"
} ]