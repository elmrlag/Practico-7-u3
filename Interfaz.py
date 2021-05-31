from zope.interface import Interface
from zope.interface import implementer

class Interfaz(Interface):

    def insertarElemento(Elemento, posi):
        pass

    def agregarElemento(Elemento):
       pass

    def mostrarElemento(posi):
        pass

    def mostrarPorCarrera(carrera):
        pass

    def mostrarPorInvestigacion(investigacion):
        pass

    def mostrarAgenteySueldo():
        pass

    def mostrarListadoDinero(categoria):
        pass