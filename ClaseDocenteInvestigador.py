from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoria = 0
    __importe = 0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, area, tipo, categoria, importe):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__categoria = categoria
        self.__importe = importe

    def MostrarDatos(self):
        super().MostrarDatos()
        print("------ DATOS INVESTIGADOR ------")
        print(f"Categoria: {self.__categoria}")
        print(f"Importe: {self.__importe}")
        print("------ ------ ------ ------")

    def MostrarCalculo(self):
        sumador = 0
        sumador += super().__sueldoBasico + ((super().__antiguedad * super().__sueldoBasico) / 100)

        if (super().__cargo == "simple"):
            sumador += super().__sueldoBasico + ((10 * super().__sueldoBasico) / 100)

        if (super().__cargo == "semiexclusivo"):
            sumador += super().__sueldoBasico + ((20 * super().__sueldoBasico) / 100)

        if (super().__cargo == "exclusivo"):
            sumador += super().__sueldoBasico + ((50 * super().__sueldoBasico) / 100)

        sumador += self.__importe

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
                            carrera = super().__carrera,
                            cargo = super().__cargo,
                            catedra = super().__catedra,
                            categoria = self.__categoria,
                            importe = self.__importe
                            )
            )
        return (d)