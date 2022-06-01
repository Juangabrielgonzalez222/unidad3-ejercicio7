import abc
from abc import ABC
class Personal(ABC):
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldoBasico=0
    __antiguedad=0
    def __init__(self,cuil='',apellido='',nombre='',sueldoBasico=0,antiguedad=0,carrera='',cargo='',catedra='',areaInvestigacion='',tipoInvestigacion=''):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoBasico=sueldoBasico
        self.__antiguedad=antiguedad
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def mostrarDatos(self):
        print('Cuil:',self.__cuil)
        print('Nombre:{} Apellido:{}'.format(self.__nombre,self.__apellido))
        print('Sueldo basico:{} Antiguedad:{}'.format(self.__sueldoBasico,self.__antiguedad))
    def mostrarDatosYSueldo(self):
        print('Apellido:{} Nombre:{} Tipo:{} Sueldo:{}'.format(self.__apellido,self.__nombre,self.tipoAgente(),self.calcularSueldo()))
    def calcularPorAntiguedad(self):
        resultado=(self.__sueldoBasico*self.__antiguedad)/100
        return resultado
    @abc.abstractclassmethod
    def calcularSueldo():
        pass
    @abc.abstractclassmethod
    def tipoAgente():
        pass
    def toJSON(self):
        return dict(cuil=self.__cuil,apellido=self.__apellido,nombre=self.__nombre,sueldoBasico=self.__sueldoBasico,antiguedad=self.__antiguedad)