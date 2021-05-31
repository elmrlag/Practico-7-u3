from ClaseColeccion import Coleccion
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseApoyo import Apoyo
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador

def Testeo():
    print("se inicia el testeo")

def opcion0():
    print("Saliendo")

def opcion1():
    print("se inicia el testeo 1")
    UnPersonal = DocenteInvestigador(24334047432, "navia", "adriel", 15000, 4, "artes", "profesor", "historia", "areaejemplo", "tipoejemplo", "categoriaejemplo", 4000)
    MColeccion.insertarElemento(UnPersonal, 5)

def opcion2():
    print("se inicia el testeo 2")
    OtroPersonal = Apoyo(34514528432, "pinos", "alejandra", 61000, 2, "apoyo")
    MColeccion.agregarElemento(OtroPersonal)

def opcion3():
    print("se inicia el testeo 3")
    MColeccion.mostrarElemento(8)

def opcion4():
    print("se inicia el testeo 4")
    UnaCarrera = input(str("Ingrese una carrera a buscar: "))
    MColeccion.MostrarPorCarrera(UnaCarrera)

def opcion5():
    print("se inicia el testeo 5")
    investigacion = input(str("Ingrese un area de investigacion: "))
    MColeccion.mostrarPorInvestigacion(investigacion)

def opcion6():
    print("se inicia el testeo 6")
    MColeccion.mostrarAgentesySueldos()

def opcion7():
    print("se inicia el testeo 7")
    categoria = input(str("Ingrese una categoria: "))
    MColeccion.mostrarListadoDinero(categoria)

def opcion8():
    print("se inicia el testeo 8")
    MColeccion.guardarEnJSON()

switcher ={
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
    6: opcion6,
    7: opcion7,
    8: opcion8
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opcion incorrecta"))
    func()

if __name__=='__main__':
    MColeccion = Coleccion()
    Testeo()

    bandera = False

    while not bandera:
        print("MENU DE OPCIONES")
        print("0 para salir")
        print("1 para Insertar a agentes a la colección")
        print("2 para Agregar agentes a la colección")
        print("3 para Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición")
        print("4 para Ingresar por teclado el nombre de una carrera y generar un listado")
        print("5 para Dada un área de investigación, contar la cantidad de agentes que son docente investigador")
        print("6 para Recorrer la colección y generar un listado que muestre nombre y apellido")
        print("7 para Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación")
        print("8 para Almacenar los datos de todos los agentes en el archivo “personal.json”")
        opcion = int(input("Ingrese valor: "))
        switch(opcion)
        bandera = int(opcion) == 0