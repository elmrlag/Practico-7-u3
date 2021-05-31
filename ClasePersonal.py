class Personal:
    __cuil = 0
    __apellido = 0
    __nombre = 0
    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def MostrarDatos(self):
        print("------ DATOS PERSONA ------")
        print(f"Cuil: {self.__cuil}")
        print(f"Apellido: {self.__apellido}")
        print(f"Nombre: {self.__nombre}")
        print(f"Sueldo Basico: {self.__sueldoBasico}")
        print(f"Antiguedad: {self.__antiguedad}")
        print("------ ------ ------ ------")

    def MostrarAgenteySueldo(self):
        print(f"Nombre y apellido: {self.__nombre} {self.__apellido}")
        print(f"Sueldo: {self.__sueldoBasico}")