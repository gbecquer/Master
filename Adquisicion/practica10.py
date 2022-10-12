import requests
import csv
from bs4 import BeautifulSoup
import os

os.chdir('C:\\Users\\Marino\\Documents\\UNIVERSIDAD\\Master BD\\Adquisición y Transformación de Datos\\Practica\\codigo')


def load_csv():
    with open('universities.csv' ,"r") as universities:
        lector = csv.reader(universities, delimiter=',')
        matrix = [row for row in lector]
    return matrix

matrix = load_csv()


prefijo = "https://en.wikipedia.org"
nombres = []
fechas = []

def grab_established_year(nombre, url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", attrs={"class": "infobox vcard"})
        body = table.find_all("tr")
        for tr in body:
            for th in tr.find_all("th"):
                if th.text == "Established":
                    td = tr.find("td")
                    fecha = td.text
                    print(nombre+" " +fecha)  
                    nombres.append(nombre)
                    fechas.append(fecha)
                    print(len(fechas))
                    
    except:
        print("except")
        pass
    finally:
        print("finally1")
        if len(fechas) == 87: 
            print("finally2")
            crearMatriz(nombres, fechas)
#%%
def crearMatriz(nombres, fechas):
    matrix = list(zip(nombres,fechas)) 
    with open("established.csv", "w", newline="") as established:
        writer = csv.writer(established, delimiter = ";")
        for row in matrix:
            writer.writerow(row)

#%%    



for linea in matrix:
    url = prefijo + linea[3] 
    grab_established_year(linea[2], url)



#%%
    
    
    
def grab_established_year(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        target_tables = soup.find("table", class_="infobox vcard")
        target_table = target_tables[0]
        
        for i in target_table.find_all("tr"):
            tr = i.get_text()
            if tr.startswith("Established"):
                established = tr.replace("Established","")
        
        return established

 

