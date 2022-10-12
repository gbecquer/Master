import requests
import time
from selenium import webdriver
from os import makedirs
from os.path import exists

driver = webdriver.Chrome( 
    executable_path = "./chromedriver.exe"
)
url ='https://www.boe.es/diario_borme/'
driver.get(url)

import sys

year = sys.argv[1]
month = sys.argv[2]
day = sys.argv[3]
seccion = sys.argv[4]

def seleccionarDia(year, month, day, seccion):
    salida = []
    calendario = driver.find_element_by_id("fechaBORME")
    calendario.send_keys(day, month, year)
    time.sleep(1)
    buscar = driver.find_element_by_class_name("boton")
    buscar.click() 
    time.sleep(1)
    if seccion == "primera":  
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
        
        
        
    if seccion == "segunda":
        secciones = driver.find_element_by_class_name("dropdown")
        secciones.click() 
        seccion2 = driver.find_element_by_xpath('//*[@id="filtros"]/div/ul/li[3]/a')
        seccion2.click()
        listas = driver.find_elements_by_class_name("dispo")
        for i in listas:
            referencia = i.find_element_by_tag_name("p").text 
            a = i.find_elements_by_tag_name("a")
            urlPDF = a[0].get_attribute("href") 
            urlXML = a[1].get_attribute("href") 
            salida.append([referencia, urlPDF, urlXML])
    return salida


contenidos = seleccionarDia(year,month, day, seccion) 
print(contenidos)

if seccion == "primera":
    if not exists("/PrimeraSeccion/"+year+'-'+month+'-'+day):
        makedirs("PrimeraSeccion/"+year+'-'+month+'-'+day)
        time.sleep(2)
        for i in contenidos:
            print(i)
            print(i[0])
            print(i[1])
            r = requests.get(i[1])
            with open("PrimeraSeccion/"+year+'-'+month+'-'+day+'/' + i[0] + ".pdf", "wb") as f:
                f.write(r.content)
if seccion == "segunda":
    if not exists("/SegundaSeccion/"+year+'-'+month+'-'+day):
        makedirs("SegundaSeccion/"+year+'-'+month+'-'+day+"/PDF/")
        makedirs("SegundaSeccion/"+year+'-'+month+'-'+day+"/XML")
        time.sleep(2)
        for i in contenidos:
            print(i)
            print(i[0])
            print(i[1])
            print(i[2])
            r = requests.get(i[1])
            with open("SegundaSeccion/"+year+'-'+month+'-'+day+"/PDF/" + i[0] + ".pdf", "wb") as f:
                f.write(r.content)
            r = requests.get(i[2])
            with open("SegundaSeccion/"+year+'-'+month+'-'+day+"/XML/" + i[0], "wb") as f:
                f.write(r.content)

