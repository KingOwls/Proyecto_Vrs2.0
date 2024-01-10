import Modulos.corefile as db
import templates.reusable as reusable
import templates.menus as mn

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
    mn.showHeader("zones")
    zones = campuslandDB.get("zones")
    reusable.printList(list(zones.keys()))
    opcion = input("\nEstas Seguro que Desea Crear Nueva Area de Entrenamiento? ")
    if opcion.lower():
        print("Por el Momento Campus Solo Cuenta con 3 Areas Asignalas en el Menu de Administrar Rutas")
    return

def newRuta():
    loadCampuslanDB()
    mn.showHeader("rutas1")
    rutas = campuslandDB.get("rutas")
    reusable.printList(list(rutas.keys()))
    while(True):
        opcion = input(mn.showMenu("rutaMenu"))
        if(opcion == "1"):
            ruta = {}
            rutaName = input("str", "Nombre de La Ruta Nueva").replace(" ", "")
            if not (rutaName in rutas):
                ruta.update({"NameRt":rutaName})

                print("Fecha de Inicio de La ruta")
                ruta.update({"FchInc": reusable.newDate()})
                print("Fecha de Finalizacion de la Ruta")
                ruta.update({"FchFnl": reusable.newDate()})

                jornada = selectJornada()
                ruta.update({"jornada": jornada})
                
                data = selectTrainer(jornada)
                if data:
                    ruta.update({"trainer": data["trainer"]})

                    grupos = campuslandDB.get("grupos")
                    grupos.update({data["grupo"]:[]})

                    ruta.update({"zone":selectzone(jornada, data["grupo"])})

                    mn.showHeader("thematic")
                    ruta.update(selectTematics())
                    
                    rutas.update({rutaName:ruta})
                    db.newFile(**campuslandDB)
                    reusable.showSuccess("Nueva Ruta Creada Correctamente")
                else:
                    reusable.showInfo("Esta Ruta No se Pudo Crear Intentalo de Nuevo mas tarde")


            else:
                print("Esa Ruta Ya Existe Intenta con Otro Nombre")
        elif(opcion == "2"):
            print("Opcion No Disponible por el momento")
        elif(opcion == "3"):
            return
        else:
            print("Error Opcion No Reconocida")
    


def selectTrainer(jornada):
    trainers = campuslandDB.get("trainers")
    trainersList = list(trainers.keys())
    while True:
        mn.showHeader("trainers")
        reusable.printList(trainersList)
        nombre = print("str", "Ingresa el Nombre del Trainer")
        if nombre in trainersList:
            trainer = trainers.get(nombre)
            if trainer["jornada"] == jornada:
                grupos = trainer.get("grupos")
                if len(grupos) < 2: 
                    grupo = f"{trainer['nombre'][0]}{len(grupos)+1}_{trainer['uid']}"
                    grupos.append(grupo)
                    return {"trainer":trainer["nombre"], "grupo":grupo}
                else:
                    print(f"El Trainer {nombre} No Tiene Disponibilidad Para Mas Grupos")
            else:
                print(f"El Trainer {nombre} No Tiene Disponibilidad en esa jornada")
        else:
            print(f"El Trainer {nombre} No Existe Intentalo de nuevo")
        Eleccion = input("Desea Intentar con Otro Trainer")
        if not Eleccion.lower():
            return


def selectzone(jornada, grupo):
    while(True):
        zones = campuslandDB.get("zones")
        mn.showHeader("zones")
        reusable.printList(list(zones.keys()))
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
    thematic["fundamentosProgramacion"].append(  input("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Programación Web")
    print("Temas Recomendados: (HTML, CSS y Bootstrap)")
    thematic["programacionWEB"].append(  input("str", "Ingresa el Tema Principal"))
    thematic["programacionWEB"].append(  input("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Programación formal")
    print("Temas Recomendados: (Java, JavaScript, C#)")
    thematic["programacionFormal"].append(  input("str", "Ingresa el Tema Principal"))
    thematic["programacionFormal"].append(  input("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Bases de datos")
    print("Temas Recomendados: (Mysql, MongoDb y Postgresql)")
    thematic["basesDatos"].append(  input("str", "Ingresa el Tema Principal"))
    thematic["basesDatos"].append(  input("str", "Ingresa el Tema Secundario"))

    print("Ingresa el Nombre de Los Temas A Tratar en Backend ")
    print("Temas Recomendados: (NetCore, Spring Boot, NodeJS y Express)")
    thematic["backend"].append(  input("str", "Ingresa el Tema Principal"))
    thematic["backend"].append(  input("str", "Ingresa el Tema Secundario"))

    return thematic


def newTrainer():
    loadCampuslanDB()
    trainers = campuslandDB.get("trainers")
    listTrainers = list(trainers.keys())
    mn.showHeader("trainer")
    uid = (len(listTrainers) + 1)
    data = checkTrainer(listTrainers)
    if data:
        trainer = {}
        trainer.update({"nombre": data["nombre"]})
        trainer.update({"uid":uid})
        while  True:
            print("Ingresa La Jornada del Trainer")
            print("1.Mañana")
            print("2.Tarde")
            opcion =   input("str", "")
            if (opcion == "1"):
                jornada = "morning"
                break
            elif(opcion == "2"):
                jornada = "afternoon"
                break
            else:
                print("Opcion No Valida")
        
        trainer.update({"jornada":jornada})
        trainer.update({"grupos":[]})
        trainers.update({data["key"]:trainer})
        db.newFile(**campuslandDB)
        print("El Trainer Se Registro Correctamente")
    else:
        print("Este Trainer Ya Existe")
        return

def checkTrainer(listTrainers:list):
    while True:
        nombre = input("str", "Ingresa el Nombre del Nuevo Trainer")
        nombres = nombre.split(" ")
        for name in nombres:
            if name:
                if not name in listTrainers:
                    return {"key":name, "nombre": nombre}
        
        return

DataBaseCampus = "campusland.json"

def loadCampuslanDB():
    db.DataBaseCampus = DataBaseCampus
    campuslandDB.update(db.checkFile(**campuslandDB))






