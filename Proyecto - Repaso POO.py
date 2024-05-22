listaEstudiantes = []

class Persona:
    def __init__(self, _cedula, _nombre, _apellido, _edad):
        self.__cedula = _cedula
        self.__nombre = _nombre
        self.__apellido = _apellido
        self.__edad = _edad

    @property
    def cedula(self):
        return self.__cedula
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido

class Estudiantes(Persona):
    def __init__(self, _cedula, _nombre, _apellido, _edad, _nota1, _nota2, _nota3):
        super().__init__(_cedula, _nombre, _apellido, _edad)
        self.__nota1 = _nota1
        self.__nota2 = _nota2
        self.__nota3 = _nota3
        self.__notaFinal = (_nota1 + _nota2 + _nota3) / 3
        self.__historial = []
    
    @property
    def cedula(self):
        return self._Persona__cedula
    
    @property
    def nombre(self):
        return self._Persona__nombre

    @property
    def apellido(self):
        return self._Persona__apellido
    
    @property
    def notaFinal(self):
        return self.__notaFinal

    @property
    def historial(self):
        return self.__historial
    
    def descripcion(self):
        return "Estudiante de pregrado"

    def entregarDatos(self):
        print("No. Cedula: {} - {} {} - Nota Final: {}".format(self.cedula, self.nombre, self.apellido, self.notaFinal))

    def editarNotas(self, _nota1, _nota2, _nota3):
        self.__nota1 = _nota1
        self.__nota2 = _nota2
        self.__nota3 = _nota3
        self.__notaFinal = (_nota1 + _nota2 + _nota3) / 3
        print("Registro Exitoso!")
    
    def incluirEvento(self, _nota1, _nota2, _nota3):
        return ("modificacion: Nota_1: {} Nota_2: {} Nota_3: {}".format(_nota1, _nota2, _nota3))
    
    def entregaHistorial(self):
        print("No. Cedula: {} - {} {}".format(self.cedula, self.nombre, self.apellido))

class EstudianteDePosgrado(Estudiantes):
    def __init__(self, _cedula, _nombre, _apellido, _edad, _nota1, _nota2, _nota3, _especialidad):
        super().__init__(_cedula, _nombre, _apellido, _edad, _nota1, _nota2, _nota3)
        self.__especialidad = _especialidad
    
    def descripcion(self):
        return "Estudiante de posgrado en " + self.__especialidad

    def registrarEstudiante():
        print("Registro de Estudiantes\n")
        cedula = int(input("Ingrese el numero de cedula: "))
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = int(input("Ingrese su edad: "))
        nota1 = float(input("Ingrese nota 1: "))
        nota2 = float(input("Ingrese nota 2: "))
        nota3 = float(input("Ingrese nota 3: "))
        objAlumno = Estudiantes(cedula, nombre, apellido, edad, nota1, nota2, nota3)
        listaEstudiantes.append(objAlumno)

    def listadoEstudiantes():
        print("Listado de Estudiantes\n")
        for objAlumno in listaEstudiantes:
            objAlumno.entregarDatos()

    def buscarEstudiante():
        print("Buscar Estudiante\n")
        cedula = int(input("Ingrese el numero de cedula a buscar: "))
        for objAlumno in listaEstudiantes:
            if cedula == objAlumno.cedula:
                objAlumno.entregarDatos()


    def modificarNotas():
        print("Modificar Notas\n")
        cedula = int(input("Ingrese el numero de cedula a buscar: "))
        for objAlumno in listaEstudiantes:
            if cedula == objAlumno.cedula:
                nota1 = float(input("Ingrese nota 1: "))
                nota2 = float(input("Ingrese nota 2: "))
                nota3 = float(input("Ingrese nota 3: ")) 
                objAlumno.editarNotas(nota1, nota2, nota3)
                objAlumno.entregarDatos()
                recepcionMensaje = objAlumno.incluirEvento(nota1, nota2, nota3)
                objAlumno.historial.append(recepcionMensaje)

    def consultarHistorial():
        print("Consulta de Historial\n")
        cedula = int(input("Ingrese el numero de cedula a buscar: "))
        for objAlumno in listaEstudiantes:
            if cedula == objAlumno.cedula:
                for recepcionMensaje in objAlumno.historial:
                    print("Evento: {}".format(recepcionMensaje))

    def salir():
        print("Salida inminente...!")
        exit()

    def main():
        while True:
            print("\n")
            print("|****************************|")
            print("|**|      Bienvenidos     |**|")
            print("|**|         Menu         |**|")
            print("|****************************|")
            print("")
            print("Seleccione una de las siguientes opciones:");
            print("1.- Registrar Estudiante")
            print("2.- Mostrar Estudiantes")
            print("3.- Buscar Estudiante")
            print("4.- Modificar notas")
            print("5.- Consultar Historial")
            print("6.- Salir\n")

            opcion = int(input("Opcion: "))

            if opcion == 1:
                EstudianteDePosgrado.registrarEstudiante()
            elif opcion == 2:
                EstudianteDePosgrado.listadoEstudiantes()
            elif opcion == 3:
                EstudianteDePosgrado.buscarEstudiante()
            elif opcion == 4:
                EstudianteDePosgrado.modificarNotas()
            elif opcion == 5:
                EstudianteDePosgrado.consultarHistorial()
            elif opcion == 6:
                EstudianteDePosgrado.salir()

if __name__ == '__main__':
    EstudianteDePosgrado.main();




