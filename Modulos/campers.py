import Modulos.corefile as db
import templates.menus as mn
import templates.reusable as reusable
import Modulos.campusland as campus

Estudiantes = {}

Estudiante = {
    "cc": "",
    "Name": "",
    "apellido": "",
    "ciudad": "",
    "direccion": "",
    "acudiente": ".",
    "telefono": {
        "celular": "",
        "fijo": ""
    },
    "estado": "inscrito",
    "notas":{
    }
    
}


status = ["aprobo", "no_aprobo", "estudiante", "entrevista", "contratado"]

def newEstudiante():
    BusquedaEstudiante()
    while True:
        print("registrar")
        cc = Verificacion()
        if cc:
            Estudiante["cc"] = cc
            Estudiante["Name"] = input("str", f"Ingresa el Nombre del Estudiante")
            Estudiante["apellido"] = input("str", f"Ingresa los Apellidos del Estudiante")  
            Estudiante["Ciudad"] = input("str", f"Ingresa la Ciudad de residencia Originaria")    
            Estudiante["direccion"] = input("str", f"Ingresa la Direccion de residencia")   
            Estudiante["telefono"]["celular"] = input("str", f"Ingresa el Numero Celular del Estudiante")
            Estudiante["telefono"]["fijo"] = input("str", f"Ingresa el Numero Fijo del Estudiante")
            Estudiante["acudiente"] = input("str", f"Nombre del Acudiente de {Estudiante['nombre']}")
            Estudiantes.update({Estudiante["cc"]:Estudiante})
            db.newFile(**Estudiantes)
            print(f"Estudiante {Estudiante['nombre']} Creado Correctamente")
        else:
            yes = input("Prefiere Editar los Estudiantes en Lugar de Crear uno Nuevo? ingrese S para si, enter para no")
            if yes.lower():
                editarEstudiante()
        yes = input("Desea Registrar Otro Estudiante ingrese S para si, enter para no")
        if not yes.lower():
            break

def editarEstudiante():
    while True:
        mn.showHeader("editarEstudiante")
        Estudiante = getEstudiante()
        if Estudiante:
            for key, value in Estudiante.items():
                if (type(value) == dict):
                    if not((key == "cc") or (key == "estado") or (key == "ruta") or (key == "trainer") or (key == "grupo")):
                        Seleccion =input(f"Desea Editar {key}")
                        if (Seleccion.lower()):
                            data = input("str", f"Ingresa {key}")
                            Estudiante.update({key: data})
                            db.newFile(**Estudiantes)
                            print("El Estudiante se Edito Correctamente")
        Desicion= input("Desea Editar Otro Estudiante")
        if not Desicion.lower():
            return

def Verificacion():
    while (True):
        cc = input("str", f"Ingresa la Cedula de Ciudadanida del Estudiante")
        if (cc in Estudiantes):
            print("Error el Usuario ya esta registrado")
            return False
        else:
            return cc
        
def getEstudiante():
    BusquedaEstudiante()
    cc = input("Ingresa la Cedula de Ciudadanida del Estudiante")
    return Estudiantes.get(cc)



def matricular():
    while(True):
        mn.showHeader("matricula")
        Estudiante = getEstudiante()
        if Estudiante:
            if (Estudiante["estado"] == "aprobado"):
                campus.loadCampuslanDB()
                mn.showHeader("rutas1")
                rutas = campus.campuslandDB.get("rutas")
                reusable.printList(list(rutas.keys()))
                opcion = reusable.input("str", "Ingresa el Nombre de la Ruta")
                if opcion in rutas:
                    ruta = rutas.get(opcion)
                    grupos = rutas[opcion]["grupos"]
                    trainers = rutas[opcion]["trainers"]
                    while True:
                        print(f"Trainers Disponibles {ruta['trainers']}")
                        trainer = reusable.input("str", f"Ingresa El Nombre del Trainer Para Asigarle a {Estudiante['nombre']}")
                        if trainer in trainers:
                            dataTrainer = campus.campuslandDB["trainers"][trainer]
                            while True:
                                print(f"Grupos Disponibles {ruta['grupos']}")
                                grupo = reusable.input("str", f"Ingresa El Nombre del Grupo Para Asigarle a {Estudiante['nombre']}")
                                if (grupo in dataTrainer["grupos"]) and (grupo in ruta["grupos"]):
                                    dataGrupo = campus.campuslandDB.get("grupos").get(grupo)
                                    if len(dataGrupo) <= 33:
                                        Estudiante.update({"ruta": ruta["nombreRuta"]})
                                        Estudiante.update({"trainer": trainer})
                                        Estudiante.update({"grupo": grupo})
                                        Estudiante.update({"estado": "estudiando"})
                                        dataGrupo.append(Estudiante["cc"])
                                        db.updateDataBases()
                                        reusable.showSuccess("Se Matriculo Correctamente")
                                        return
                                    else:
                                        reusable.showError(f"{ruta['nombreRuta']} Llego al Maximo de Estudiantes")
                                        return
                                else:
                                    reusable.showError(f"Ingresa el Grupo del Trainer {dataTrainer['nombre'].upper()}")
                        else:
                            reusable.showError("Ingresa el Nombre del Trainer Correctamente")
                else:
                    reusable.showError("Esta Ruta No Exite Ingresa Datos Reales")
            else:
                reusable.showInfo("El Estado del Estudiante No es Valido Para Esta Opcion")
        else:
            reusable.showInfo(f"No se Encontro al Estudiante")

        if not reusable.yesORnot("Desea Intentar Con Otro Estudiante"):
            break


def delEstudiante():
    mn.showHeader("eliminarEstudiante")
    Estudiante = getEstudiante()
    if Estudiante:
        Estudiantes.pop(Estudiante["cc"])
        db.newFile(**Estudiantes)
        reusable.showSuccess("El Estudiante Se Borro Correctamente")
    else:
        reusable.showError("Este Usuario no Existe en la Base de Datos")

URL = "Estudiantes.json"

def BusquedaEstudiante():
    db.URL = URL
    Estudiantes.update(db.checkFile(**Estudiantes))