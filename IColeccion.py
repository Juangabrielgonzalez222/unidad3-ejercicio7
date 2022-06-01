from zope.interface import Interface
class IColeccion(Interface):
    def insertarElemento(elemento,posicion):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(posicion):
        pass