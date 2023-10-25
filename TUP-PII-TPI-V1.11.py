from abc import ABC, abstractmethod
import random


class Usuario(ABC):
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def __str__(self):
        return self.email

    def validar_credenciales(self, email, password):
        return self.email == email and self.password == password


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, password, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, password)
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mi_cursos = []

    def __str__(self):
        return f"ESTUDIANTE: {self.nombre} {self.apellido}, LEGAJO: {self.legajo}, AÑO DE INSCRIPCION: {self.anio_inscripcion_carrera}"

    def matricular_en_curso(self, curso):
        if curso not in self.mi_cursos:
            self.mi_cursos.append(curso)
            return True
        else:
            return False


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, password, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, password)
        self.nombre = nombre
        self.apellido = apellido
        self.titulo = titulo
        self.anio_egreso = anio_egreso
        self.mis_cursos = []

    def __str__(self):
        return f"PROFESOR: {self.nombre} {self.apellido}, TITULO: {self.titulo}, AÑO DE EGRESO: {self.anio_egreso}"

    def dictar_curso(self, curso):
        self.mis_cursos.append(curso)


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contraseña = ''.join(random.choice(
            '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(6))
        self.archivos = []

    def __str__(self):
        return f"NOMBRE: {self.nombre}\CONTRASEÑA: {self.contraseña}"

    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)


alumno1 = Estudiante("Héctor", "Mendoza", "hectormaximendoza@gmail.com",
                     "71192HECTOR", 12345, 2022)
profesor1 = Profesor("Ema Elsa", "Candia",
                     "emaecandia@gmail.com", "ema1971", "PhD", 2010)

curso1 = Curso("INGLES 1")
curso2 = Curso("INGLES 2")
curso3 = Curso("LABORATORIO 1")
curso4 = Curso("LABORATORIO 2")
curso5 = Curso("PROGRAMACION 1")
curso6 = Curso("PROGRAMACION 2")

profesor1.dictar_curso(curso1)
profesor1.dictar_curso(curso2)
profesor1.dictar_curso(curso3)
profesor1.dictar_curso(curso4)
profesor1.dictar_curso(curso5)
profesor1.dictar_curso(curso6)


def login_alumno(email, password):
    for alumno in alumnos:
        if alumno.validar_credenciales(email, password):
            return alumno
    return None


def login_profesor(email, password):
    for profesor in profesores:
        if profesor.validar_credenciales(email, password):
            return profesor
    return None


alumnos = [alumno1]
profesores = [profesor1]

cursos_sistema = [curso1, curso2, curso3, curso4, curso5, curso6]

while True:
    print("\nMENU:")
    print("1. INGRESO COMO ESTUDIANTE")
    print("2. INGRESO COMO PROFESOR")
    print("3. VER LOS CURSOS")
    print("4. SALIR")

    opcion = input("ELIJA UNA OPCION: ")

    if opcion == "1":
        email = input("EMAIL ALUMNO: ")
        password = input("CONTRASEÑA: ")

        alumno = login_alumno(email, password)

        if alumno:
            while True:
                print("\nSUBMENU:")
                print("1. MATRICULARSE AL CURSO")
                print("2. VER CURSOS MATRICULADOS")
                print("3. REGRESAR AL MENU PRINCIPL")
                sub_opcion = input("ELIJA UNA OPCION: ")

                if sub_opcion == "1":
                    print("\nCURSOS QUE ESTAN DISPONIBLES:")
                    for i, curso in enumerate(cursos_sistema, start=1):
                        print(f"{i}. {curso.nombre}")

                    curso_index = int(input("ELIJA UN CURSO PARA MATRICULARSE: ")) - 1

                    if 0 <= curso_index < len(cursos_sistema):
                        curso_seleccionado = cursos_sistema[curso_index]
                        matriculado = alumno.matricular_en_curso(
                            curso_seleccionado)

                        if matriculado:
                            print(
                                f"SU MATRICULACION FUI EXITOSA {curso_seleccionado.nombre}")
                        else:
                            print(
                                f"MATRICULADO EN  {curso_seleccionado.nombre}")

                elif sub_opcion == "2":
                    print("\nCURSOS MATRICULADOS:")
                    for i, curso in enumerate(alumno.mi_cursos, start=1):
                        print(f"{i}. {curso.nombre}")

                    curso_index = int(
                        input("SELECCIONE CURSO PARA VER ARCHIVOS: ")) - 1

                    if 0 <= curso_index < len(alumno.mi_cursos):
                        curso_seleccionado = alumno.mi_cursos[curso_index]
                        print(f"ARCHIVOS EN {curso_seleccionado.nombre}:")
                        for archivo in curso_seleccionado.archivos:
                            print(archivo)

                elif sub_opcion == "3":
                    break
        else:
            print("LOS DATOS INGRESADOS NO COINCIDEN CON NUESTROS REGISTROS. POR FAVOR, REGISTRESE.")

    elif opcion == "2":
        email = input("INGRES EMAIL DE PROFESOR: ")
        password = input("CONTRASEÑA: ")

        profesor = login_profesor(email, password)

        if profesor:
            while True:
                print("\nnSUBMENU:")
                print("1. DICTAR CURSO")
                print("2. VER CURSOS DICTADOS")
                print("3. REGRESAR AL MENU PRINCIPAL")
                sub_opcion = input("ELIJA UNA OPCION ")

                if sub_opcion == "1":
                    nombre_curso = input(
                        "INGRESE NOMBRE DEL CURSO PARA DAR DE ALTA: ")
                    nuevo_curso = Curso(nombre_curso)
                    profesor.dictar_curso(nuevo_curso)
                    print(f"CURSO DADO DE ALTA:\n{str(nuevo_curso)}")

                elif sub_opcion == "2":
                    print("\nCURSOS DICTADOS:")
                    for i, curso in enumerate(profesor.mis_cursos, start=1):
                        print(
                            f"{i}. {curso.nombre}\CONTRASEÑA: {curso.contraseña}")

                elif sub_opcion == "3":
                    break
        else:
            print("LOS DATOS INGRESADOS NO COINCIDEN CON NUESTROS REGISTROS. POR FAVOR HABLE CON ALUMNADO")

    elif opcion == "3":
        print("\nCURSOS EN EL SISTEMA:")
        for i, curso in enumerate(cursos_sistema, start=1):
            print(
                f"{i}. MATERIA: {curso.nombre} CURSO: TECNICATURA DE PROGRAMACION")

    elif opcion == "4":
        print("ESTA SALIENDO DEL SISTEMA! HASTA PRONTO ! ")
        break

    else:
        print("SELECCION INCORRECTA. INTENTE CON UNA OPCION VALIDA.")