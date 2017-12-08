#Cabrera Balderas Carlos Eduardo
#UNAM-CERT
''' 
Descripcion: Indica si un numero es primo.
Recibe: Numero. 
Devuelve: Cierto o falso.
'''
def primo(x):
	''' 
	Si el numero es mayor o igual a 2 que es el primer primo...
	'''
	if x >= 2:
		''' 
		Si no da resultado de residuoo imprime falso, de lo contrario
		verdadero.
		'''
		if not x % 2:
			print 'False'
		else: 
			print 'True'
primo(37)
