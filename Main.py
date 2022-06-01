from ManejadorPersonal import ManejadorPersonal
from Menu import Menu
from ObjectEncoder import ObjectEncoder

if __name__== '__main__':
	objectEncoder=ObjectEncoder()
	manejadorPersonal=None
	archivo='personal.json'
	diccionario=objectEncoder.leerJSONArchivo(archivo)
	if diccionario!=-1:
		manejadorPersonal=objectEncoder.decodificarDiccionario(diccionario)
		print('Se cargaron datos del archivo',archivo)
	else:
		manejadorPersonal=ManejadorPersonal()
	menu=Menu()
	menu.lanzarMenu(manejadorPersonal,objectEncoder)