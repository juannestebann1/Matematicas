import Configure as cf

#Archivo donde se creara toda las funciones de el modulo de matematicas

print(cf.AUTORES)

if cf.VERSION > 1.0:
	print("la version es la mas actualizada")
else:
	print("Debes actualizar de version a la " + str(cf.VERSION))
