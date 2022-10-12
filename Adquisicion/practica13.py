# =============================================================================
# Práctica 13. BORME. Usar selenium y chromedriver 
# =============================================================================

import requests
import time
from selenium import webdriver
from os import makedirs
from os.path import exists


# El exe del chromedriver está en la misma carpeta que el script de python, con
# el siguiente comando se indica donde esta exactamente, para que pueda acceder
# a él sin problemas.

driver = webdriver.Chrome( 
    executable_path = "./chromedriver.exe"
)
url ='https://www.boe.es/diario_borme/'

driver.get(url)

# Las siguientes variables que se acaban de definir arriba van a ser las que
# van a marcar en que fecha se va a buscar el boletin del BORME.

year = "2020"
month = "12"
day = "01"
seccion = "segunda"


# A parte se puede definir una función que, como indica en el enunciado de la 
# práctica, pueda obtener directamente estos valores con una fecha cualquiera 
# aportada por el usuario

def obtener_fecha(fecha):
    """
    A partir de una fecha en formato YYYYMMDD, se van a obtener por separado 
    los valores del año, mes y día.
    
    Params
    -------
    fecha : str
        La fecha que introduce el usuario, de la cual quiere obtener los 
        boletines del BORME, en formato YYYYMMDD.
    Returns
    --------
    year : str
        año(YYYY)
    month : str
        mes(MM)
    day : str
        día(DD)
    """
    
    year = fecha[0:4]
    month = fecha[4:6]
    day = fecha[6:8]
    
    return year,month,day


# Función para buscar los distintos elementos dada una fecha para el boletín,
# en función de la sección del BORME a la que pertenezcan.

def seleccionar_dia(year, month, day, seccion):
    salida = []
    calendario = driver.find_element_by_id("fechaBORME")
    calendario.send_keys(day, month, year)
    time.sleep(1)
    buscar = driver.find_element_by_class_name("boton")
    buscar.click() 
    time.sleep(1)
    if seccion == "primera": 
        #navego hasta seccion primera: 
        secciones = driver.find_element_by_class_name("dropdown")
        secciones.click() 
        seccion1 = driver.find_element_by_xpath('//*[@id="filtros"]/div/ul/li[2]/a')
        seccion1.click()
        listas = driver.find_elements_by_class_name("dispo")
        for i in listas:
            ciudad = i.find_element_by_tag_name("p").text
            a = i.find_elements_by_tag_name("a")
            url = a[0].get_attribute("href") 
            salida.append([ciudad, url])
        #print(salida)
        
        
    if seccion == "segunda":
        #navego hasta seccion segunda:
        secciones = driver.find_element_by_class_name("dropdown")
        secciones.click() 
        seccion2 = driver.find_element_by_xpath('//*[@id="filtros"]/div/ul/li[3]/a')
        seccion2.click()
        listas = driver.find_elements_by_class_name("dispo")
        for i in listas:
            referencia = i.find_element_by_tag_name("p").text #sacamos la p.
            a = i.find_elements_by_tag_name("a")
            urlPDF = a[0].get_attribute("href") #url de los pdfs
            urlXML = a[1].get_attribute("href") #url de los xml
            salida.append([referencia, urlPDF, urlXML])
        #print(salida)
    return salida


# Con los datos de entrada predefinidos para este caso, vamos a crear la variable 
# contenidos, a partir de la cual va a buscar en la página todo el contenido 
# disponible. Además, dependiendo de si se trata de la primera o segunda sección,
# vamos a crear una nueva carpeta en la que cargar todo el contenido que se 
# encuentre para nuestro caso.
 
contenidos = seleccionar_dia(year,month, day, seccion) 
print(contenidos)

if seccion == "primera":
    if not exists("/seccionPrimera"):
        makedirs("seccionPrimera")
        time.sleep(1)
        for i in contenidos:
            #print(i)
            r = requests.get(i[1])
            with open("seccionPrimera/"+ i[0] +".pdf", "wb") as f:
                f.write(r.content)   
if seccion == "segunda":
    if not exists("/seccionSegunda"):
        makedirs("seccionSegunda/PDF/")
        makedirs("seccionSegunda/XML")
        time.sleep(1)
        for i in contenidos:
            print(i)
            print(i[0])
            print(i[1])
            print(i[2]) 
            r = requests.get(i[1])
            with open("seccionSegunda/PDF/"+ i[0] +".pdf", "wb") as f:
                f.write(r.content) 
            r = requests.get(i[2])
            with open("seccionSegunda/XML/"+ i[0], "wb") as f:
                f.write(r.content)  

driver.close()

# En la carpeta en la que se ha guardado el script de la práctica y el exe de 
# chromedriver ahora se va a poder ver también la carpeta que ha aparecido con
# los archivos tanto en pdf como en xml de los boletines del BORME, para la fecha
# del 01/12/2020.
