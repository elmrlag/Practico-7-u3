from ClasePersonal import Personal

class Apoyo(Personal):
    __categoria = 0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = categoria

    def MostrarDatos(self):
        super().MostrarDatos()
        print("------ DATOS APOYO ------")
        print(f"Categoria: {self.__categoria}")
        print("------ ------ ------ ------")

    def MostrarCalculo(self):
        sumador = 0
        sumador += super().__sueldoBasico + ((super().__antiguedad * super().__sueldoBasico) / 100)

        if (self.__categoria >= 1 and self.__categoria <= 10):
            sumador += super().__sueldoBasico + ((10 * super().__sueldoBasico) / 100)

        if (self.__categoria >= 11 and self.__categoria <= 20):
            sumador += super().__sueldoBasico + ((20 * super().__sueldoBasico) / 100)

        if (self.__categoria >= 21 and self.__categoria <= 22):
            sumador += super().__sueldoBasico + ((30 * super().__sueldoBasico) / 100)

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
                            categoria = self.__categoria
                            )
            )
        return (d)