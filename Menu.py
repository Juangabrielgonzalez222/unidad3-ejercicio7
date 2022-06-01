from Apoyo import Apoyo
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.opcion6,
            7:self.opcion7,
            8:self.opcion8,
            9:self.salir
        }
    def lanzarMenu(self,manejadorPersonal,objectEncoder):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para insertar un personal en la colección en una posición determinada.')
            print('-Ingrese 2 para agregar un personal a la colección.')
            print('-Ingrese 3 para dada una posición de la Lista: Mostrar por pantalla qué tipo se encuentra almacenado en dicha posición.')
            print('-Ingrese 4 para generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.')
            print('-Ingrese 5 para dada un área de investigación, contar la cantidad de agentes que son docente investigador, y la cantidad de investigadores que trabajen en ese área.')
            print('-Ingrese 6 para generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.')
            print('-Ingrese 7 para listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen la categoría, al final del listado deberá mostrar el total de dinero se debe solicitar.')
            print('-Ingrese 8 para almacenar la Lista en el archivo.')
            print('-Ingrese 9 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<8:
                ejecutar(manejadorPersonal)
            elif opcion==8:
                ejecutar(manejadorPersonal,objectEncoder)
            else:
                ejecutar()
    def opcion1(self,manejadorPersonal):
        personal=self.cargarPersonal()
        if personal!=-1:
            posicion=self.cargarNumeroEntero('Ingrese posicion a insertar en la lista:\n')
            manejadorPersonal.insertarPersonal(personal,posicion)
    def opcion2(self,manejadorPersonal):
        personal=self.cargarPersonal()
        if personal!=-1:
            manejadorPersonal.agregarPersonal(personal)
    def opcion3(self,manejadorPersonal):
        posicion=self.cargarNumeroEntero('Ingrese posicion:\n')
        manejadorPersonal.mostrarPersonal(posicion)
    def opcion4(self,manejadorPersonal):
        carrera=input('Ingrese nombre de la carrera:\n')
        manejadorPersonal.listadoOrdenadoSegunCarrera(carrera)
    def opcion5(self,manejadorPersonal):
        areaInvestigacion=input('Ingrese area de investigacion:\n')
        manejadorPersonal.cantidadPorAreaInvestigacion(areaInvestigacion)
    def opcion6(self,manejadorPersonal):
        manejadorPersonal.listadoOrdenadoApellido()
    def opcion7(self,manejadorPersonal):
        categoriaInvestigacion=input('Ingrese categoria de investigacion:\n')
        manejadorPersonal.listadoPorCategoriaInvestigacion(categoriaInvestigacion)
    def opcion8(self,manejadorPersonal,objectEncoder):
        manejadorPersonal.guardarArchivo(objectEncoder)
    def cargarPersonal(self):
        resultado=-1
        print('A continuación debe seleccionar el tipo de personal: \n1:Docente,2:Apoyo,3:Investigador,4:Docente Investigador')
        tipo=self.cargarNumeroEntero('Ingrese el numero del tipo de personal:\n')
        personal=None
        if tipo>0 and tipo<5:
            cuil=input('Ingrese cuil:\n')
            apellido=input('Ingrese apellido:\n')
            nombre=input('Ingrese nombre:\n')
            sueldoBasico=self.cargarFlotante('Ingrese el sueldo basico:\n')
            antiguedad=self.cargarNumeroEntero('Ingrese la antiguedad:\n')
            if tipo==1:
                carrera=input('Ingrese la carrera:\n')
                cargo=input('Ingrese el cargo:\n')
                catedra=input('Ingrese la catedra:\n')
                personal=Docente(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra)
            elif tipo==2:
                categoria=self.cargarNumeroEntero('Ingrese la categoria:\n')
                personal=Apoyo(cuil,apellido,nombre,sueldoBasico,antiguedad,categoria)
            elif tipo==3:
                areaInvestigacion=input('Ingrese el area de investigacion:\n')
                tipoInvestigacion=input('Ingrese el tipo de investitacion:\n')
                personal=Investigador(cuil,apellido,nombre,sueldoBasico,antiguedad,None,None,None,areaInvestigacion,tipoInvestigacion)
            else:
                carrera=input('Ingrese la carrera:\n')
                cargo=input('Ingrese el cargo:\n')
                catedra=input('Ingrese la catedra:\n')
                areaInvestigacion=input('Ingrese el area de investigacion:\n')
                tipoInvestigacion=input('Ingrese el tipo de investitacion:\n')
                categoriaIncentivo=input('Ingrese la categoria de investigacion:\n')
                importeExtra=self.cargarFlotante('Ingrese el importe extra:\n')
                personal=DocenteInvestigador(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,areaInvestigacion,tipoInvestigacion,categoriaIncentivo,importeExtra)
            resultado=personal
        else:
            print('El numero ingresado no corresponde a ningun tipo.')  
        return resultado
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarFlotante(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se admiten numeros enteros y punto ,por ejemplo:500 o 500.50')
            else:
                bandera=False
        return numero
    def cargarBool(self,mensaje):
        resultado=None
        bandera=True
        opcion=''
        while bandera:
            print(mensaje)
            opcion=input('Ingrese "s" si tiene, "n" en caso contrario.\n')
            if opcion=='s':
                resultado=True
                bandera=False
            elif opcion=='n':
                resultado=False
                bandera=False
            else:
                print('Solo se admite "s" o "n"')
        return resultado
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')