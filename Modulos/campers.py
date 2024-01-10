import Modulos.corefile as data
import Modulos.menus as menu
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
            data.newFile(**Estudiantes)
            print(f"Estudiante {Estudiante['nombre']} Creado Correctamente")
        else:
            yes = input("Prefiere Editar los Estudiantes en Lugar de Crear uno Nuevo? ingrese S para si, enter para no")
            if yes.lower():
                editarEstudiante()
        yes = input("Desea Registrar Otro Estudiante ingrese S para si, enter para no")
        if not yes.lower():
            break

def editarEstudiante():
    print("editar Estudiante")
    while True:
        Estudiante = getEstudiante()
        if Estudiante:
            for key, value in Estudiante.items():
                if (type(value) == dict):
                    if not((key == "cc") or (key == "estado") or (key == "ruta") or (key == "trainer") or (key == "grupo")):
                        Seleccion =input(f"Desea Editar {key}")
                        if (Seleccion.lower()):
                            data = input("str", f"Ingresa {key}")
                            Estudiante.update({key: data})
                            data.newFile(**Estudiantes)
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
        print("Matricula")
        Estudiante = getEstudiante()
        if Estudiante:
            if (Estudiante["estado"] == "aprobado"):
                campus.loadCampuslanDB()
                print("Ruta a tomar")
                rutas = campus.campuslanddata.get("rutas")
                menu.printList(list(rutas.keys()))
                opcion = menu.input("str", "Ingresa el Nombre de la Ruta")
                if opcion in rutas:
                    ruta = rutas.get(opcion)
                    grupos = rutas[opcion]["grupos"]
                    trainers = rutas[opcion]["trainers"]
                    while True:
                        print(f"Trainers Disponibles {ruta['trainers']}")
                        trainer = menu.input("str", f"Ingresa El Nombre del Trainer Para Asigarle a {Estudiante['nombre']}")
                        if trainer in trainers:
                            dataTrainer = campus.campuslanddata["trainers"][trainer]
                            while True:
                                print(f"Grupos Disponibles {ruta['grupos']}")
                                grupo = menu.input("str", f"Ingresa El Nombre del Grupo Para Asigarle a {Estudiante['nombre']}")
                                if (grupo in dataTrainer["grupos"]) and (grupo in ruta["grupos"]):
                                    dataGrupo = campus.campuslanddata.get("grupos").get(grupo)
                                    if len(dataGrupo) <= 33:
                                        Estudiante.update({"ruta": ruta["nombreRuta"]})
                                        Estudiante.update({"trainer": trainer})
                                        Estudiante.update({"grupo": grupo})
                                        Estudiante.update({"estado": "estudiando"})
                                        dataGrupo.append(Estudiante["cc"])
                                        data.updateDataBases()
                                        print("Se Matriculo Correctamente")
                                        return
                                    else:
                                        print(f"{ruta['nombreRuta']} Llego al Maximo de Estudiantes")
                                        return
                                else:
                                    print(f"Ingresa el Grupo del Trainer {dataTrainer['nombre'].upper()}")
                        else:
                            print("Ingresa el Nombre del Trainer Correctamente")
                else:
                    print("Esta Ruta No Exite Ingresa Datos Reales")
            else:
                print("El Estado del Estudiante No es Valido Para Esta Opcion")
        else:
            print(f"No se Encontro al Estudiante")
        tomar= input("Desea Intentar Con Otro Estudiante")
        if not tomar.lower():
            break


def delEstudiante():
    print("eliminarEstudiante")
    Estudiante = getEstudiante()
    if Estudiante:
        Estudiantes.pop(Estudiante["cc"])
        data.newFile(**Estudiantes)
        print("El Estudiante Se Borro Correctamente")
    else:
        print("Este Usuario no Existe en la Base de Datos")

URL = "Estudiantes.json"

def BusquedaEstudiante():
    data.URL = URL
    Estudiantes.update(data.checkFile(**Estudiantes))