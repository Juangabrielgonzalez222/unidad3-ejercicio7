import json
from pathlib import Path
from ManejadorPersonal import ManejadorPersonal
from Docente import Docente
from Investigador import Investigador
from Apoyo import Apoyo
from DocenteInvestigador import DocenteInvestigador
class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        resultado=None
        if '__class__' not in d:
            resultado=-1
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ManejadorPersonal':
                personal=d['personal']
                manejador=class_()
                for i in range(len(personal)):
                    dPersonal=personal[i]
                    class_name=dPersonal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPersonal['__atributos__']
                    unPersonal=class_(**atributos)
                    manejador.agregarPersonal(unPersonal)
            resultado=manejador
        return resultado
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        resultado=-1
        try:
            with Path(archivo).open(encoding="UTF-8") as fuente:
                diccionario=json.load(fuente)
                fuente.close()
        except FileNotFoundError:
            print('El archivo {} no existe, no se cargaron datos'.format(archivo))
        else:
            resultado=diccionario
        return resultado
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)