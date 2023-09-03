from Hans_Packages import Pypack

carpeta = 'Europa.zip'
carpeta1 = '__init__.py'
carpeta2 = 'mi_web.zip'
carpeta3 = 'archivo_comprimido.zip'
direccion = "C:\\Users\\hansn\\OneDrive\\Escritorio"
direccion1 = 'C:\\Users\\hansn\\PycharmProjects\\Hans_Package\\Hans_Packages'
direccion2 = 'C:\\Users\\hansn\\Downloads'
direccion3 = 'C:\\Users\\hansn\\PycharmProjects\\Hans_Package'

# print(Pypack.unpack(folder=carpeta3)) # Si la funcion "unpack" recibe solo un argumento, esta descomprime la carpeta dentro del directorio de trabajo
# print(Pypack.unpack(folder=carpeta2, origin=direccion2))
# print(Pypack.unpack(folder=carpeta3, destination=direccion3))
# print(Pypack.unpack(folder=carpeta, origin=direccion, destination=direccion3))

#print(Pypack.pack(files='Dia_9.py'))
#print(Pypack.pack(files=['Dia_9.py','prueba.txt','prueba1.txt']))
#print(Pypack.pack(files='all', destination=direccion3))
#print(Pypack.pack(files=['Dia_9.py','prueba.txt','prueba1.txt'], destination="C:\\Users\\hansn\\OneDrive\\Escritorio"))
#print(Pypack.pack(files=['Sin título.png','Sin título2.png','Sin título3.png'], origin="C:\\Users\\hansn\\OneDrive\\Escritorio"))
#print(Pypack.pack(files='Sin título3.png', origin="C:\\Users\\hansn\\OneDrive\\Escritorio"))
#print(Pypack.pack(files=['Sin título.png','Sin título2.png','Sin título3.png'], origin="C:\\Users\\hansn\\OneDrive\\Escritorio", destination='C:\\Users\\hansn\\Downloads'))
#print(Pypack.pack(files='all', origin=direccion1, destination=direccion2))