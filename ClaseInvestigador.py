from ClasePersonal import Personal

class Investigador(Personal):
    __area = 0
    __tipo = 0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, area, tipo):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__area = area
        self.__tipo = tipo

    def MostrarDatos(self):
        super().MostrarDatos()
        print("------ DATOS INVESTIGADOR ------")
        print(f"Area: {self.__area}")
        print(f"Tipo: {self.__tipo}")
        print("------ ------ ------ ------")

    def GetArea(self):
        return (self.__area.lower())

    def MostrarCalculo(self):
        sumador = 0
        sumador += super().__sueldoBasico + ((super().__antiguedad * super().__sueldoBasico) / 100)

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
                            area = self.__area,
                            tipo = self.__tipo
                            )
            )
        return (d)