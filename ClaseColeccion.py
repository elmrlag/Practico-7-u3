from zope.interface import implementer
from Interfaz import Interfaz
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseApoyo import Apoyo
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
import numpy as np
import json
from pathlib import Path

@implementer(Interfaz)

class Coleccion():
    __dimension = 0
    __actual = 0
    __cantidad = 0
    __elementos = None

    def __init__(self, dimension = 10):
        self.__dimension = dimension
        self.__actual = 0
        self.__cantidad = 0
        self.__elementos = np.empty(dimension)

    def insertarElemento(self, Elemento, posi):
        try:
            self.__elementos[posi] = Elemento
        except:
            print(f"la posicion {posi} no es valida")

    def agregarElemento(self, Elemento):
        self.__elementos[self.__actual] = Elemento
        self.__actual += 1

    def mostrarElemento(self, posi):
        try:
            print(self.__elementos[posi].MostrarDatos())
        except IndexError:
            print(f"la posicion {posi} no es valida para mostrar")

    def mostrarPorCarrera(self, carrera):
        for i in range (len(self.__elementos)):
            if (carrera.lower() == self.__elementos[i].GetCarrera()):
                self.__elementos[i].MostrarDatos()

    def mostrarPorInvestigacion(self, investigacion):
        cont = 0
        for i in range (len(self.__elementos)):
            if (type(self.__elementos[i]) == "DocenteInvestigador" or type(self.__elementos[i]) == "Investigador"):
                if (self.__elementos[i].GetArea == investigacion):
                    cont += 1
        print(f"la cantidad de personal implicado con la investigacion {investigacion} es de {cont}")

    def mostrarAgentesySueldos(self):
        for i in range (len(self.__elementos)):
            self.__elementos[i].MostrarAgenteySueldo()

    def mostrarListadoDinero(self, categoria):
        for i in range (len(self.__elementos)):
            if (type(self.__elementos[i]) == "DocenteInvestigador"):
                if (self.__elementos[i].GetCategoria() == categoria):
                    mostrar = self.__elementos[i].MostrarCalculo()
        print(mostrar)

    def guardarEnJSON(self):
        for i in range (len(self.__elementos)):
            d = self.__elementos[i].toJSON()
            with Path("personal.json").open("w", encoding="UTF-8") as destino:
                json.dump(d, destino, indent=4)
                destino.close()

