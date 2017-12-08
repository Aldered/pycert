#Cabrera Balderas Carlos Eduardo
#UNAM-CERT

import random
import string
''' 
Descripcion: Genera password aleatoria.
Recibe: Numero de mayusculas, minusculas y numeros
Devuelve: La password generada.
'''
def pass_gen():
	''' 
	Se inician las variables: un contador, nuestra lista, el alfabeto y numeros.
	'''
	i = 0 
	pw = []
	min = string.ascii_lowercase
	may = string.ascii_uppercase
	n = string.digits
	''' 
	Se pediran los datos.
	'''
	pass_len = int(raw_input('Longitud de la password: '))
	may_len = int(raw_input('Numero de mayusculas que tendra: '))
	min_len = int(raw_input('Numero de minusculas que tendra: '))
	n_len = int(raw_input('Numero de numeros que tendra: '))
	''' 
	Se pondra la longitud total para determinar si se estan agregando los 
	datos correctamente, Ejemplo pass_len = 5, may_len y min_len = 2 y
	n_len = 1, tendria que dar 0, para no ingresar pass_len = 5 y may_len = 20,
	si sucede se llama a si misma la funcion.
	'''
	len_tot = pass_len - may_len - min_len - n_len 
	
	if len_tot < 0:
		print 'Intente de nuevo.'
		pass_gen()
		''' 
		De lo contrario, mientras 0 sea menor que la longitud total agrega un valor
		de las minusculas.
		'''
	else:
		while i < pass_len:
			''' 
			i sera nuestro contador para validar el numero de mayusculas
			minusculas y digitos que nos piden, al final de hacer todo el
			ciclo, vuelve a iterar hasta que sea igual e imprime la lista. 
			'''
			if i <  min_len: 
				pw.append(random.choice(min))
				if i < may_len:
					pw.append(random.choice(may))
					if i < n_len:
						pw.append(random.choice(n))
			i = i + 1
			print pw
pass_gen()
