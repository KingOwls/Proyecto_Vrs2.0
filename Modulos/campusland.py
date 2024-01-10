import Modulos.corefile as db
import Modulos.menus as menu

campuslandDB = {
    "zones":{
        "artemis":{
            "nombre": "artemis",
            "morning": ["I1_1"]
        },
        "sputnik":{
            "nombre": "sputnik",
            "morning": ["m1_1"],
        },
        "apolo":{
            "nombre": "apolo",
            "morning": ["j1_1"],
        }
    },

    "rutas": {
        "nodejs":{
            "NameRt": "nodejs",
            "zone": "sputnik",
            "FchInc": "03-12-2024",
            "FchFnl": "30-04-2025",
            "trainers": ["miguel"],
            "grupos":["m1_1"],
            "jornada": "morning",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML"],
            "programacionFormal": ["JavaScript", "C#"],
            "basesDatos": ["MongoDB", "MySql"],
            "backend": ["NodeJS", "Express"]
        },
        "java":{
            "NameRt": "java",
            "zone": "apolo",
            "FchInc": "03-12-2024",
            "FchFnl": "30-04-2025",
            "trainers": ["johlver"],
            "grupos": ["j1_1"],
            "jornada": "morning",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["HTML"],
            "programacionFormal": ["Java"],
            "basesDatos": ["Postgresql", "MySql"],
            "backend": ["Spring Boot", "Express"]
        },
        "netcore":{
            "NameRt": "netcore",
            "zone": "apolo",
            "FchInc": "03-12-2024",
            "FchFnl": "30-04-2025",
            "trainers": ["Ingeniero"],
            "grupos": ["I1_1"],
            "jornada": "morning",
            "fundamentosProgramacion": ["Introducción a la algoritmia", "PSeInt"],
            "programacionWEB": ["CSS"],
            "programacionFormal": ["C#"],
            "basesDatos": ["Postgresql", "MySql"],
            "backend": ["NetCore", "POO"]
        }
    },

    "trainers":{
        "Ingeniero":{
            "uid": "1",
            "nombre": "Ingeniero",
            "jornada": "morning",
            "grupos": ["I1_1"]
        },
        "johlver":{
            "uid": "1",
            "nombre": "johlver",
            "jornada": "morning",
            "grupos": ["j1_1"]
        },
        "miguel":{
            "uid": "2",
            "nombre": "miguel",
            "jornada": "morning",
            "grupos": ["m1_1"]
        }
    },

    "grupos": {
        "j1_1": [],
        "I1_1": [],
        "m1_1": []
    }

}



def newzone():
    loadCampuslanDB()
    menu.showHeader("zones")
    zones = campuslandDB.get("zones")
    menu.printList(list(zones.keys()))
    opcion = input("\nEstas Seguro que Desea Crear Nueva Area de Entrenamiento? ")
    if opcion.lower():
        print("Por el Momento Campus Solo Cuenta con 3 Areas Asignalas en el Menu de Administrar Rutas")
    return

def newRuta():
    loadCampuslanDB()
    menu.showHeader("rutas1")
    rutas = campuslandDB.get("rutas")
    menu.printList(list(rutas.keys()))
    while(True):
        opcion = input(menu.showMenu("rutaMenu"))
        if(opcion == "1"):
            ruta = {}
            rutaName = input("str", "Nombre de La Ruta Nueva").replace(" ", "")
            if not (rutaName in rutas):
                ruta.update({"NameRt":rutaName})

                print("Fecha de Inicio de La ruta")
                ruta.update({"FchInc": menu.newDate()})
                print("Fecha de Finalizacion de la Ruta")
                ruta.update({"FchFnl": menu.newDate()})

                jornada = selectJornada()
                ruta.update({"jornada": jornada})

            else:
                print("Esa Ruta Ya Existe Intenta con Otro Nombre")
        elif(opcion == "2"):
            print("Opcion No Disponible por el momento")
        elif(opcion == "3"):
            return
        else:
            print("Error Opcion No Reconocida")



def selectzone(jornada, grupo):
    while(True):
        zones = campuslandDB.get("zones")
        menu.showHeader("zones")
        menu.printList(list(zones.keys()))
        opcion = input("str", "Ingresa el Nombre del Area")
        if opcion in zones:
            zone = zones.get(opcion)
            if (len(zone[jornada]) < 2):
                zone[jornada].append(grupo)
                return zone["nombre"]
            else:
                print("Esta Area No Cuenta Con Espacio Disponible Intentalo Con Otra o en Jornada Contraria")
        else:
            print(f"El Area {opcion} No Existe Intentalo de Nuevo")

def selectJornada():
    while(True):
        opcion = input("En este momento hay 1) mañana, 2) tarde")
        if opcion == "1":
            return "morning"
        else:
            print("Opcion de la tarde Todavia no disponible")
        

def selectTematics():
    thematic = {
        "fundamentosProgramacion": [],
        "programacionWEB": [],
        "programacionFormal": [],
        "basesDatos": [],
        "backend": []
    }
    print("Ingresa el Nombre de Los Temas A Tratar en Fundamentos de Programacion")
    print("Temas Recomendados: (Introducción a la algoritmia, PSeInt y Python)")
    thematic["fundamentosProgramacion"].append(  input("str", "Ingresa el Tema Principal"))


    print("Ingresa el Nombre de Los Temas A Tratar en Programación Web")
    print("Temas Recomendados: (HTML, CSS y Bootstrap)")
    thematic["programacionWEB"].append(  input("str", "Ingresa el Tema Principal"))

    print("Ingresa el Nombre de Los Temas A Tratar en Programación formal")
    print("Temas Recomendados: (Java, JavaScript, C#)")
    thematic["programacionFormal"].append(  input("str", "Ingresa el Tema Principal"))

    print("Ingresa el Nombre de Los Temas A Tratar en Bases de datos")
    print("Temas Recomendados: (Mysql, MongoDb y Postgresql)")
    thematic["basesDatos"].append(  input("str", "Ingresa el Tema Principal"))


    print("Ingresa el Nombre de Los Temas A Tratar en Backend ")
    print("Temas Recomendados: (NetCore, Spring Boot, NodeJS y Express)")
    thematic["backend"].append(  input("str", "Ingresa el Tema Principal"))
    return thematic

DataBaseCampus = "campusland.json"

def loadCampuslanDB():
    db.DataBaseCampus = DataBaseCampus
    campuslandDB.update(db.checkFile(**campuslandDB))






