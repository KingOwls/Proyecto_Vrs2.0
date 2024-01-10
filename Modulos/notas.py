import Modulos.campers as sc
import Modulos.corefile as db
import Modulos.menus as menu
import Modulos.campusland as campus


def pruebaAdmision():
    while(True):
        print("prueba")
        Estudiante = sc.getEstudiante()
        if Estudiante:
            if (Estudiante["estado"] == "inscrito"):
                teorica = menu.checkInput("float", f"Ingresa la nota de la prueba teorica de {Estudiante['nombre']}")
                practica = menu.checkInput("float", f"Ingresa la nota de la prueba practica de {Estudiante['nombre']}")
                nota = (teorica + practica) / 2
                if (nota >= 60):
                    Estudiante["estado"] = "aprobado"
                else:
                    Estudiante["estado"] = "no_aprobado"

                print("Se Actualizo la Nota Correctamente")
                
            elif(Estudiante["estado"] == "no_aprobado"):
                print(f"El Estudiante {Estudiante['nombre']} ya Presento las Pruebas y NO fue apto")
            elif(Estudiante["estado"] == "aprobado"):
                print(f"El Estudiante {Estudiante['nombre']} ya Presento las Pruebas y Aprobo")
            else:
                print(f"El estado de {Estudiante['nombre']} no es apto para esta opcion")

        else:
            print("No se Encontro el Estudiante")
        
        if(not menu.yesORnot("Desea Registrar la Nota de otro Estudiante")):
                db.URL = "Estudiantes.json"
                db.newFile(**sc.Estudiantes)
                break

def menuNotas():
    while True:
        opcion = input("notas: 1) Fundamentos, 2) Web 3) Formal , 4) Base de datos, 5) Backend, 6)Salida")
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
        elif(opcion == "6"):
            break
        else:
            print("Opcion No Valida Intentalo De Nuevo")

def registrarNotas():
    print("registrarNotas")
    Estudiante = sc.getEstudiante()
    if Estudiante:
        if Estudiante["estado"] == "estudiando":
            key = menuNotas()
            notas = Estudiante.get("notas")
            if key in list(notas.keys()):
                print("Las Notas De Este Modulo Ya se Registraron")
            else:
                notaPruebaTecnica = (input("float", "Ingresa la Nota de la Prueba Tecnica")*((60)/100))
                notaPruebaTeorica = (input("float", "Ingresa la Nota de la Prueba Teorica")*(30)/100)
                notasTrabajosQuizes = (input("float", "Ingresa la Definitiva de Trabajos y Quizes")*(10)/100)
                definitiva = (notaPruebaTecnica + notaPruebaTeorica + notasTrabajosQuizes)
                notas.update({key:{
                    "notaPruebaTecnica": notaPruebaTecnica,
                    "notaPruebaTeorica": notaPruebaTeorica,
                    "notasTrabajosQuizes": notasTrabajosQuizes,
                    "definitiva": definitiva
                }})
                db.URL = sc.URL
                db.newFile(**sc.Estudiantes)
                print("Se Registraron las Notas Correctamente")
        else:
            print("El Estado del Estudiante No es Valido Para Esta Opcion")
    else:
        print("No Se Encontro al Estudiante")


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