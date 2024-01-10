import Modulos.campers as sc
import Modulos.corefile as db
import templates.reusable as reusable
import templates.menus as menu
import Modulos.campusland as campus


def pruebaAdmision():
    while(True):
        menu.showHeader("prueba")
        Estudiante = sc.getEstudiante()
        if Estudiante:
            if (Estudiante["estado"] == "inscrito"):
                teorica = reusable.checkInput("float", f"Ingresa la nota de la prueba teorica de {Estudiante['nombre']}")
                practica = reusable.checkInput("float", f"Ingresa la nota de la prueba practica de {Estudiante['nombre']}")
                nota = (teorica + practica) / 2
                if (nota >= 60):
                    Estudiante["estado"] = "aprobado"
                else:
                    Estudiante["estado"] = "no_aprobado"

                reusable.showSuccess("Se Actualizo la Nota Correctamente")
                
            elif(Estudiante["estado"] == "no_aprobado"):
                reusable.showInfo(f"El Estudiante {Estudiante['nombre']} ya Presento las Pruebas y NO fue apto")
            elif(Estudiante["estado"] == "aprobado"):
                reusable.showInfo(f"El Estudiante {Estudiante['nombre']} ya Presento las Pruebas y Aprobo")
            else:
                reusable.showInfo(f"El estado de {Estudiante['nombre']} no es apto para esta opcion")

        else:
            reusable.showInfo("No se Encontro el Estudiante")
        
        if(not reusable.yesORnot("Desea Registrar la Nota de otro Estudiante")):
                db.URL = "Estudiantes.json"
                db.newFile(**sc.Estudiantes)
                break

def menuNotas():
    while True:
        opcion = input(menu.showMenu("notas"))
        if (opcion == "1"):
            return "moduloFundamentos"
        elif(opcion == "2"):
            return "moduloWEB"
        elif(opcion == "3"):
            return "moduloFormal"
        elif(opcion == "4"):
            return "moduloBaseDatos"
        elif(opcion == "5"):
            return "moduloBackend"
        else:
            reusable.showError("Opcion No Valida Intentalo De Nuevo")

def registrarNotas():
    menu.showHeader("registrarNotas")
    Estudiante = sc.getEstudiante()
    if Estudiante:
        if Estudiante["estado"] == "estudiando":
            key = menuNotas()
            notas = Estudiante.get("notas")
            if key in list(notas.keys()):
                reusable.showError("Las Notas De Este Modulo Ya se Registraron")
            else:
                notaPruebaTecnica = (reusable.checkInput("float", "Ingresa la Nota de la Prueba Tecnica")*0.6)
                notaPruebaTeorica = (reusable.checkInput("float", "Ingresa la Nota de la Prueba Teorica")*0.3)
                notasTrabajosQuizes = (reusable.checkInput("float", "Ingresa la Definitiva de Trabajos y Quizes")*0.1)
                definitiva = (notaPruebaTecnica + notaPruebaTeorica + notasTrabajosQuizes)
                notas.update({key:{
                    "notaPruebaTecnica": notaPruebaTecnica,
                    "notaPruebaTeorica": notaPruebaTeorica,
                    "notasTrabajosQuizes": notasTrabajosQuizes,
                    "definitiva": definitiva
                }})
                db.URL = sc.URL
                db.newFile(**sc.Estudiantes)
                reusable.showSuccess("Se Registraron las Notas Correctamente")
        else:
            reusable.showInfo("El Estado del Estudiante No es Valido Para Esta Opcion")
    else:
        reusable.showError("No Se Encontro al Estudiante")

def moduloReportes():
    sc.BusquedaEstudiante()
    campus.loadCampuslanDB()
    Estudiantes = sc.Estudiantes
    campuslandDB = campus.campuslandDB
    while True:
        opcion = input(menu.showMenu("reportes"))
        if (opcion == "1"):
            reusable.printList(newReporte("inscrito", Estudiantes))
        elif(opcion == "2"):
            reusable.printList(newReporte("aprobado", Estudiantes))
        elif(opcion == "3"):
            menu.showHeader("trainers")
            trainers = campuslandDB.get("trainers")
            reusable.printList(list(trainers.keys()))
        elif(opcion == "4"):
            reusable.printList(bajoNotas(Estudiantes))
        elif(opcion == "5"):
            menu.showHeader("rutas1")
            rutas = campuslandDB["rutas"]
            reusable.printList(list(rutas.keys()))
            rutaName = reusable.checkInput("str", "Ingresa el Nombre de la Ruta")
            if rutaName in list(rutas.keys()):
                menu.showHeader("infoRutas")
                ruta = rutas[rutaName]
                print(f"Nombre de la Ruta: {ruta['nombreRuta']}")
                print(f"Trainers de la Ruta: ", end="")
                for trainer in ruta["trainers"]:
                    print(trainer.upper(), end="")
                print("")
                print(f"Estudiantes De la Ruta {ruta['nombreRuta']}")
                grupos = ruta["grupos"]
                estudiantes = []
                for Estudiante in Estudiantes.values():
                    if "grupo" in Estudiante.keys():
                        if (Estudiante["grupo"] in grupos):
                            estudiantes.append(f"CC: {Estudiante['cc']} Nombre: {Estudiante['nombre']}")
                
                if not len(estudiantes):
                    print("No Se Encontraron Estudiantes")

                reusable.printList(estudiantes)
            else:
                print("No se Encontro la ruta a Mostrar")
        elif(opcion == "6"):
            perModul = {}
            pasaron = 0
            perdieron = 0
            for Estudiante in Estudiantes.values():
                notas = Estudiante["notas"]
                for key,value in notas.items():
                    nota = value["definitiva"]
                    if nota < 60:
                        perdieron += 1 
                    else:
                        pasaron += 1

                    perModul.update({key: {"pasaron": pasaron, "perdieron":perdieron}})
            message = "Falta Registrar Notas De Algunos Modulos Intentalo de Nuevo mas Tarde"
            for key, value in perModul.items():
                reusable.showSuccess(f"En el Modulo {key} Pasaron:{value['pasaron']} y Perdieron: {value['perdieron']}")
                if key == "backend":
                    message = ""
            
            if message:
                reusable.showInfo(message)


        elif(opcion == "7"):
            return
        else:
            reusable.showError("Opcion No Valida Intentalo de Nuevo")


def bajoNotas(Estudiantes):
    data = []
    for Estudiante in Estudiantes.values():
        notas = Estudiante["notas"]
        for modulo in notas.values():
            nota = modulo["definitiva"]
            if nota < 60:
                data.append(f"CC: {Estudiante['cc']} Nombre: {Estudiante['nombre']}")
    
    menu.showHeader("bajoRendimiento")
    if not len(data):
        print("No Se Encontraron Datos Con esa Caracteristica")

    return data
        

def newReporte(estado, Estudiantes:dict):
    if estado:
        menu.showHeader(estado)
        data = []
        for key, value in Estudiantes.items():
                if value["estado"] == estado:
                    data.append(f"Nombre del Estudiante: {value['nombre']}")

    if not len(data):
        print("No Se Encontraron Datos Con esa Caracteristica")

    return data