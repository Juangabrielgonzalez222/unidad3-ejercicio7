from Personal import Personal

class Investigador(Personal):
    __areaInvestigacion=''
    __tipoInvestigacion=''
    def __init__(self, cuil='', apellido='', nombre='', sueldoBasico=0, antiguedad=0, carrera='', cargo='', catedra='', areaInvestigacion='', tipoInvestigacion=''):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvestigacion, tipoInvestigacion)
        self.__areaInvestigacion=areaInvestigacion
        self.__tipoInvestigacion=tipoInvestigacion
    def getAreaInvestigacion(self):
        return self.__areaInvestigacion
    def getTipoInvestigacion(self):
        return self.__tipoInvestigacion
    def mostrarDatos(self):
        super().mostrarDatos()
        print('Area Investigacion:{} Tipo Investigacion:{}'.format(self.__areaInvestigacion,self.__tipoInvestigacion))
    def calcularSueldo(self):
        resultado=0
        resultado=self.getSueldoBasico()+self.calcularPorAntiguedad()
        return resultado
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),areaInvestigacion=self.__areaInvestigacion,tipoInvestigacion=self.__tipoInvestigacion))
        return d
    def tipoAgente(self):
        return 'Investigador'