#Abrir archivo
miArchivo = open('miArchivo.txt','w')

#Obtener info del archivo
print('Name: ', miArchivo.name)
print('Esta cerrado: ', miArchivo.closed)
print('Esta abierto: ', miArchivo.mode)

#Escribir algo en el archivo
miArchivo.write('Me gusta el ciclismo')
miArchivo.write (' y natacion')
miArchivo.close()

#Agregar al archivo
miArchivo = open('miArchivo.txt','a')
miArchivo.write(' y tambien escalada')
miArchivo.close()

#Leer archivo
miArchivo = open('miArchivo.txt', 'r+')
texto = miArchivo.read(150)
print(texto)
