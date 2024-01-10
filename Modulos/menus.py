import os

opcions = {
    "rutaMenu": [
        "Crear Ruta Nueva",
        "Editar Ruta Existente",
        "Salir"
    ],
    "jornada":[
        "mañana",
        "tarde",
    ],
    "trainers":[
        "Crear Nuevo Trainer",
        "Editar Trainer",
        "Salir"
    ],
    "notas":[
        "Fundamentos de Programacion",
        "Programacion WEB",
        "Programacion Formal",
        "Base de Datos",
        "Backend"
    ],
    "reportes":[
        "Listar los campers que se encuentren en estado de inscrito",
        "Listar los campers que aprobaron el examen inicial y no estan Matriculados",
        "Listar los entrenadores que se encuentran trabajando con campuslands",
        "Listar los estudiantes que cuentan con bajo rendimiento.",
        "Listar los campers y entrenador de ruta de entrenamiento",
        "Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos",
        "Salir"
    ]
}
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