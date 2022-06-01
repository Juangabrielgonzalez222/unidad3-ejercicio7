from Docente import Docente
from Investigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __categoriaIncentivo=''
    __importeExtra=0
    def __init__(self, cuil='', apellido='', nombre='', sueldoBasico=0, antiguedad=0, carrera='', cargo='', catedra='', areaInvestigacion='', tipoInvestigacion='', categoriaIncentivo='', importeExtra=0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, areaInvestigacion, tipoInvestigacion)
        self.__categoriaIncentivo=categoriaIncentivo
        self.__importeExtra=importeExtra
    def getCategoriaIncentivo(self):
        return self.__categoriaIncentivo
    def getImporteExtra(self):
        return self.__importeExtra
    def mostrarDatos(self):
        super().mostrarDatos()
        print('Categoria Investigacion:{} Importe Extra:{}'.format(self.__categoriaIncentivo,self.__importeExtra))
    def calcularSueldo(self):
        resultado=0
        resultado=Docente.calcularSueldo(self)+self.__importeExtra
        return resultado
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(cuil=self.getCuil(), apellido=self.getApellido(), nombre=self.getNombre(), sueldoBasico=self.getSueldoBasico(), antiguedad=self.getAntiguedad(), carrera=self.getCarrera(), cargo=self.getCargo(), catedra=self.getCatedra(), areaInvestigacion=self.getAreaInvestigacion(), tipoInvestigacion=self.getTipoInvestigacion(), categoriaIncentivo=self.__categoriaIncentivo, importeExtra=self.__importeExtra))
        return d
    def tipoAgente(self):
        return 'Docente Investigador'