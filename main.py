import Modulos.menus as menu
import Modulos.campers as sc
import Modulos.notas as notas
import Modulos.campusland as campus
import os




while (True):
        opMenu = input("Buenos dias: ¿que desea hacer hoy?: \n1) Desicion de Estudiante\n 2)registro de prueba de admision\n 3)registro de area de entrenamiento\n 4)registro de ruta de entrenamiento\n 5)gestionar matricula\n 6)registrar notas\n 7)registrar nuevo trainer\n 8)generar reportes\n 9)salir\n")
        if (opMenu == "1"):
            Desicion= input("Desea: 1)Registrar Estudiante, 2) Editar Estudiante, 3) Eliminar Estudiante")
            if(Desicion == "1"):
                print("registrar Estudiante")
                os.system("pause")
                sc.newEstudiante()
            elif(opMenu == "2"):
                print("Editar Estudiante")
                os.system("pause")
                sc.editarEstudiante()
            elif(opMenu == "3"):
                print("Editar Estudiante")
                os.system("pause")
                sc.delEstudiante()
        elif (opMenu == "2"):
            print("registro de prueba de admision")
            os.system("pause")
            notas.pruebaAdmision()
        elif(opMenu == "3"):
            print("registro de area de entrenamiento")
            os.system("pause")
            campus.newArea()
        elif(opMenu == "4"):
            print("registro de ruta de entrenamiento")
            os.system("pause")
            campus.newRuta()
        elif(opMenu == "5"):
            print("gestionar matricula")
            os.system("pause")
            sc.matricular()
        elif(opMenu == "6"):
            print("Registro de notas")
            os.system("pause")
            notas.registrarNotas()
        elif(opMenu == "7"):
            print("registrar nuevo trainer")
            os.system("pause")
            campus.newTrainer()
        elif(opMenu == "8"):
            print("generar reportes")
            os.system("pause")
            notas.moduloReportes()
        elif(opMenu == "9"):
            print("salir")
            menu.showSuccess("Gracias Por usar el Sistema")
            break
        else:
            menu.showError("Opcion No Valida Intentalo de Nuevo")