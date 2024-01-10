import os
import random

def uuid():
    return random.randint(0000, 9999)

def printList(arrayText:list):
    for data in arrayText:
        print(data.upper())
    print("")
    os.system("pause")


def newDate():
    while True:
        day = input("int", "Ingresa el Dia")
        if (day > 0) and (day <= 31):
            break
        else:
            print("Ingresa un Dia Valido")
    
    while True:
        month = input("int", "Ingresa el Mes")
        if (month > 0) and (month <= 12):
            break
        else:
            print("Ingresa un Mes Valido")

    while True:
        year = input("int", "Ingresa el Año")
        if (year > 2000) and (year < 3000):
            break
        else:
            print("Ingresa un Año Ventana de Tiempo para este Campo es de (1900)-(3000)")

    return f"{day}-{month}-{year}"