from ClasePersonal import Personal

class Docente(Personal):
    __carrera = 0
    __cargo = 0
    __catedra = 0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def MostrarDatos(self):
        super().MostrarDatos()
        print("------ DATOS DOCENTE ------")
        print(f"Carrera: {self.__carrera}")
        print(f"Cargo: {self.__cargo}")
        print(f"Catedra: {self.__catedra}")
        print("------ ------ ------ ------")

    def GetCarrera(self):
        return (self.__carrera.lower())

    def MostrarCalculo(self):
        sumador = 0
        sumador += super().__sueldoBasico + ((super().__antiguedad * super().__sueldoBasico) / 100)

        if (super().__cargo == "simple"):
            sumador += super().__sueldoBasico + ((10 * super().__sueldoBasico) / 100)

        if (super().__cargo == "semiexclusivo"):
            sumador += super().__sueldoBasico + ((20 * super().__sueldoBasico) / 100)

        if (super().__cargo == "exclusivo"):
            sumador += super().__sueldoBasico + ((50 * super().__sueldoBasico) / 100)

        return (sumador)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil = super().__cuil,
                            apellido = super().__apellido,
                            nombre = super().__nombre,
                            sueldoBasico = super().__sueldoBasico,
                            antiguedad = super().__antiguedad,
                            carrera = self.__carrera,
                            cargo = self.__cargo,
                            catedra = self.__catedra
                            )
            )
        return (d)