class Nodo:
    __aparato=None
    __siguiente=None
    def __init__(self,aparato):
        self.__aparato=aparato
        self.__siguiente=None
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__aparato
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def setDato(self,dato):
        self.__aparato=dato