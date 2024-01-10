import json
import os


PATH = "Proyecto_Vrs_2\data"
URL = ""

def newFile(**kwargs):
    with open(f"{PATH}{URL}", "w") as archivo:
        json.dump(kwargs, archivo, indent=4)


def loadData():
    with open(f"{PATH}{URL}", "r") as archivo:
        return json.load(archivo)
    
def checkFile(**kwargs):
    if(os.path.isfile(f"{PATH}{URL}")):
        kwargs.update(loadData())
    else:
        newFile(**kwargs)

    return kwargs

def updateDataBases():
    import Modulos.campers as Estudiantes
    import Modulos.campusland as campus
    with open(f"{PATH}{campus.URL}", "w") as archivo:
        json.dump(campus.campuslandDB, archivo, indent=4)
        archivo.close

    with open(f"{PATH}{Estudiantes.URL}", "w") as archivo:
        json.dump(Estudiantes.Estudiantes, archivo, indent=4)
        archivo.close