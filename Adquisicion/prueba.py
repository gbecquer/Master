## Saber si un numero es par o impar

numero = int(input("Dame un numero crack: "))

def parimpar():

    resultado = ""
    if numero % 2 == 0:
        resultado = str(numero) + " es par"
    else:
        resultado = str(numero) + " es impar"
    return resultado

print(parimpar())

print("Hola")